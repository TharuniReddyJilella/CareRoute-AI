# ============================================================
# CareRoute AI - Department Triage
# ============================================================

from pathlib import Path
import joblib
import pandas as pd


# ============================================================
# PATHS
# ============================================================

APP_DIR = Path(__file__).parent
PROJECT_DIR = APP_DIR.parent

MODEL_PATH = (
    PROJECT_DIR
    / "models"
    / "department_classifier.pkl"
)


# ============================================================
# LOAD TRAINED MODEL
# ============================================================

MODEL_PACKAGE = joblib.load(MODEL_PATH)

MODEL = MODEL_PACKAGE["model"]
FEATURES = MODEL_PACKAGE["features"]


# ============================================================
# DIRECT SYMPTOM → DEPARTMENT MAPPING
# ============================================================

SYMPTOM_DEPARTMENT_MAP = {

    # --------------------------------------------------------
    # Cardiology
    # --------------------------------------------------------

    "Chest discomfort": "Cardiology",
    "Palpitations": "Cardiology",

    # --------------------------------------------------------
    # Pulmonology
    # --------------------------------------------------------

    "Cough": "Pulmonology",
    "Shortness of breath": "Pulmonology",

    # --------------------------------------------------------
    # Neurology
    # --------------------------------------------------------

    "Headache": "Neurology",
    "Dizziness": "Neurology",
    "Numbness": "Neurology",

    # --------------------------------------------------------
    # Dermatology
    # --------------------------------------------------------

    "Skin rash": "Dermatology",
    "Itching": "Dermatology",

    # --------------------------------------------------------
    # Gastroenterology
    # --------------------------------------------------------

    "Abdominal pain": "Gastroenterology",
    "Nausea": "Gastroenterology",
    "Vomiting": "Gastroenterology",
    "Diarrhea": "Gastroenterology",

    # --------------------------------------------------------
    # Orthopedics
    # --------------------------------------------------------

    "Joint pain": "Orthopedics",
    "Back pain": "Orthopedics",

    # --------------------------------------------------------
    # ENT
    # --------------------------------------------------------

    "Ear pain": "ENT",
    "Hearing difficulty": "ENT",
    "Sore throat": "ENT",
    "Nasal congestion": "ENT",

    # --------------------------------------------------------
    # Ophthalmology
    # --------------------------------------------------------

    "Eye pain": "Ophthalmology",
    "Blurred vision": "Ophthalmology",

    # --------------------------------------------------------
    # General Medicine
    # --------------------------------------------------------

    "Fever": "General Medicine",
    "Fatigue": "General Medicine",
}


# ============================================================
# DEPARTMENT PRIORITY
# ============================================================

DEPARTMENT_PRIORITY = [
    "Cardiology",
    "Neurology",
    "Pulmonology",
    "Ophthalmology",
    "Gastroenterology",
    "Orthopedics",
    "Dermatology",
    "ENT",
    "General Medicine",
]


# ============================================================
# RULE-BASED PREDICTION
# ============================================================

def rule_based_prediction(symptoms):
    """
    Predicts a department using explicit symptom-to-department
    mappings.

    Multiple symptoms are handled using weighted voting.
    """

    scores = {}

    for symptom in symptoms:

        department = SYMPTOM_DEPARTMENT_MAP.get(
            symptom
        )

        if department is not None:

            scores[department] = (
                scores.get(department, 0) + 1
            )

    if not scores:
        return None

    # --------------------------------------------------------
    # Find highest score
    # --------------------------------------------------------

    max_score = max(
        scores.values()
    )

    candidates = [
        department
        for department, score in scores.items()
        if score == max_score
    ]

    # --------------------------------------------------------
    # Resolve ties using department priority
    # --------------------------------------------------------

    for department in DEPARTMENT_PRIORITY:

        if department in candidates:
            return department

    return candidates[0]


# ============================================================
# ML PREDICTION
# ============================================================

def ml_prediction(symptoms):
    """
    Uses the trained CareRoute AI classification model.

    The model expects symptom indicators matching the training
    feature columns.
    """

    input_data = {
        feature: 0
        for feature in FEATURES
    }

    for symptom in symptoms:

        if symptom in input_data:
            input_data[symptom] = 1

    X = pd.DataFrame(
        [input_data],
        columns=FEATURES
    )

    prediction = MODEL.predict(X)

    return prediction[0]


# ============================================================
# FINAL DEPARTMENT PREDICTION
# ============================================================

def predict_department(symptoms):
    """
    Hybrid department prediction.

    1. Uses explicit symptom routing for known symptoms.
    2. Uses the trained ML model as a fallback.
    3. Falls back to General Medicine if nothing is available.

    This is a department-navigation system and does not
    diagnose diseases.
    """

    if not symptoms:
        return "General Medicine"

    # --------------------------------------------------------
    # Clean symptoms
    # --------------------------------------------------------

    cleaned_symptoms = [
        symptom.strip()
        for symptom in symptoms
        if symptom and symptom.strip()
    ]

    if not cleaned_symptoms:
        return "General Medicine"

    # --------------------------------------------------------
    # Rule-based routing
    # --------------------------------------------------------

    rule_department = rule_based_prediction(
        cleaned_symptoms
    )

    if rule_department is not None:
        return rule_department

    # --------------------------------------------------------
    # ML fallback
    # --------------------------------------------------------

    try:

        ml_department = ml_prediction(
            cleaned_symptoms
        )

        if ml_department:
            return ml_department

    except Exception:
        pass

    # --------------------------------------------------------
    # Final fallback
    # --------------------------------------------------------

    return "General Medicine"