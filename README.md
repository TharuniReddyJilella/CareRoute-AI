# 🏥 CareRoute AI

### Smart Healthcare Department Triage System

CareRoute AI is an AI-powered healthcare navigation system that helps users identify the appropriate medical department based on their reported symptoms.

The system provides a safe triage workflow that combines symptom-based machine learning, emergency red-flag detection, multilingual voice input, department recommendations, and Google Maps hospital search.

> ⚠️ **Disclaimer:** CareRoute AI is a healthcare navigation and triage-support system. It does not diagnose diseases and is not a replacement for professional medical advice.

---

## 🎯 Problem Statement

Patients often feel confused about which medical specialist or hospital department they should consult for non-emergency symptoms.

This uncertainty can result in:

- Delayed medical consultation
- Visiting an inappropriate department
- Difficulty understanding which specialist to approach
- Additional stress for patients and caregivers

CareRoute AI addresses this problem by providing a simple symptom-based department recommendation workflow.

---

## 💡 Proposed Solution

CareRoute AI allows users to:

1. Enter basic patient information.
2. Describe symptoms using voice input or manual selection.
3. Detect potentially urgent symptoms using predefined safety rules.
4. Analyze non-emergency symptoms using a machine-learning classifier.
5. Recommend an appropriate healthcare department.
6. Search for nearby hospitals through Google Maps.
7. View completed assessments during the current application session.
8. Use the system in English, Telugu, or Hindi.

---

## 🚀 Key Features

### 🎤 Voice-Based Symptom Input

Users can describe their symptoms using their voice.

Supported languages:

- 🇬🇧 English
- 🇮🇳 తెలుగు (Telugu)
- 🇮🇳 हिन्दी (Hindi)

The application converts the recorded speech into text and identifies supported symptoms from the input.

---

### ☑️ Manual Symptom Selection

Users can also select symptoms manually from a predefined list.

Example symptoms include:

- Headache
- Fever
- Cough
- Shortness of breath
- Chest discomfort
- Palpitations
- Abdominal pain
- Nausea
- Vomiting
- Diarrhea
- Joint pain
- Back pain
- Skin rash
- Itching
- Ear pain
- Hearing difficulty
- Sore throat
- Nasal congestion
- Eye pain
- Blurred vision
- Dizziness
- Numbness
- Fatigue

---

### 🚨 Emergency Red-Flag Detection

Before generating a normal department recommendation, CareRoute AI checks for predefined potentially urgent symptoms.

Examples include:

- Chest discomfort
- Severe chest pain
- Difficulty breathing
- Loss of consciousness
- Fainting
- Sudden weakness
- Sudden numbness
- Difficulty speaking
- Severe bleeding
- Coughing blood
- Vomiting blood
- Severe allergic reaction
- Severe eye injury

If a red flag is detected, the system provides urgent-care guidance instead of treating the case as a routine department recommendation.

---

### 🧠 Machine Learning Department Recommendation

For non-emergency cases, CareRoute AI uses a supervised machine-learning classification approach to recommend an appropriate healthcare department.

The system evaluates:

- Patient symptoms
- Symptom combinations
- Learned relationships between symptoms and healthcare specialties

The model predicts the most appropriate department represented in the training data.

---

### 🏥 Hospital Search

After receiving a department recommendation, users can search for relevant hospitals using Google Maps.

Examples:

```text
Cardiology hospital near me
Neurology hospital near me
Dermatology hospital near me
Orthopedic hospital near me
```

The application generates department-specific Google Maps search queries.

> The Google Maps feature provides a search/navigation link. It does not independently verify hospital availability, services, distance, or appointment availability.

---

### 📋 Patient History

CareRoute AI provides a third page for completed assessments.

The history can display:

- Patient number
- Patient name
- Age
- Selected symptoms
- Duration
- Severity
- Recommended department
- Assessment date and time
- Emergency status

Users can:

- Start a new patient assessment
- View previous assessments
- Clear the session history

