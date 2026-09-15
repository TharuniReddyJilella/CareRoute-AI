import streamlit as st
import sys
from pathlib import Path
import io
from datetime import datetime


# ============================================================
# PATHS
# ============================================================

APP_DIR = Path(__file__).parent
PROJECT_DIR = APP_DIR.parent

sys.path.append(str(APP_DIR))


# ============================================================
# IMPORTS
# ============================================================

from questions import SYMPTOMS, TRANSLATIONS
from safety import check_red_flags
from triage import predict_department

from recommendations import (
    get_department_description,
    get_department_name
)

from maps import (
    get_nearby_hospitals_url,
    get_emergency_hospital_url
)


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="CareRoute AI",
    page_icon="🏥",
    layout="centered",
    initial_sidebar_state="collapsed"
)


# ============================================================
# SESSION STATE
# ============================================================

if "page" not in st.session_state:
    st.session_state.page = 1

if "language" not in st.session_state:
    st.session_state.language = "English"

if "patient_history" not in st.session_state:
    st.session_state.patient_history = []


# ============================================================
# UI TEXT
# ============================================================

UI = {

    # ========================================================
    # ENGLISH
    # ========================================================

    "English": {

        "title": "CareRoute AI",
        "subtitle": "Smart Healthcare Guidance",

        "language": "🌐 Select Your Language",
        "language_help": "Choose the language you want to use.",
        "continue": "Continue →",

        "what": "✨ What You Can Do",
        "what_subtitle":
            "Simple and accessible healthcare navigation.",

        "speak": "Speak Your Symptoms",
        "speak_desc":
            "Tell us what you are experiencing using your voice.",

        "department": "Get Department",
        "department_desc":
            "Receive a healthcare department recommendation.",

        "hospital": "Find Nearby Hospitals",
        "hospital_desc":
            "Open Google Maps to find nearby healthcare facilities.",

        # PAGE 2

        "back": "← Back",

        "page2_title":
            "Tell Us Your Symptoms",

        "page2_subtitle":
            "Speak your symptoms or select them manually.",

        "patient":
            "👤 Patient Information",

        "name":
            "Name",

        "name_placeholder":
            "Enter patient name",

        "age":
            "Age",

        "voice_title":
            "🎙️ Speak Your Symptoms",

        "voice_desc":
            "Describe what you are experiencing naturally.",

        "voice_instruction":
            "Click the microphone and speak clearly.",

        "record":
            "🎙️ Record Your Symptoms",

        "record_received":
            "✅ Voice recording received.",

        "understood":
            "📝 What we understood:",

        "detected":
            "🔎 Detected symptoms:",

        "voice_no_symptom":
            "No known symptom was detected from your speech. "
            "Please try again or select symptoms manually.",

        "voice_error":
            "We could not understand the voice recording. "
            "Please try recording again or select the symptoms manually.",

        "manual_title":
            "🩺 Select Symptoms",

        "manual_desc":
            "Optional: select any additional symptoms.",

        "symptom_question":
            "What symptoms are you experiencing?",

        "symptom_placeholder":
            "Select one or more symptoms",

        "additional":
            "📋 Additional Information",

        "duration":
            "How long have you had these symptoms?",

        "duration_options": [
            "Less than 1 day",
            "1–3 days",
            "4–7 days",
            "More than 1 week",
            "More than 1 month"
        ],

        "severity":
            "How severe are your symptoms?",

        "severity_options": [
            "Mild",
            "Moderate",
            "Severe"
        ],

        "recommend":
            "🔍 Find My Recommendation",

        "no_symptoms":
            "Please speak or select at least one symptom.",

        "urgent":
            "🚨 Urgent Attention Recommended",

        "urgent_message":
            "Some of the symptoms you selected may require urgent "
            "medical attention. Please seek immediate medical care "
            "or contact your local emergency service.",

        "urgent_warning":
            "Do not rely on this application for emergency medical "
            "decisions. Please seek immediate professional medical care.",

        "recommended":
            "🏥 Recommended Department",

        "why":
            "💡 Why this department?",

        "summary":
            "📄 Patient Summary",

        "summary_name":
            "Name",

        "summary_age":
            "Age",

        "summary_language":
            "Language",

        "summary_symptoms":
            "Symptoms",

        "summary_duration":
            "Duration",

        "summary_severity":
            "Severity",

        "summary_department":
            "Recommended Department",

        "nearby":
            "📍 Nearby Hospitals",

        "nearby_desc":
            "Find healthcare facilities related to the recommended department.",

        "maps":
            "📍 Open Google Maps",

        "listen":
            "🔊 Listen to Recommendation",

        "model_note":
            "This recommendation is based on the symptoms provided "
            "and the trained CareRoute AI model.",

        "new_patient":
            "👤 Continue With Another Patient",

        "new_patient_desc":
            "Start a fresh assessment for another patient.",

        "new_patient_button":
            "➕ Continue With Another Patient",

        "disclaimer":
            "⚠️ CareRoute AI provides general healthcare navigation only. "
            "It does not diagnose diseases or replace professional medical advice.",

        "footer":
            "CareRoute AI • Healthcare navigation support • Not a diagnostic system"
    },


    # ========================================================
    # TELUGU
    # ========================================================

    "Telugu": {

        "title":
            "కేర్‌రూట్ AI",

        "subtitle":
            "స్మార్ట్ ఆరోగ్య మార్గదర్శకత్వం",

        "language":
            "🌐 మీ భాషను ఎంచుకోండి",

        "language_help":
            "మీరు ఉపయోగించాలనుకునే భాషను ఎంచుకోండి.",

        "continue":
            "కొనసాగించండి →",

        "what":
            "✨ మీరు ఏమి చేయవచ్చు",

        "what_subtitle":
            "సులభమైన ఆరోగ్య మార్గదర్శకత్వం.",

        "speak":
            "మీ లక్షణాలను చెప్పండి",

        "speak_desc":
            "మీకు ఉన్న లక్షణాలను మీ స్వరంతో చెప్పండి.",

        "department":
            "విభాగాన్ని పొందండి",

        "department_desc":
            "మీ లక్షణాల ఆధారంగా ఆరోగ్య విభాగం సూచన పొందండి.",

        "hospital":
            "సమీపంలోని ఆసుపత్రులను కనుగొనండి",

        "hospital_desc":
            "సమీపంలోని ఆరోగ్య కేంద్రాలను కనుగొనడానికి Google Maps తెరవండి.",

        "back":
            "← వెనక్కి",

        "page2_title":
            "మీ లక్షణాలను చెప్పండి",

        "page2_subtitle":
            "మీ లక్షణాలను మాట్లాడండి లేదా మాన్యువల్‌గా ఎంచుకోండి.",

        "patient":
            "👤 రోగి సమాచారం",

        "name":
            "పేరు",

        "name_placeholder":
            "రోగి పేరును నమోదు చేయండి",

        "age":
            "వయస్సు",

        "voice_title":
            "🎙️ మీ లక్షణాలను మాట్లాడండి",

        "voice_desc":
            "మీకు ఉన్న సమస్యలను సహజంగా మాట్లాడి చెప్పండి.",

        "voice_instruction":
            "మైక్రోఫోన్‌పై క్లిక్ చేసి స్పష్టంగా మాట్లాడండి.",

        "record":
            "🎙️ మీ లక్షణాలను రికార్డ్ చేయండి",

        "record_received":
            "✅ మీ వాయిస్ రికార్డింగ్ అందింది.",

        "understood":
            "📝 మేము అర్థం చేసుకున్నది:",

        "detected":
            "🔎 గుర్తించిన లక్షణాలు:",

        "voice_no_symptom":
            "మీ మాటల నుండి తెలిసిన లక్షణం గుర్తించబడలేదు. "
            "మళ్ళీ ప్రయత్నించండి లేదా లక్షణాలను మాన్యువల్‌గా ఎంచుకోండి.",

        "voice_error":
            "వాయిస్ రికార్డింగ్‌ను అర్థం చేసుకోలేకపోయాము. "
            "దయచేసి మళ్ళీ రికార్డ్ చేయండి లేదా లక్షణాలను మాన్యువల్‌గా ఎంచుకోండి.",

        "manual_title":
            "🩺 లక్షణాలను ఎంచుకోండి",

        "manual_desc":
            "ఐచ్ఛికం: అవసరమైతే అదనపు లక్షణాలను ఎంచుకోండి.",

        "symptom_question":
            "మీకు ప్రస్తుతం ఏ లక్షణాలు ఉన్నాయి?",

        "symptom_placeholder":
            "ఒకటి లేదా అంతకంటే ఎక్కువ లక్షణాలను ఎంచుకోండి",

        "additional":
            "📋 అదనపు సమాచారం",

        "duration":
            "ఈ లక్షణాలు మీకు ఎంతకాలంగా ఉన్నాయి?",

        "duration_options": [
            "1 రోజు కంటే తక్కువ",
            "1–3 రోజులు",
            "4–7 రోజులు",
            "1 వారం కంటే ఎక్కువ",
            "1 నెల కంటే ఎక్కువ"
        ],

        "severity":
            "మీ లక్షణాల తీవ్రత ఎంత?",

        "severity_options": [
            "తక్కువ",
            "మధ్యస్థం",
            "తీవ్రమైనది"
        ],

        "recommend":
            "🔍 నా సిఫార్సును పొందండి",

        "no_symptoms":
            "దయచేసి కనీసం ఒక లక్షణాన్ని మాట్లాడండి లేదా ఎంచుకోండి.",

        "urgent":
            "🚨 అత్యవసర వైద్య సహాయం అవసరం కావచ్చు",

        "urgent_message":
            "మీరు ఎంచుకున్న కొన్ని లక్షణాలకు తక్షణ వైద్య సహాయం అవసరం కావచ్చు. "
            "దయచేసి వెంటనే వైద్య సహాయం పొందండి లేదా స్థానిక అత్యవసర సేవలను సంప్రదించండి.",

        "urgent_warning":
            "అత్యవసర వైద్య నిర్ణయాల కోసం ఈ అప్లికేషన్‌పై ఆధారపడకండి. "
            "వెంటనే వైద్య సహాయం పొందండి.",

        "recommended":
            "🏥 సిఫార్సు చేసిన విభాగం",

        "why":
            "💡 ఈ విభాగాన్ని ఎందుకు సూచించాము?",

        "summary":
            "📄 రోగి సారాంశం",

        "summary_name":
            "పేరు",

        "summary_age":
            "వయస్సు",

        "summary_language":
            "భాష",

        "summary_symptoms":
            "లక్షణాలు",

        "summary_duration":
            "లక్షణాల వ్యవధి",

        "summary_severity":
            "తీవ్రత",

        "summary_department":
            "సిఫార్సు చేసిన విభాగం",

        "nearby":
            "📍 సమీపంలోని ఆసుపత్రులు",

        "nearby_desc":
            "సిఫార్సు చేసిన విభాగానికి సంబంధించిన ఆరోగ్య కేంద్రాలను కనుగొనండి.",

        "maps":
            "📍 Google Maps తెరవండి",

        "listen":
            "🔊 సిఫార్సును వినండి",

        "model_note":
            "ఈ సిఫార్సు మీరు అందించిన లక్షణాలు మరియు CareRoute AI మోడల్‌పై ఆధారపడి ఉంటుంది.",

        "new_patient":
            "👤 మరొక రోగితో కొనసాగించండి",

        "new_patient_desc":
            "మరొక రోగి కోసం కొత్త ఆరోగ్య అంచనాను ప్రారంభించండి.",

        "new_patient_button":
            "➕ మరొక రోగితో కొనసాగించండి",

        "disclaimer":
            "⚠️ CareRoute AI సాధారణ ఆరోగ్య మార్గదర్శకత్వం కోసం మాత్రమే. "
            "ఇది వ్యాధులను నిర్ధారించదు మరియు వైద్యుల సలహాకు ప్రత్యామ్నాయం కాదు.",

        "footer":
            "కేర్‌రూట్ AI • ఆరోగ్య మార్గదర్శకత్వం • వ్యాధి నిర్ధారణ వ్యవస్థ కాదు"
    },


    # ========================================================
    # HINDI
    # ========================================================

    "Hindi": {

        "title":
            "CareRoute AI",

        "subtitle":
            "स्मार्ट स्वास्थ्य मार्गदर्शन",

        "language":
            "🌐 अपनी भाषा चुनें",

        "language_help":
            "वह भाषा चुनें जिसका आप उपयोग करना चाहते हैं।",

        "continue":
            "जारी रखें →",

        "what":
            "✨ आप क्या कर सकते हैं",

        "what_subtitle":
            "सरल और सुलभ स्वास्थ्य मार्गदर्शन।",

        "speak":
            "अपने लक्षण बोलें",

        "speak_desc":
            "अपनी समस्या के बारे में अपनी आवाज़ में बताएं।",

        "department":
            "विभाग की सिफारिश पाएं",

        "department_desc":
            "आपके लक्षणों के आधार पर स्वास्थ्य विभाग की सिफारिश पाएं।",

        "hospital":
            "पास के अस्पताल खोजें",

        "hospital_desc":
            "पास के स्वास्थ्य केंद्र खोजने के लिए Google Maps खोलें।",

        "back":
            "← वापस",

        "page2_title":
            "अपने लक्षण बताएं",

        "page2_subtitle":
            "अपने लक्षण बोलें या उन्हें मैन्युअल रूप से चुनें।",

        "patient":
            "👤 रोगी की जानकारी",

        "name":
            "नाम",

        "name_placeholder":
            "रोगी का नाम दर्ज करें",

        "age":
            "उम्र",

        "voice_title":
            "🎙️ अपने लक्षण बोलें",

        "voice_desc":
            "आप जो महसूस कर रहे हैं उसके बारे में स्वाभाविक रूप से बोलें।",

        "voice_instruction":
            "माइक्रोफोन पर क्लिक करें और स्पष्ट रूप से बोलें।",

        "record":
            "🎙️ अपने लक्षण रिकॉर्ड करें",

        "record_received":
            "✅ आपकी आवाज़ की रिकॉर्डिंग प्राप्त हुई।",

        "understood":
            "📝 हमने यह समझा:",

        "detected":
            "🔎 पहचाने गए लक्षण:",

        "voice_no_symptom":
            "आपकी आवाज़ से कोई ज्ञात लक्षण नहीं मिला। "
            "फिर से कोशिश करें या लक्षणों को मैन्युअल रूप से चुनें।",

        "voice_error":
            "आवाज़ की रिकॉर्डिंग को समझ नहीं सके। "
            "कृपया फिर से रिकॉर्ड करें या लक्षणों को मैन्युअल रूप से चुनें।",

        "manual_title":
            "🩺 लक्षण चुनें",

        "manual_desc":
            "वैकल्पिक: आवश्यकता होने पर अतिरिक्त लक्षण चुनें।",

        "symptom_question":
            "आपको वर्तमान में कौन से लक्षण हो रहे हैं?",

        "symptom_placeholder":
            "एक या अधिक लक्षण चुनें",

        "additional":
            "📋 अतिरिक्त जानकारी",

        "duration":
            "आपको ये लक्षण कितने समय से हैं?",

        "duration_options": [
            "1 दिन से कम",
            "1–3 दिन",
            "4–7 दिन",
            "1 सप्ताह से अधिक",
            "1 महीने से अधिक"
        ],

        "severity":
            "आपके लक्षण कितने गंभीर हैं?",

        "severity_options": [
            "हल्के",
            "मध्यम",
            "गंभीर"
        ],

        "recommend":
            "🔍 मेरी सिफारिश पाएं",

        "no_symptoms":
            "कृपया कम से कम एक लक्षण बोलें या चुनें।",

        "urgent":
            "🚨 तुरंत चिकित्सा सहायता की आवश्यकता हो सकती है",

        "urgent_message":
            "आपके द्वारा बताए गए कुछ लक्षणों के लिए तत्काल चिकित्सा सहायता की आवश्यकता हो सकती है। "
            "कृपया तुरंत चिकित्सा सहायता लें या स्थानीय आपातकालीन सेवा से संपर्क करें।",

        "urgent_warning":
            "आपातकालीन चिकित्सा निर्णयों के लिए इस एप्लिकेशन पर निर्भर न रहें। "
            "तुरंत पेशेवर चिकित्सा सहायता लें।",

        "recommended":
            "🏥 सुझाया गया विभाग",

        "why":
            "💡 यह विभाग क्यों सुझाया गया?",

        "summary":
            "📄 रोगी सारांश",

        "summary_name":
            "नाम",

        "summary_age":
            "उम्र",

        "summary_language":
            "भाषा",

        "summary_symptoms":
            "लक्षण",

        "summary_duration":
            "लक्षणों की अवधि",

        "summary_severity":
            "गंभीरता",

        "summary_department":
            "सुझाया गया विभाग",

        "nearby":
            "📍 पास के अस्पताल",

        "nearby_desc":
            "अनुशंसित विभाग से संबंधित स्वास्थ्य सुविधाएं खोजें।",

        "maps":
            "📍 Google Maps खोलें",

        "listen":
            "🔊 सुझाव सुनें",

        "model_note":
            "यह सुझाव आपके बताए गए लक्षणों और CareRoute AI के प्रशिक्षित मॉडल पर आधारित है।",

        "new_patient":
            "👤 दूसरे रोगी के साथ जारी रखें",

        "new_patient_desc":
            "दूसरे रोगी के लिए नया स्वास्थ्य मूल्यांकन शुरू करें।",

        "new_patient_button":
            "➕ दूसरे रोगी के साथ जारी रखें",

        "disclaimer":
            "⚠️ CareRoute AI केवल सामान्य स्वास्थ्य मार्गदर्शन प्रदान करता है। "
            "यह बीमारी का निदान नहीं करता और डॉक्टर की सलाह का विकल्प नहीं है।",

        "footer":
            "CareRoute AI • स्वास्थ्य मार्गदर्शन • निदान प्रणाली नहीं"
    }
}


