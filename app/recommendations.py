# CareRoute AI - Multilingual Department Recommendations


DEPARTMENT_DESCRIPTIONS = {

    "English": {

        "General Medicine":
            "For common, general, or unclear symptoms and conditions.",

        "Cardiology":
            "For symptoms related to the heart and circulation.",

        "Pulmonology":
            "For symptoms related to the lungs and breathing.",

        "Neurology":
            "For symptoms involving the brain, nerves, or nervous system.",

        "Dermatology":
            "For skin, hair, and nail related concerns.",

        "Gastroenterology":
            "For digestive system and gastrointestinal concerns.",

        "ENT":
            "For ear, nose, throat, and related concerns.",

        "Orthopedics":
            "For bones, joints, muscles, and movement-related concerns.",

        "Ophthalmology":
            "For eye and vision-related concerns.",

        "Gynecology":
            "For female reproductive and gynecological concerns."
    },


    "Telugu": {

        "General Medicine":
            "సాధారణమైన, స్పష్టంగా గుర్తించలేని లేదా వివిధ రకాల లక్షణాల కోసం ఈ విభాగాన్ని సంప్రదించవచ్చు.",

        "Cardiology":
            "గుండె మరియు రక్త ప్రసరణకు సంబంధించిన లక్షణాల కోసం ఈ విభాగాన్ని సంప్రదించవచ్చు.",

        "Pulmonology":
            "ఊపిరితిత్తులు మరియు శ్వాసకు సంబంధించిన లక్షణాల కోసం ఈ విభాగాన్ని సంప్రదించవచ్చు.",

        "Neurology":
            "మెదడు, నరాలు మరియు నాడీ వ్యవస్థకు సంబంధించిన లక్షణాల కోసం ఈ విభాగాన్ని సంప్రదించవచ్చు.",

        "Dermatology":
            "చర్మం, జుట్టు మరియు గోళ్లకు సంబంధించిన సమస్యల కోసం ఈ విభాగాన్ని సంప్రదించవచ్చు.",

        "Gastroenterology":
            "జీర్ణ వ్యవస్థ మరియు కడుపుకు సంబంధించిన సమస్యల కోసం ఈ విభాగాన్ని సంప్రదించవచ్చు.",

        "ENT":
            "చెవి, ముక్కు మరియు గొంతుకు సంబంధించిన సమస్యల కోసం ఈ విభాగాన్ని సంప్రదించవచ్చు.",

        "Orthopedics":
            "ఎముకలు, కీళ్లు, కండరాలు మరియు కదలికలకు సంబంధించిన సమస్యల కోసం ఈ విభాగాన్ని సంప్రదించవచ్చు.",

        "Ophthalmology":
            "కళ్ళు మరియు చూపుకు సంబంధించిన సమస్యల కోసం ఈ విభాగాన్ని సంప్రదించవచ్చు.",

        "Gynecology":
            "మహిళల పునరుత్పత్తి వ్యవస్థ మరియు స్త్రీ సంబంధిత సమస్యల కోసం ఈ విభాగాన్ని సంప్రదించవచ్చు."
    },


    "Hindi": {

        "General Medicine":
            "सामान्य, अस्पष्ट या विभिन्न प्रकार के लक्षणों के लिए इस विभाग से संपर्क किया जा सकता है।",

        "Cardiology":
            "हृदय और रक्त संचार से संबंधित लक्षणों के लिए इस विभाग से संपर्क किया जा सकता है।",

        "Pulmonology":
            "फेफड़ों और सांस से संबंधित लक्षणों के लिए इस विभाग से संपर्क किया जा सकता है।",

        "Neurology":
            "मस्तिष्क, नसों और तंत्रिका तंत्र से संबंधित लक्षणों के लिए इस विभाग से संपर्क किया जा सकता है।",

        "Dermatology":
            "त्वचा, बाल और नाखून से संबंधित समस्याओं के लिए इस विभाग से संपर्क किया जा सकता है।",

        "Gastroenterology":
            "पाचन तंत्र और पेट से संबंधित समस्याओं के लिए इस विभाग से संपर्क किया जा सकता है।",

        "ENT":
            "कान, नाक और गले से संबंधित समस्याओं के लिए इस विभाग से संपर्क किया जा सकता है।",

        "Orthopedics":
            "हड्डियों, जोड़ों, मांसपेशियों और चलने-फिरने से संबंधित समस्याओं के लिए इस विभाग से संपर्क किया जा सकता है।",

        "Ophthalmology":
            "आंखों और दृष्टि से संबंधित समस्याओं के लिए इस विभाग से संपर्क किया जा सकता है।",

        "Gynecology":
            "महिलाओं की प्रजनन प्रणाली और स्त्री रोग संबंधी समस्याओं के लिए इस विभाग से संपर्क किया जा सकता है।"
    }
}


# --------------------------------------------------
# GET DEPARTMENT DESCRIPTION
# --------------------------------------------------

def get_department_description(
    department,
    language="English"
):

    language_data = DEPARTMENT_DESCRIPTIONS.get(
        language,
        DEPARTMENT_DESCRIPTIONS["English"]
    )

    return language_data.get(
        department,
        "A healthcare professional can help determine the appropriate care."
    )


# --------------------------------------------------
# GET DEPARTMENT DISPLAY NAME
# --------------------------------------------------

DEPARTMENT_NAMES = {

    "English": {
        "General Medicine": "General Medicine",
        "Cardiology": "Cardiology",
        "Pulmonology": "Pulmonology",
        "Neurology": "Neurology",
        "Dermatology": "Dermatology",
        "Gastroenterology": "Gastroenterology",
        "ENT": "ENT",
        "Orthopedics": "Orthopedics",
        "Ophthalmology": "Ophthalmology",
        "Gynecology": "Gynecology"
    },

    "Telugu": {
        "General Medicine": "సాధారణ వైద్యం",
        "Cardiology": "కార్డియాలజీ",
        "Pulmonology": "పల్మోనాలజీ",
        "Neurology": "న్యూరాలజీ",
        "Dermatology": "డెర్మటాలజీ",
        "Gastroenterology": "గ్యాస్ట్రోఎంటరాలజీ",
        "ENT": "చెవి, ముక్కు మరియు గొంతు (ENT)",
        "Orthopedics": "ఆర్థోపెడిక్స్",
        "Ophthalmology": "కంటి వైద్యం",
        "Gynecology": "గైనకాలజీ"
    },

    "Hindi": {
        "General Medicine": "सामान्य चिकित्सा",
        "Cardiology": "हृदय रोग विभाग",
        "Pulmonology": "फेफड़े और श्वसन विभाग",
        "Neurology": "तंत्रिका विज्ञान विभाग",
        "Dermatology": "त्वचा रोग विभाग",
        "Gastroenterology": "पाचन तंत्र विभाग",
        "ENT": "कान, नाक और गला विभाग",
        "Orthopedics": "हड्डी और जोड़ विभाग",
        "Ophthalmology": "नेत्र विभाग",
        "Gynecology": "स्त्री रोग विभाग"
    }
}


def get_department_name(
    department,
    language="English"
):

    language_data = DEPARTMENT_NAMES.get(
        language,
        DEPARTMENT_NAMES["English"]
    )

    return language_data.get(
        department,
        department
    )