> Patient history is stored only in the current Streamlit session and is not intended to function as a permanent medical record.

---

### 🌐 Multilingual Interface

The application supports:

- English
- తెలుగు
- हिन्दी

The selected language is used across the application's user interface and healthcare guidance.

---

## 🖥️ Application Workflow

```text
                    ┌──────────────────┐
                    │   Welcome Page   │
                    │  Select Language │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Patient Details  │
                    │ Name + Age       │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Symptom Input    │
                    │ Voice / Manual   │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Safety Screening │
                    │ Red-Flag Check   │
                    └────────┬─────────┘
                             │
                ┌────────────┴────────────┐
                │                         │
          Red Flag Detected        No Red Flag
                │                         │
                ▼                         ▼
       ┌─────────────────┐      ┌──────────────────┐
       │ Urgent Medical  │      │ ML Classification│
       │ Care Guidance   │      └────────┬─────────┘
       └─────────────────┘               │
                                         ▼
                              ┌──────────────────┐
                              │ Department       │
                              │ Recommendation   │
                              └────────┬─────────┘
                                       │
                                       ▼
                              ┌──────────────────┐
                              │ Google Maps      │
                              │ Hospital Search  │
                              └────────┬─────────┘
                                       │
                                       ▼
                              ┌──────────────────┐
                              │ Patient History  │
                              └──────────────────┘
```

---

## 🏗️ Project Architecture

```text
CareRoute-AI/
│
├── app/
│   ├── app.py
│   ├── maps.py
│   ├── questions.py
│   ├── recommendations.py
│   ├── safety.py
│   └── triage.py
│
├── assets/
│   ├── care_route_icon.png
│   ├── care_route_logo.png
│   ├── department.png
│   ├── healthcare_background.png
│   ├── location.png
│   ├── microphone.png
│   └── tagline.png
│
├── data/
│   ├── department_dataset.csv
│   ├── nodes_condition.csv
│   ├── nodes_speciality.csv
│   ├── nodes_symptom.csv
│   ├── raw_medical_data.csv
│   └── triples.jsonl
│
├── models/
│   └── department_classifier.pkl
│
├── notebooks/
│   └── 01_data_exploration.ipynb
│
├── tests/
│   ├── test_safety.py
│   └── test_triage.py
│
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

---

# 🧠 Machine Learning

CareRoute AI uses a supervised machine-learning classification approach to recommend an appropriate healthcare department.

## Dataset

The project uses healthcare relationship data from **BODHI-S by Eka Care**.

The dataset represents relationships between:

```text
Symptoms
    ↓
Conditions
    ↓
Medical Specialties
```

The dataset contains:

- 779 condition nodes
- 4,037 symptom nodes/variants
- 590 symptom root concepts
- 39 specialty nodes
- 13,204 relationships

Important relationship types include:

- `PRESENT_IN`
- `TREATED_BY`
- `IS_INFLUENCED_BY`
- `RELATED_TO`
- `HAS_PREREQUISITE`

---

## 📊 Data Exploration

Exploratory Data Analysis was performed using the BODHI-S relationship data.

The analysis examined:

- Relationship distribution
- Unique symptoms
- Unique conditions
- Medical specialties
- Symptom-condition relationships
- Condition-specialty relationships
- Department mapping

The processed dataset used for classification contains:

- 553 conditions
- 2,559 symptom features
- 8 learnable department classes

---

## 🤖 Models Evaluated

The following classification models were evaluated:

### 1. Logistic Regression

A linear classification algorithm used as a baseline model.

### 2. Linear Support Vector Classifier

A linear SVM-based classifier suitable for high-dimensional symptom features.

### 3. Random Forest

An ensemble learning algorithm based on multiple decision trees.

Models were compared using classification performance metrics, including:

- Accuracy
- Precision
- Recall
- F1 Score

The best-performing model was selected for deployment.

The trained model is stored as:

```text
models/
└── department_classifier.pkl
```

---

## 🔄 Department Mapping

The source dataset contains multiple medical specialties.

For the application, relevant specialties are mapped into user-friendly healthcare departments such as:

- General Medicine
- Cardiology
- Neurology
- Pulmonology
- Dermatology
- Gastroenterology
- ENT
- Orthopedics
- Ophthalmology
- Gynecology

The currently trained classifier represents the department classes available in the processed training data.

---

# 🛡️ Safety Design

Healthcare applications require additional safeguards.

CareRoute AI follows a **safety-first triage approach**:

```text
User Symptoms
      │
      ▼