# ============================================================
# VOICE LANGUAGE CODES
# ============================================================

VOICE_LANGUAGE_CODES = {
    "English": "en-IN",
    "Telugu": "te-IN",
    "Hindi": "hi-IN"
}


# ============================================================
# TEXT TO SPEECH LANGUAGE CODES
# ============================================================

TTS_LANGUAGE_CODES = {
    "English": "en",
    "Telugu": "te",
    "Hindi": "hi"
}


# ============================================================
# VOICE KEYWORDS
# ============================================================

VOICE_KEYWORDS = {

    "English": {

        "Headache": [
            "headache",
            "head pain"
        ],

        "Fever": [
            "fever",
            "temperature"
        ],

        "Cough": [
            "cough",
            "coughing"
        ],

        "Shortness of breath": [
            "shortness of breath",
            "difficulty breathing",
            "breathing problem",
            "breathlessness"
        ],

        "Chest discomfort": [
            "chest discomfort",
            "chest pain",
            "pain in chest"
        ],

        "Palpitations": [
            "palpitations",
            "heart beating fast",
            "heart racing"
        ],

        "Abdominal pain": [
            "abdominal pain",
            "stomach pain",
            "belly pain",
            "stomach ache"
        ],

        "Nausea": [
            "nausea",
            "feeling nauseous"
        ],

        "Vomiting": [
            "vomiting",
            "vomit",
            "throwing up"
        ],

        "Diarrhea": [
            "diarrhea",
            "loose motions",
            "loose stools"
        ],

        "Joint pain": [
            "joint pain",
            "pain in joints"
        ],

        "Back pain": [
            "back pain",
            "pain in back"
        ],

        "Skin rash": [
            "skin rash",
            "rash"
        ],

        "Itching": [
            "itching",
            "itchy"
        ],

        "Ear pain": [
            "ear pain",
            "pain in ear"
        ],

        "Hearing difficulty": [
            "hearing difficulty",
            "difficulty hearing",
            "hearing problem"
        ],

        "Sore throat": [
            "sore throat",
            "throat pain"
        ],

        "Nasal congestion": [
            "nasal congestion",
            "blocked nose",
            "stuffy nose"
        ],

        "Eye pain": [
            "eye pain",
            "pain in eye"
        ],

        "Blurred vision": [
            "blurred vision",
            "blurry vision"
        ],

        "Dizziness": [
            "dizziness",
            "dizzy",
            "feeling dizzy"
        ],

        "Numbness": [
            "numbness",
            "numb",
            "feeling numb"
        ],

        "Fatigue": [
            "fatigue",
            "tired",
            "very tired"
        ]
    },


    "Telugu": {

        "Headache": [
            "తలనొప్పి",
            "తల నొప్పి"
        ],

        "Fever": [
            "జ్వరం",
            "టెంపరేచర్"
        ],

        "Cough": [
            "దగ్గు"
        ],

        "Shortness of breath": [
            "శ్వాస తీసుకోవడంలో ఇబ్బంది",
            "శ్వాస ఇబ్బంది",
            "ఊపిరి తీసుకోవడం కష్టం"
        ],

        "Chest discomfort": [
            "ఛాతీలో అసౌకర్యం",
            "ఛాతి నొప్పి",
            "ఛాతీలో నొప్పి"
        ],

        "Palpitations": [
            "గుండె దడ",
            "గుండె వేగంగా కొట్టుకోవడం"
        ],

        "Abdominal pain": [
            "కడుపు నొప్పి",
            "పొట్ట నొప్పి"
        ],

        "Nausea": [
            "వికారం"
        ],

        "Vomiting": [
            "వాంతులు",
            "వాంతి"
        ],

        "Diarrhea": [
            "విరేచనాలు",
            "లూజ్ మోషన్స్"
        ],

        "Joint pain": [
            "కీళ్ల నొప్పి",
            "కీళ్ళ నొప్పి"
        ],

        "Back pain": [
            "వెన్నునొప్పి",
            "వెన్ను నొప్పి"
        ],

        "Skin rash": [
            "చర్మంపై దద్దుర్లు",
            "దద్దుర్లు"
        ],

        "Itching": [
            "దురద"
        ],

        "Ear pain": [
            "చెవి నొప్పి"
        ],

        "Hearing difficulty": [
            "వినికిడి సమస్య",
            "వినడం కష్టం"
        ],

        "Sore throat": [
            "గొంతు నొప్పి"
        ],

        "Nasal congestion": [
            "ముక్కు దిబ్బడ",
            "ముక్కు మూసుకుపోవడం"
        ],

        "Eye pain": [
            "కంటి నొప్పి"
        ],

        "Blurred vision": [
            "చూపు మసకబారడం",
            "మసకగా కనిపించడం"
        ],

        "Dizziness": [
            "తల తిరగడం",
            "తల తిరుగుతోంది"
        ],

        "Numbness": [
            "తిమ్మిరి",
            "మొద్దుబారడం"
        ],

        "Fatigue": [
            "అలసట",
            "చాలా అలసట"
        ]
    },


    # ========================================================
    # HINDI
    # ========================================================

    "Hindi": {

        "Headache": [
            "सिरदर्द",
            "सिर दर्द",
            "सिर में दर्द",
            "मेरे सिर में दर्द",
            "मुझे सिर में दर्द",
            "सिर में बहुत दर्द"
        ],

        "Fever": [
            "बुखार",
            "मुझे बुखार",
            "तेज बुखार",
            "बहुत तेज बुखार",
            "शरीर में गर्मी"
        ],

        "Cough": [
            "खांसी",
            "मुझे खांसी",
            "बहुत खांसी",
            "खांस रहा",
            "खांस रही"
        ],

        "Shortness of breath": [
            "सांस लेने में कठिनाई",
            "सांस लेने में दिक्कत",
            "सांस लेने में परेशानी",
            "सांस फूलना",
            "सांस लेने में समस्या",
            "सांस नहीं आ रही",
            "सांस लेने में मुश्किल",
            "सांस लेने में तकलीफ"
        ],

        "Chest discomfort": [
            "सीने में असहजता",
            "सीने में दर्द",
            "छाती में दर्द",
            "सीने में तकलीफ",
            "छाती में तकलीफ",
            "सीने में भारीपन",
            "छाती में भारीपन"
        ],

        "Palpitations": [
            "दिल की धड़कन तेज",
            "दिल तेजी से धड़कना",
            "दिल की धड़कन",
            "दिल बहुत तेज धड़क रहा है",
            "दिल जोर से धड़क रहा है",
            "दिल धड़क रहा है"
        ],

        "Abdominal pain": [
            "पेट दर्द",
            "पेट में दर्द",
            "मेरे पेट में दर्द",
            "मुझे पेट में दर्द",
            "पेट में बहुत दर्द"
        ],

        "Nausea": [
            "मतली",
            "जी मिचलाना",
            "मुझे मतली",
            "जी मिचला रहा है",
            "जी मिचला रही है"
        ],

        "Vomiting": [
            "उल्टी",
            "उल्टियां",
            "मुझे उल्टी",
            "उल्टी हो रही है",
            "उल्टी आ रही है"
        ],

        "Diarrhea": [
            "दस्त",
            "पतले दस्त",
            "बार बार दस्त",
            "लूज मोशन",
            "लूज मोशन हो रहे हैं",
            "बार बार लूज मोशन"
        ],

        "Joint pain": [
            "जोड़ों का दर्द",
            "जोड़ों में दर्द",
            "जोड़ों में तकलीफ",
            "मेरे जोड़ों में दर्द",
            "जोड़ों में बहुत दर्द"
        ],

        "Back pain": [
            "कमर दर्द",
            "पीठ दर्द",
            "कमर में दर्द",
            "पीठ में दर्द",
            "मेरी कमर में दर्द",
            "मेरी पीठ में दर्द"
        ],

        "Skin rash": [
            "त्वचा पर चकत्ते",
            "चकत्ते",
            "शरीर पर चकत्ते",
            "त्वचा पर दाने",
            "शरीर पर दाने",
            "दाने हो रहे हैं"
        ],

        "Itching": [
            "खुजली",
            "मुझे खुजली",
            "बहुत खुजली",
            "शरीर में खुजली",
            "त्वचा में खुजली"
        ],

        "Ear pain": [
            "कान में दर्द",
            "कान दर्द",
            "मेरे कान में दर्द",
            "कान में बहुत दर्द"
        ],

        "Hearing difficulty": [
            "सुनने में कठिनाई",
            "सुनने में दिक्कत",
            "सुनाई नहीं देना",
            "कम सुनाई देना",
            "सुनने में परेशानी",
            "सुनने में तकलीफ"
        ],

        "Sore throat": [
            "गले में खराश",
            "गले में दर्द",
            "गला दर्द",
            "मेरे गले में दर्द",
            "गले में तकलीफ",
            "गले में बहुत दर्द"
        ],

        "Nasal congestion": [
            "नाक बंद",
            "नाक बंद होना",
            "नाक बंद है",
            "नाक में जकड़न",
            "नाक बंद हो गई",
            "नाक से सांस नहीं आ रही"
        ],

        "Eye pain": [
            "आंखों में दर्द",
            "आंख में दर्द",
            "मेरी आंख में दर्द",
            "आंखों में तकलीफ",
            "आंख में बहुत दर्द"
        ],

        "Blurred vision": [
            "धुंधला दिखाई देना",
            "धुंधला दिखना",
            "साफ दिखाई नहीं देना",
            "दृष्टि धुंधली",
            "आंखों से धुंधला दिखना",
            "मुझे धुंधला दिखाई देता है"
        ],

        "Dizziness": [
            "चक्कर आना",
            "चक्कर",
            "मुझे चक्कर आ रहे हैं",
            "सिर घूमना",
            "सिर घूम रहा है",
            "बहुत चक्कर आ रहे हैं"
        ],

        "Numbness": [
            "सुन्नपन",
            "सुन्न होना",
            "हाथ सुन्न होना",
            "पैर सुन्न होना",
            "शरीर सुन्न होना",
            "हाथ में सुन्नपन",
            "पैर में सुन्नपन"
        ],

        "Fatigue": [
            "थकान",
            "बहुत थकान",
            "मुझे बहुत थकान",
            "कमजोरी",
            "बहुत कमजोरी",
            "मुझे कमजोरी महसूस हो रही है"
        ]
    }
}


# ============================================================
# DETECT VOICE SYMPTOMS
# ============================================================

def detect_voice_symptoms(transcript, language):

    if not transcript:
        return []

    transcript_lower = transcript.strip().lower()

    detected = []

    language_keywords = VOICE_KEYWORDS.get(
        language,
        {}
    )

    for symptom in SYMPTOMS:

        keywords = language_keywords.get(
            symptom,
            []
        )

        for keyword in keywords:

            if keyword.lower() in transcript_lower:

                detected.append(symptom)

                break

    return list(
        dict.fromkeys(detected)
    )


# ============================================================
# TEXT TO SPEECH
# ============================================================

def generate_voice_response(text, language):

    try:

        from gtts import gTTS

        audio_buffer = io.BytesIO()

        speech = gTTS(
            text=text,
            lang=TTS_LANGUAGE_CODES.get(
                language,
                "en"
            ),
            slow=False
        )

        speech.write_to_fp(
            audio_buffer
        )

        audio_buffer.seek(0)

        return audio_buffer

    except Exception:

        return None


# ============================================================
# PATIENT DATA RESET + HISTORY
# ============================================================


def clear_patient_data():

    keys_to_clear = [
        "patient_name",
        "patient_age",
        "manual_symptoms",
        "voice_input",
        "duration",
        "severity",
        "recommend_button",
        "voice_transcript",
        "voice_detected_symptoms",
        "all_selected_symptoms",
        "last_recommendation",
    ]

    for key in keys_to_clear:

        if key in st.session_state:
            del st.session_state[key]

    for index in range(len(SYMPTOMS)):

        checkbox_key = f"symptom_checkbox_{index}"

        if checkbox_key in st.session_state:
            del st.session_state[checkbox_key]

    st.session_state.manual_symptom_state = {
        symptom: False
        for symptom in SYMPTOMS
    }