Red-Flag Screening
      │
      ├── Red Flag → Urgent Medical Care Guidance
      │
      └── No Red Flag
              │
              ▼
       ML Recommendation
              │
              ▼
     Healthcare Department
```

The machine-learning model is not allowed to override predefined emergency safety rules.

The system is designed for **department navigation**, not disease diagnosis.

---

# 🎤 Voice Processing

The voice workflow uses speech recognition to convert recorded audio into text.

Language codes used by the application include:

```text
English → en-IN
Telugu  → te-IN
Hindi   → hi-IN
```

The application then extracts supported symptom terms from the recognized speech.

For multilingual spoken responses, the application uses text-to-speech support for:

```text
English → en
Telugu  → te
Hindi   → hi
```

---

# 🗺️ Google Maps Integration

CareRoute AI generates Google Maps search URLs based on the recommended department.

Example:

```text
Recommended Department
        ↓
Cardiology
        ↓
Cardiology hospital near me
        ↓
Google Maps
```

The system does not maintain its own hospital database.

Google Maps is used as an external search/navigation service.

---

# 🧪 Testing

The project includes automated tests using `pytest`.

Testing covers important components such as:

### Safety Testing

- Red-flag symptom detection
- Multiple symptom combinations
- Empty symptom input
- Emergency symptom handling

### Triage Testing

- Department prediction
- Single-symptom predictions
- Multiple-symptom predictions
- Model-based recommendation logic

Run all tests using:

```bash
pytest
```

Expected result:

```text
10 passed
```

Warnings related to the saved scikit-learn model version may appear depending on the installed scikit-learn version.

---

# ⚙️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data processing |
| NumPy | Numerical operations |
| Scikit-learn | Machine learning |
| Matplotlib | Data visualization |
| Seaborn | Exploratory data analysis |
| Streamlit | Web application |
| Joblib | Model serialization |
| SpeechRecognition | Voice-to-text processing |
| gTTS | Text-to-speech |
| Pytest | Automated testing |
| Google Maps | Hospital search/navigation |
| Git & GitHub | Version control |

---

# 📦 Installation

## 1. Clone the repository

```bash
git clone https://github.com/TharuniReddyJilella/CareRoute-AI.git
```

## 2. Open the project

```bash
cd CareRoute-AI
```

## 3. Create a virtual environment

### Windows

```bash
python -m venv venv
```

## 4. Activate the virtual environment

```bash
venv\Scripts\activate
```

## 5. Install dependencies

```bash
pip install -r requirements.txt
```

## 6. Run the application

```bash
streamlit run app/app.py
```

The application will open in your browser.

---

# 🧪 Running Tests

From the project root:

```bash
pytest
```

To run only safety tests:

```bash
pytest tests/test_safety.py
```

To run only triage tests:

```bash
pytest tests/test_triage.py
```

---

# 📁 Important Files

### `app/app.py`

Main Streamlit application containing:

- Welcome page
- Language selection
- Patient details
- Voice input
- Manual symptom selection
- Recommendation interface
- Patient history
- Application routing

### `app/triage.py`

Contains the machine-learning based triage and department prediction logic.

### `app/safety.py`

Contains emergency red-flag detection and safety messaging.

### `app/recommendations.py`

Contains multilingual department descriptions and department names.

### `app/maps.py`

Generates Google Maps hospital search and navigation URLs.

### `app/questions.py`

Contains symptom and triage-related question data.

### `models/department_classifier.pkl`

Serialized trained machine-learning model and its feature information.

### `notebooks/01_data_exploration.ipynb`

Contains exploratory data analysis and dataset investigation.

---

# 📌 Current Model Coverage

The current processed training data supports the following learnable department classes:

```text
General Medicine
Orthopedics
Dermatology
ENT
Neurology
Ophthalmology
Gastroenterology
Cardiology
```

Some additional departments are represented conceptually in the application's department mapping but are not currently represented as learnable classes in the processed training dataset.

This distinction is maintained to avoid overstating the model's current training coverage.

---

# 🔐 Privacy & Data Handling

CareRoute AI does not use a permanent patient database in the current implementation.

Patient history is stored in the Streamlit session while the application is running.

Therefore:

- History is not a permanent medical record.
- Restarting the application clears the session history.
- Users should not enter unnecessary sensitive personal information.
- The application should not be used as a replacement for a clinical information system.

---

# ⚠️ Limitations

The current prototype has several limitations:

- It is intended for healthcare navigation rather than diagnosis.
- Department recommendations depend on the available training data.
- The current ML model covers the department classes represented in the processed dataset.
- Voice recognition performance can vary with background noise, pronunciation, and audio quality.
- Google Maps search results are provided by an external service.
- Hospital availability and appointment information are not independently verified.
- Patient history is session-based and not persistent.
- The system has not been presented as a substitute for professional clinical judgment.

---

# 🚀 Future Enhancements

Potential future improvements include:

- 🏥 Real-time hospital availability
- 📅 Hospital appointment booking
- 👨‍⚕️ Doctor availability integration
- 🗣️ Improved multilingual conversational AI
- 🧠 Larger and more diverse training datasets
- 📱 Mobile application support
- 🔐 Secure persistent patient records with appropriate privacy controls
- 🏨 Hospital service and specialty verification
- 📍 Location-aware hospital recommendations
- 🔄 Continuous model improvement using validated healthcare data

---

# 📈 Project Impact

CareRoute AI aims to make healthcare navigation simpler by helping users understand:

```text
"What should I do next?"
```

instead of attempting to answer:

```text
"What disease do I have?"
```

The system focuses on guiding users toward an appropriate healthcare department while prioritizing emergency safety.

---

# 👩‍💻 Project Structure

```text
CareRoute AI
│
├── User Interface
│      └── Streamlit
│
├── Voice Processing
│      ├── Speech Recognition
│      └── gTTS
│
├── Safety Layer
│      └── Red-Flag Detection
│
├── Machine Learning
│      ├── Feature Processing
│      ├── Classification
│      └── Department Recommendation
│
├── Hospital Search
│      └── Google Maps
│
├── Patient History
│      └── Session-Based Storage
│
└── Testing
       └── Pytest
```

---

# 📚 Dataset & References

## BODHI-S — Eka Care

CareRoute AI uses healthcare relationship data from the BODHI-S dataset developed by Eka Care.

Dataset:

```text
https://huggingface.co/datasets/ekacare/BODHI-S
```

Project repository:

```text
https://github.com/eka-care/BODHI
```

The dataset is provided under the **CC BY-NC 4.0** license. Refer to the original dataset and project repository for complete licensing and attribution information.

---

# 📄 License

This project is intended for educational and research purposes.

The project code is distributed under the license included in the repository.

The healthcare dataset used by the project has its own licensing terms, which must be respected separately.

---

# 🙌 Acknowledgements

Special thanks to:

- **Eka Care** for the BODHI-S healthcare dataset.
- The open-source Python and machine-learning community.
- Streamlit for the application framework.
- scikit-learn for machine-learning tools.
- Google Maps for hospital search and navigation functionality.

---

# ⭐ Conclusion

**CareRoute AI** combines healthcare data, machine learning, safety rules, voice interaction, multilingual support, and hospital search into a single healthcare navigation platform.

The goal is simple:

> **Help patients reach the right healthcare department more confidently and safely.**