def save_patient_history(
    name,
    age,
    symptoms,
    duration,
    severity,
    department,
    urgent=False
):

    history_record = {
        "name": name.strip() if name and name.strip() else "Not provided",
        "age": int(age),
        "symptoms": list(symptoms),
        "duration": duration,
        "severity": severity,
        "department": department,
        "urgent": urgent,
        "timestamp": datetime.now().strftime("%d %b %Y, %I:%M %p")
    }

    st.session_state.patient_history.append(history_record)


def show_page_three():

    language = st.session_state.get(
        "language",
        "English"
    )

    T = UI[language]

    history_text = {

        "English": {
            "back": "← Back to Assessment",
            "title": "Patient History",
            "subtitle": "Review previous CareRoute AI triage sessions.",
            "empty": "No patient history yet. Complete an assessment to see it here.",
            "patient": "Patient",
            "name": "Name",
            "age": "Age",
            "symptoms": "Symptoms",
            "duration": "Duration",
            "severity": "Severity",
            "department": "Recommended Department",
            "urgent": "Urgent Attention Recommended",
            "date": "Assessment Date",
            "new": "➕ Start New Patient",
            "clear": "🗑️ Clear History",
            "clear_confirm": "Are you sure you want to clear all patient history?",
            "yes": "Yes, Clear History",
            "no": "Cancel",
            "disclaimer": "History is stored only during the current app session and is not a medical record."
        },

        "Telugu": {
            "back": "← అంచనాకు తిరిగి వెళ్ళండి",
            "title": "రోగి చరిత్ర",
            "subtitle": "మునుపటి CareRoute AI ఆరోగ్య అంచనాలను చూడండి.",
            "empty": "ఇంకా రోగి చరిత్ర లేదు. అంచనాను పూర్తి చేసిన తర్వాత ఇక్కడ కనిపిస్తుంది.",
            "patient": "రోగి",
            "name": "పేరు",
            "age": "వయస్సు",
            "symptoms": "లక్షణాలు",
            "duration": "వ్యవధి",
            "severity": "తీవ్రత",
            "department": "సిఫార్సు చేసిన విభాగం",
            "urgent": "అత్యవసర వైద్య సహాయం అవసరం కావచ్చు",
            "date": "అంచనా తేదీ",
            "new": "➕ కొత్త రోగిని ప్రారంభించండి",
            "clear": "🗑️ చరిత్రను తొలగించండి",
            "clear_confirm": "మొత్తం రోగి చరిత్రను తొలగించాలా?",
            "yes": "అవును, చరిత్రను తొలగించండి",
            "no": "రద్దు",
            "disclaimer": "చరిత్ర ప్రస్తుత యాప్ సెషన్‌లో మాత్రమే నిల్వ చేయబడుతుంది మరియు ఇది వైద్య రికార్డు కాదు."
        },

        "Hindi": {
            "back": "← मूल्यांकन पर वापस जाएं",
            "title": "रोगी इतिहास",
            "subtitle": "पिछले CareRoute AI स्वास्थ्य मूल्यांकनों को देखें।",
            "empty": "अभी कोई रोगी इतिहास नहीं है। मूल्यांकन पूरा करने के बाद यह यहां दिखाई देगा।",
            "patient": "रोगी",
            "name": "नाम",
            "age": "उम्र",
            "symptoms": "लक्षण",
            "duration": "अवधि",
            "severity": "गंभीरता",
            "department": "सुझाया गया विभाग",
            "urgent": "तुरंत चिकित्सा सहायता की आवश्यकता हो सकती है",
            "date": "मूल्यांकन की तारीख",
            "new": "➕ नया रोगी शुरू करें",
            "clear": "🗑️ इतिहास साफ करें",
            "clear_confirm": "क्या आप पूरा रोगी इतिहास साफ करना चाहते हैं?",
            "yes": "हां, इतिहास साफ करें",
            "no": "रद्द करें",
            "disclaimer": "इतिहास केवल वर्तमान ऐप सत्र के दौरान संग्रहीत होता है और यह चिकित्सा रिकॉर्ड नहीं है।"
        }
    }[language]

    if st.button(
        history_text["back"],
        key="history_back_button"
    ):
        st.session_state.page = 2
        st.rerun()

    st.markdown(
        f'<div class="main-title">{history_text["title"]}</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="main-subtitle">{history_text["subtitle"]}</div>',
        unsafe_allow_html=True
    )

    history = st.session_state.get(
        "patient_history",
        []
    )

    if not history:

        st.info(
            history_text["empty"]
        )

    else:

        for index, record in enumerate(
            reversed(history),
            start=1
        ):

            display_department = get_department_name(
                record["department"],
                language
            )

            translated_symptoms = [
                TRANSLATIONS[language].get(
                    symptom,
                    symptom
                )
                for symptom in record["symptoms"]
            ]

            patient_number = (
                len(history) - index + 1
            )

            with st.container(border=True):

                st.markdown(
                    f"""
                    <div class="card-title"
                         style="text-align:left;font-size:22px;">
                        👤 {history_text["patient"]} {patient_number}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                col1, col2 = st.columns(2)

                with col1:

                    st.markdown(
                        f'**{history_text["name"]}:** '
                        f'{record["name"]}'
                    )

                    st.markdown(
                        f'**{history_text["age"]}:** '
                        f'{record["age"]}'
                    )

                    st.markdown(
                        f'**{history_text["duration"]}:** '
                        f'{record["duration"]}'
                    )

                    st.markdown(
                        f'**{history_text["severity"]}:** '
                        f'{record["severity"]}'
                    )

                with col2:

                    st.markdown(
                        f'**{history_text["department"]}:** '
                        f'{display_department}'
                    )

                    st.markdown(
                        f'**{history_text["date"]}:** '
                        f'{record["timestamp"]}'
                    )

                st.markdown(
                    f'**{history_text["symptoms"]}:** '
                    f'{", ".join(translated_symptoms)}'
                )

                if record["urgent"]:

                    st.warning(
                        f'🚨 {history_text["urgent"]}'
                    )

    st.write("")

    if st.button(
        history_text["new"],
        use_container_width=True,
        key="history_new_patient_button"
    ):

        clear_patient_data()

        st.session_state.page = 2

        st.rerun()

    if history:

        st.write("")

        if st.button(
            history_text["clear"],
            use_container_width=True,
            key="clear_history_button"
        ):

            st.session_state.show_clear_history_confirm = True

        if st.session_state.get(
            "show_clear_history_confirm",
            False
        ):

            st.warning(
                history_text["clear_confirm"]
            )

            confirm_col1, confirm_col2 = st.columns(2)

            with confirm_col1:

                if st.button(
                    history_text["yes"],
                    use_container_width=True,
                    key="confirm_clear_history"
                ):

                    st.session_state.patient_history = []
                    st.session_state.show_clear_history_confirm = False
                    st.rerun()

            with confirm_col2:

                if st.button(
                    history_text["no"],
                    use_container_width=True,
                    key="cancel_clear_history"
                ):

                    st.session_state.show_clear_history_confirm = False
                    st.rerun()

    st.write("")

    st.caption(
        history_text["disclaimer"]
    )

    st.caption(
        T["footer"]
    )


# ============================================================
# PAGE 1
# ============================================================

def show_page_one():

    # --------------------------------------------------------
    # LOGO
    # --------------------------------------------------------

    logo_path = (
        PROJECT_DIR
        / "assets"
        / "care_route_logo.png"
    )

    if logo_path.exists():

        # Center the logo
        left_col, center_col, right_col = st.columns(
            [1, 2, 1]
        )

        with center_col:
            st.image(
                str(logo_path),
                width=390
            )

    else:

        st.markdown(
            '<div class="main-title">🏥 CareRoute AI</div>',
            unsafe_allow_html=True
        )

    # --------------------------------------------------------
    # SUBTITLE
    # --------------------------------------------------------

    st.markdown(
        '<div class="main-subtitle">'
        'Smart Healthcare Guidance'
        '</div>',
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # LANGUAGE
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-title" style="font-size:24px;">'
        '🌐 Select Your Language'
        '</div>',
        unsafe_allow_html=True
    )

    st.caption(
        "Choose the language you want to use."
    )

    # --------------------------------------------------------
    # LANGUAGE OPTIONS
    # --------------------------------------------------------

    language_options = [
        "English",
        "తెలుగు",
        "हिन्दी"
    ]

    current_language = st.session_state.language

    if current_language == "English":
        current_display_language = "English"

    elif current_language == "Telugu":
        current_display_language = "తెలుగు"

    else:
        current_display_language = "हिन्दी"

    selected_display_language = st.selectbox(
        "Language",
        language_options,
        index=language_options.index(
            current_display_language
        ),
        label_visibility="collapsed",
        key="welcome_language"
    )

    # --------------------------------------------------------
    # CONVERT DISPLAY LANGUAGE
    # --------------------------------------------------------

    if selected_display_language == "English":

        selected_language = "English"

    elif selected_display_language == "తెలుగు":

        selected_language = "Telugu"

    elif selected_display_language == "हिन्दी":

        selected_language = "Hindi"

    else:

        selected_language = "English"

    st.session_state.language = selected_language

    T = UI[selected_language]

    # --------------------------------------------------------
    # CONTINUE
    # --------------------------------------------------------

    st.write("")

    if st.button(
        T["continue"],
        use_container_width=True,
        key="continue_button"
    ):

        st.session_state.page = 2
        st.rerun()

    # --------------------------------------------------------
    # WHAT YOU CAN DO
    # --------------------------------------------------------

    st.markdown(
        f"""
        <div class="section-title">
            {T["what"]}
        </div>

        <div class="section-subtitle">
            {T["what_subtitle"]}
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(
        3,
        gap="large"
    )

    with col1:

        with st.container(
            border=True
        ):

            st.markdown(
                '<div class="icon-circle">🎙️</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                f"""
                <div class="card-title">
                    {T["speak"]}
                </div>

                <div class="card-text">
                    {T["speak_desc"]}
                </div>
                """,
                unsafe_allow_html=True
            )

    with col2:

        with st.container(
            border=True
        ):

            st.markdown(
                '<div class="icon-circle">🩺</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                f"""
                <div class="card-title">
                    {T["department"]}
                </div>

                <div class="card-text">
                    {T["department_desc"]}
                </div>
                """,
                unsafe_allow_html=True
            )

    with col3:

        with st.container(
            border=True
        ):

            st.markdown(
                '<div class="icon-circle">📍</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                f"""
                <div class="card-title">
                    {T["hospital"]}
                </div>

                <div class="card-text">
                    {T["hospital_desc"]}
                </div>
                """,
                unsafe_allow_html=True
            )

    st.write("")

    st.caption(
        T["disclaimer"]
    )

# ============================================================
# PAGE 2
# ============================================================

def show_page_two():

    language = st.session_state.get(
        "language",
        "English"
    )

    T = UI[language]

    # ========================================================
    # BACK
    # ========================================================

    if st.button(
        T["back"],
        key="back_button"
    ):
        st.session_state.page = 1
        st.rerun()

    # ========================================================
    # PAGE TITLE
    # ========================================================

    st.markdown(
        f"""
        <div class="main-title">
            {T["page2_title"]}
        </div>

        <div class="main-subtitle">
            {T["page2_subtitle"]}
        </div>
        """,
        unsafe_allow_html=True
    )

    # ========================================================
    # PATIENT INFORMATION
    # ========================================================

    with st.container(border=True):

        st.markdown(
            f"""
            <div class="card-title"
                 style="font-size:23px;text-align:left;">
                {T["patient"]}
            </div>
            """,
            unsafe_allow_html=True
        )

        col1, col2 = st.columns(2)

        with col1:

            st.text_input(
                T["name"],
                placeholder=T["name_placeholder"],
                key="patient_name"
            )

        with col2:

            st.number_input(
                T["age"],
                min_value=1,
                max_value=120,
                value=18,
                step=1,
                key="patient_age"
            )

    # ========================================================
    # VOICE INPUT
    # ========================================================

    with st.container(border=True):

        st.markdown(
            f"""
            <div class="card-title"
                 style="font-size:25px;text-align:left;">
                {T["voice_title"]}
            </div>

            <div class="card-text"
                 style="text-align:left;">
                {T["voice_desc"]}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.caption(
            T["voice_instruction"]
        )

        voice_audio = st.audio_input(
            T["record"],
            key="voice_input"
        )

    # ========================================================
    # VOICE RECOGNITION
    # ========================================================

    voice_detected_symptoms = []
    voice_transcript = ""

    if voice_audio is not None:

        st.success(
            T["record_received"]
        )

        try:

            import io
            import speech_recognition as sr

            # ------------------------------------------------
            # Create recognizer
            # ------------------------------------------------

            recognizer = sr.Recognizer()

            recognizer.dynamic_energy_threshold = True
            recognizer.energy_threshold = 200
            recognizer.pause_threshold = 1.0
            recognizer.phrase_threshold = 0.2
            recognizer.non_speaking_duration = 0.5

            # ------------------------------------------------
            # Read recorded audio
            # ------------------------------------------------

            audio_bytes = voice_audio.getvalue()

            if not audio_bytes:

                st.warning(
                    T["voice_no_symptom"]
                )

            else:

                audio_file = sr.AudioFile(
                    io.BytesIO(audio_bytes)
                )

                # IMPORTANT:
                # Do not use adjust_for_ambient_noise()
                # on an already-recorded audio file.

                with audio_file as source:

                    audio_data = recognizer.record(
                        source
                    )

                # ------------------------------------------------
                # TRY ALL THREE LANGUAGES
                # ------------------------------------------------
                #
                # This is the main fix.
                #
                # Even if the UI language is English,
                # Hindi/Telugu speech can still be recognized.
                # ------------------------------------------------

                recognition_languages = [
                    ("English", "en-IN"),
                    ("English-US", "en-US"),
                    ("Hindi", "hi-IN"),
                    ("Telugu", "te-IN")
                ]

                all_transcripts = []
                recognition_errors = []

                for language_name, recognition_language in (
                    recognition_languages
                ):

                    try:

                        result = recognizer.recognize_google(
                            audio_data,
                            language=recognition_language,
                            show_all=True
                        )

                        if isinstance(result, dict):

                            alternatives = result.get(
                                "alternative",
                                []
                            )

                            for alternative in alternatives:

                                transcript = alternative.get(
                                    "transcript",
                                    ""
                                )

                                if transcript.strip():

                                    all_transcripts.append(
                                        (
                                            language_name,
                                            transcript.strip()
                                        )
                                    )

                        elif isinstance(result, str):

                            if result.strip():

                                all_transcripts.append(
                                    (
                                        language_name,
                                        result.strip()
                                    )
                                )

                    except sr.UnknownValueError:

                        recognition_errors.append(
                            f"{language_name}: "
                            "speech was not understood"
                        )

                    except sr.RequestError as error:

                        recognition_errors.append(
                            f"{language_name}: "
                            f"Google service error - {error}"
                        )

                    except Exception as error:

                        recognition_errors.append(
                            f"{language_name}: "
                            f"{error}"
                        )

                # ------------------------------------------------
                # REMOVE DUPLICATES
                # ------------------------------------------------

                unique_transcripts = []

                seen = set()

                for language_name, transcript in (
                    all_transcripts
                ):

                    key = transcript.lower().strip()

                    if key not in seen:

                        seen.add(key)

                        unique_transcripts.append(
                            (
                                language_name,
                                transcript
                            )
                        )

                all_transcripts = (
                    unique_transcripts
                )

                # ------------------------------------------------
                # SYMPTOM PHRASES
                # ------------------------------------------------

                voice_keywords = {

                    "Headache": [
                        "headache",
                        "head pain",
                        "pain in my head",
                        "सिरदर्द",
                        "सिर दर्द",
                        "सिर में दर्द",
                        "तలనొప్పి",
                        "తలనొప్పి",
                        "తల నొప్పి"
                    ],

                    "Fever": [
                        "fever",
                        "high fever",
                        "I have fever",
                        "बुखार",
                        "मुझे बुखार",
                        "तेज बुखार",
                        "జ్వరం",
                        "నాకు జ్వరం",
                        "తీవ్రమైన జ్వరం"
                    ],

                    "Cough": [
                        "cough",
                        "I have cough",
                        "खांसी",
                        "मुझे खांसी",
                        "దగ్గు",
                        "నాకు దగ్గు"
                    ],

                    "Shortness of breath": [
                        "shortness of breath",
                        "difficulty breathing",
                        "difficulty in breathing",
                        "trouble breathing",
                        "breathing problem",
                        "can't breathe",
                        "cannot breathe",
                        "सांस लेने में कठिनाई",
                        "सांस लेने में दिक्कत",
                        "सांस लेने में परेशानी",
                        "सांस फूलना",
                        "सांस लेने में समस्या",
                        "శ్వాస తీసుకోవడంలో ఇబ్బంది",
                        "శ్వాస తీసుకోవడం కష్టం",
                        "ఊపిరి తీసుకోవడంలో ఇబ్బంది"
                    ],

                    "Chest discomfort": [
                        "chest discomfort",
                        "chest pain",
                        "pain in chest",
                        "chest tightness",
                        "सीने में दर्द",
                        "सीने में तकलीफ",
                        "छाती में दर्द",
                        "छाती में तकलीफ",
                        "ఛాతీలో నొప్పి",
                        "ఛాతీలో అసౌకర్యం",
                        "ఛాతి నొప్పి"
                    ],

                    "Palpitations": [
                        "palpitations",
                        "heart beating fast",
                        "heart is beating fast",
                        "fast heartbeat",
                        "दिल की धड़कन तेज",
                        "दिल तेजी से धड़कना",
                        "दिल बहुत तेज धड़क रहा है",
                        "గుండె దడ",
                        "గుండె వేగంగా కొట్టుకోవడం"
                    ],

                    "Abdominal pain": [
                        "abdominal pain",
                        "stomach pain",
                        "stomach ache",
                        "pain in stomach",
                        "पेट दर्द",
                        "पेट में दर्द",
                        "मेरे पेट में दर्द",
                        "కడుపు నొప్పి",
                        "కడుపులో నొప్పి"
                    ],

                    "Nausea": [
                        "nausea",
                        "feeling nauseous",
                        "feel nauseous",
                        "मतली",
                        "जी मिचलाना",
                        "मुझे मतली",
                        "వికారం",
                        "వికారం గా ఉంది"
                    ],

                    "Vomiting": [
                        "vomiting",
                        "vomit",
                        "throwing up",
                        "उल्टी",
                        "उल्टियां",
                        "मुझे उल्टी",
                        "వాంతులు",
                        "వాంతి"
                    ],

                    "Diarrhea": [
                        "diarrhea",
                        "loose motions",
                        "loose motion",
                        "frequent loose motions",
                        "दस्त",
                        "पतले दस्त",
                        "लूज मोशन",
                        "విరేచనాలు",
                        "లూజ్ మోషన్స్"
                    ],

                    "Joint pain": [
                        "joint pain",
                        "pain in joints",
                        "joints are painful",
                        "जोड़ों का दर्द",
                        "जोड़ों में दर्द",
                        "मेरे जोड़ों में दर्द",
                        "కీళ్ల నొప్పి",
                        "కీళ్లలో నొప్పి"
                    ],

                    "Back pain": [
                        "back pain",
                        "pain in my back",
                        "lower back pain",
                        "कमर दर्द",
                        "पीठ दर्द",
                        "कमर में दर्द",
                        "पीठ में दर्द",
                        "వెన్నునొప్పి",
                        "వెన్నులో నొప్పి"
                    ],

                    "Skin rash": [
                        "skin rash",
                        "rash",
                        "skin rashes",
                        "चकत्ते",
                        "त्वचा पर चकत्ते",
                        "शरीर पर चकत्ते",
                        "त्वचा पर दाने",
                        "చర్మంపై దద్దుర్లు",
                        "చర్మంపై దద్దుర్లు వచ్చాయి"
                    ],

                    "Itching": [
                        "itching",
                        "itchy",
                        "खुजली",
                        "मुझे खुजली",
                        "बहुत खुजली",
                        "దురద",
                        "నాకు దురద"
                    ],

                    "Ear pain": [
                        "ear pain",
                        "pain in ear",
                        "earache",
                        "कान में दर्द",
                        "कान दर्द",
                        "मेरे कान में दर्द",
                        "చెవి నొప్పి",
                        "చెవిలో నొప్పి"
                    ],

                    "Hearing difficulty": [
                        "hearing difficulty",
                        "difficulty hearing",
                        "cannot hear",
                        "can't hear",
                        "कम सुनाई देना",
                        "सुनने में दिक्कत",
                        "सुनाई नहीं देना",
                        "వినికిడి సమస్య",
                        "సరిగ్గా వినిపించడం లేదు"
                    ],

                    "Sore throat": [
                        "sore throat",
                        "throat pain",
                        "pain in throat",
                        "गले में खराश",
                        "गले में दर्द",
                        "गला दर्द",
                        "గొంతు నొప్పి",
                        "గొంతులో నొప్పి"
                    ],

                    "Nasal congestion": [
                        "nasal congestion",
                        "blocked nose",
                        "stuffy nose",
                        "nose is blocked",
                        "नाक बंद",
                        "नाक बंद होना",
                        "नाक बंद है",
                        "ముక్కు దిబ్బడ",
                        "ముక్కు మూసుకుపోయింది"
                    ],

                    "Eye pain": [
                        "eye pain",
                        "pain in eye",
                        "eyes hurt",
                        "आंखों में दर्द",
                        "आंख में दर्द",
                        "मेरी आंख में दर्द",
                        "కంటి నొప్పి",
                        "కంటిలో నొప్పి"
                    ],

                    "Blurred vision": [
                        "blurred vision",
                        "blurry vision",
                        "vision is blurry",
                        "cannot see clearly",
                        "धुंधला दिखाई देना",
                        "धुंधला दिखना",
                        "साफ दिखाई नहीं देना",
                        "చూపు మసకబారడం",
                        "సరిగ్గా కనిపించడం లేదు"
                    ],

                    "Dizziness": [
                        "dizziness",
                        "dizzy",
                        "feeling dizzy",
                        "चक्कर आना",
                        "चक्कर",
                        "मुझे चक्कर आ रहे हैं",
                        "सिर घूमना",
                        "తల తిరగడం",
                        "చక్కర్లు వస్తున్నాయి"
                    ],

                    "Numbness": [
                        "numbness",
                        "numb",
                        "hand is numb",
                        "leg is numb",
                        "सुन्नपन",
                        "सुन्न होना",
                        "हाथ सुन्न होना",
                        "पैर सुन्न होना",
                        "తిమ్మిరి",
                        "చేతి మొద్దుబారడం",
                        "కాలు మొద్దుబారడం"
                    ],

                    "Fatigue": [
                        "fatigue",
                        "tired",
                        "very tired",
                        "weakness",
                        "feeling weak",
                        "थकान",
                        "बहुत थकान",
                        "मुझे बहुत थकान",
                        "कमजोरी",
                        "बहुत कमजोरी",
                        "అలసట",
                        "చాలా అలసట",
                        "బలహీనంగా ఉంది"
                    ]
                }

                # ------------------------------------------------
                # DETECT SYMPTOMS FROM TRANSCRIPT
                # ------------------------------------------------

                def detect_from_text(text):

                    normalized_text = (
                        text.lower()
                        .strip()
                    )

                    detected = []

                    for symptom, keywords in (
                        voice_keywords.items()
                    ):

                        for keyword in keywords:

                            if keyword.lower() in (
                                normalized_text
                            ):

                                detected.append(
                                    symptom
                                )

                                break

                    return detected

                # ------------------------------------------------
                # FIND BEST TRANSCRIPT
                # ------------------------------------------------

                best_transcript = ""
                best_language = ""
                best_symptoms = []

                for language_name, transcript in (
                    all_transcripts
                ):

                    detected = detect_from_text(
                        transcript
                    )

                    # Prefer transcript that detected
                    # the highest number of symptoms.

                    if len(detected) > len(
                        best_symptoms
                    ):

                        best_transcript = transcript
                        best_language = language_name
                        best_symptoms = detected

                # ------------------------------------------------
                # FALLBACK:
                # If no transcript has matched symptoms,
                # still display the first recognized text.
                # ------------------------------------------------

                if not best_transcript and (
                    all_transcripts
                ):

                    best_language, best_transcript = (
                        all_transcripts[0]
                    )

                    best_symptoms = detect_from_text(
                        best_transcript
                    )

                # ------------------------------------------------
                # SUCCESS
                # ------------------------------------------------

                if best_transcript:

                    voice_transcript = (
                        best_transcript
                    )

                    voice_detected_symptoms = (
                        best_symptoms
                    )

                    st.info(
                        f"**{T['understood']}**\n\n"
                        f"{voice_transcript}"
                    )

                    st.caption(
                        f"Recognition language: "
                        f"{best_language}"
                    )

                    if voice_detected_symptoms:

                        translated_detected = [

                            TRANSLATIONS[
                                language
                            ].get(
                                symptom,
                                symptom
                            )

                            for symptom
                            in voice_detected_symptoms
                        ]

                        st.success(
                            f"**{T['detected']}** "
                            f"{', '.join(translated_detected)}"
                        )

                    else:

                        st.warning(
                            T["voice_no_symptom"]
                        )

                        st.caption(
                            "Your speech was recognized, "
                            "but no matching symptom phrase "
                            "was found."
                        )

                # ------------------------------------------------
                # NO TRANSCRIPT
                # ------------------------------------------------

                else:

                    st.warning(
                        T["voice_no_symptom"]
                    )

                    with st.expander(
                        "Voice recognition details"
                    ):

                        if recognition_errors:

                            for message in (
                                recognition_errors
                            ):

                                st.write(
                                    message
                                )

                        else:

                            st.write(
                                "No speech transcript was returned."
                            )

        except Exception as error:

            st.error(
                T["voice_error"]
            )

            with st.expander(
                "Voice processing details"
            ):

                st.write(
                    str(error)
                )

    # ========================================================
    # MANUAL SYMPTOMS
    # ========================================================

    with st.container(border=True):

        st.markdown(
            f"""
            <div class="card-title"
                 style="font-size:23px;text-align:left;">
                {T["manual_title"]}
            </div>

            <div class="card-text"
                 style="text-align:left;">
                {T["manual_desc"]}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div style="
                color:#07538c;
                font-size:17px;
                font-weight:600;
                margin-top:10px;
                margin-bottom:10px;
            ">
                {T["symptom_question"]}
            </div>
            """,
            unsafe_allow_html=True
        )

        # ----------------------------------------------------
        # CHECKBOXES
        # ----------------------------------------------------

        symptom_col1, symptom_col2 = st.columns(2)

        for index, english_symptom in enumerate(
            SYMPTOMS
        ):

            translated_symptom = (
                TRANSLATIONS[
                    language
                ][english_symptom]
            )

            checkbox_key = (
                f"symptom_checkbox_{index}"
            )

            if index % 2 == 0:

                with symptom_col1:

                    st.checkbox(
                        translated_symptom,
                        key=checkbox_key
                    )

            else:

                with symptom_col2:

                    st.checkbox(
                        translated_symptom,
                        key=checkbox_key
                    )

    # ========================================================
    # GET MANUAL SYMPTOMS
    # ========================================================

    selected_symptoms = []

    for index, english_symptom in enumerate(
        SYMPTOMS
    ):

        checkbox_key = (
            f"symptom_checkbox_{index}"
        )

        if st.session_state.get(
            checkbox_key,
            False
        ):

            selected_symptoms.append(
                english_symptom
            )

    # ========================================================
    # COMBINE VOICE + MANUAL
    # ========================================================

    all_selected_symptoms = list(
        dict.fromkeys(
            selected_symptoms
            +
            voice_detected_symptoms
        )
    )

    # ========================================================
    # SELECTED SYMPTOMS
    # ========================================================

    if all_selected_symptoms:

        translated_current = [

            TRANSLATIONS[
                language
            ][symptom]

            for symptom
            in all_selected_symptoms
        ]

        st.info(
            f"**{T['summary_symptoms']}:** "
            f"{', '.join(translated_current)}"
        )

    # ========================================================
    # ADDITIONAL INFORMATION
    # ========================================================

    with st.container(border=True):

        st.header(
            T["additional"]
        )

        col3, col4 = st.columns(2)

        with col3:

            duration = st.selectbox(
                T["duration"],
                T["duration_options"],
                key="duration"
            )

        with col4:

            severity = st.select_slider(
                T["severity"],
                options=T["severity_options"],
                value=T["severity_options"][1],
                key="severity_slider"
            )

       # ========================================================
    # RECOMMENDATION
    # ========================================================

    st.write("")

    recommend = st.button(
        T["recommend"],
        use_container_width=True,
        key="recommend_button"
    )

    if recommend:

        # ====================================================
        # CHECK SYMPTOMS
        # ====================================================

        if not all_selected_symptoms:

            st.warning(
                T["no_symptoms"]
            )

            return

        # ====================================================
        # PATIENT DETAILS
        # ====================================================

        patient_name = st.session_state.get(
            "patient_name",
            ""
        )

        patient_age = st.session_state.get(
            "patient_age",
            18
        )

        if patient_name.strip():

            display_name = patient_name

        else:

            if language == "English":

                display_name = "Not provided"

            elif language == "Telugu":

                display_name = "పేరు ఇవ్వలేదు"

            else:

                display_name = "नाम नहीं दिया गया"

        # ====================================================
        # TRANSLATED SYMPTOMS
        # ====================================================

        translated_final_symptoms = [
            TRANSLATIONS[language][symptom]
            for symptom in all_selected_symptoms
        ]

        # ====================================================
        # LANGUAGE DISPLAY
        # ====================================================

        language_display = {
            "English": "English",
            "Telugu": "తెలుగు",
            "Hindi": "हिन्दी"
        }

        # ====================================================
        # SAFETY CHECK
        # ====================================================

        is_red_flag = check_red_flags(
            all_selected_symptoms,
            severity
        )

        # ====================================================
        # PATIENT REPORT
        # ====================================================

        st.write("")

        st.divider()

        st.subheader(
            T["summary"]
        )

        report_data = {

            T["summary_name"]:
                display_name,

            T["summary_age"]:
                str(patient_age),

            T["summary_language"]:
                language_display[language],

            T["summary_symptoms"]:
                ", ".join(
                    translated_final_symptoms
                ),

            T["summary_duration"]:
                duration,

            T["summary_severity"]:
                severity
        }

        with st.container(
            border=True
        ):

            for label, value in report_data.items():

                st.markdown(
                    f"""
                    <div style="
                        padding:8px 0;
                        font-size:17px;
                    ">
                        <strong>{label}:</strong>
                        {value}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        # ====================================================
        # PREDICT DEPARTMENT
        # ====================================================

        try:

            department = predict_department(
                all_selected_symptoms
            )

            display_department = (
                get_department_name(
                    department,
                    language
                )
            )

            department_description = (
                get_department_description(
                    department,
                    language
                )
            )

            # =================================================
            # SAVE HISTORY
            # =================================================

            save_patient_history(
                patient_name,
                patient_age,
                all_selected_symptoms,
                duration,
                severity,
                department,
                urgent=is_red_flag
            )

            # =================================================
            # RECOMMENDED DEPARTMENT
            # =================================================

            st.write("")

            st.markdown(
                '<div class="result-icon">🏥</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                f"""
                <div class="result-title">
                    {T["recommended"]}
                </div>

                <div style="
                    text-align:center;
                    color:#07538c;
                    font-size:30px;
                    font-weight:800;
                    margin-top:8px;
                ">
                    {display_department}
                </div>
                """,
                unsafe_allow_html=True
            )

            # =================================================
            # WHY THIS DEPARTMENT?
            # =================================================

            st.subheader(
                T["why"]
            )

            st.info(
                department_description
            )

            # =================================================
            # SAFETY MESSAGE
            # =================================================

            if is_red_flag:

                st.write("")

                st.error(
                    T["urgent"]
                )

                st.warning(
                    T["urgent_message"]
                )

                st.warning(
                    T["urgent_warning"]
                )

                emergency_url = (
                    get_emergency_hospital_url()
                )

                st.link_button(
                    "📍 Find Emergency Care on Google Maps",
                    emergency_url,
                    use_container_width=True
                )

                urgent_voice = (
                    generate_voice_response(
                        T["urgent_message"],
                        language
                    )
                )

                if urgent_voice is not None:

                    st.subheader(
                        T["listen"]
                    )

                    st.audio(
                        urgent_voice,
                        format="audio/mp3"
                    )

            # =================================================
            # DEPARTMENT IN SUMMARY
            # =================================================

            st.subheader(
                T["summary_department"]
            )

            st.success(
                display_department
            )

            # =================================================
            # NEARBY HOSPITALS
            # =================================================

            st.subheader(
                T["nearby"]
            )

            st.write(
                T["nearby_desc"]
            )

            maps_url = (
                get_nearby_hospitals_url(
                    department
                )
            )

            st.link_button(
                T["maps"],
                maps_url,
                use_container_width=True
            )

            # =================================================
            # VOICE OUTPUT
            # =================================================

            speech_text = (
                f"{T['recommended']}. "
                f"{display_department}. "
                f"{department_description}"
            )

            if is_red_flag:

                speech_text += " " + (
                    T["urgent_message"]
                )

            voice_result = (
                generate_voice_response(
                    speech_text,
                    language
                )
            )

            if voice_result is not None:

                st.subheader(
                    T["listen"]
                )

                st.audio(
                    voice_result,
                    format="audio/mp3"
                )

            # =================================================
            # MODEL NOTE
            # =================================================

            st.caption(
                T["model_note"]
            )

        except Exception as error:

            st.error(
                "Unable to generate the recommendation."
            )

            st.exception(
                error
            )
    # ========================================================
    # PATIENT HISTORY
    # ========================================================

    st.write("")

    st.divider()

    st.subheader(
        "📋 Patient History"
    )

    st.caption(
        "View completed patient assessments and previous recommendations."
    )

    if st.button(
        "📋 View Patient History",
        use_container_width=True,
        key="view_history_button"
    ):

        st.session_state.page = 3
        st.rerun()

    # ========================================================
    # FOOTER
    # ========================================================

    st.write("")

    st.caption(
        T["disclaimer"]
    )

    st.caption(
        T["footer"]
    )
# ============================================================
# CSS
# ============================================================


st.markdown(
    """
    <style>

    .stApp {

        background:
            radial-gradient(
                circle at 5% 15%,
                rgba(92, 211, 255, 0.14),
                transparent 28%
            ),

            radial-gradient(
                circle at 95% 75%,
                rgba(92, 211, 255, 0.12),
                transparent 28%
            ),

            #ffffff;
    }


    .main-title {

        text-align: center;

        color: #07538c;

        font-size: 36px;

        font-weight: 800;

        margin-bottom: 4px;
    }


    .main-subtitle {

        text-align: center;

        color: #54799c;

        font-size: 18px;

        margin-bottom: 30px;
    }


    .section-title {

        text-align: center;

        color: #07538c;

        font-size: 29px;

        font-weight: 800;

        margin-top: 35px;

        margin-bottom: 5px;
    }


    .section-subtitle {

        text-align: center;

        color: #54799c;

        font-size: 16px;

        margin-bottom: 25px;
    }


    .card-title {

        color: #07538c;

        font-size: 20px;

        font-weight: 750;

        text-align: center;
    }


    .card-text {

        color: #54799c;

        font-size: 15px;

        line-height: 1.5;

        text-align: center;
    }


    .icon-circle {

        width: 105px;

        height: 105px;

        border-radius: 50%;

        background: #edfaff;

        margin: 0 auto 15px auto;

        display: flex;

        align-items: center;

        justify-content: center;

        font-size: 55px;
    }


    .result-title {

        text-align: center;

        color: #07538c;

        font-size: 30px;

        font-weight: 800;
    }


    .result-icon {

        text-align: center;

        font-size: 48px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# PAGE ROUTING
# ============================================================

if st.session_state.page == 1:

    show_page_one()

elif st.session_state.page == 2:

    show_page_two()

elif st.session_state.page == 3:

    show_page_three()
