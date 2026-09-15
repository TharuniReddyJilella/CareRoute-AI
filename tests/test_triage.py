import sys
from pathlib import Path

# Add the app folder to Python path
APP_DIR = Path(__file__).parent.parent / "app"
sys.path.insert(0, str(APP_DIR))

from triage import predict_department


VALID_DEPARTMENTS = {
    "General Medicine",
    "Cardiology",
    "Neurology",
    "Dermatology",
    "Gastroenterology",
    "ENT",
    "Orthopedics",
    "Ophthalmology",
}


def test_headache_prediction_returns_department():
    symptoms = ["Headache"]

    result = predict_department(symptoms)

    assert isinstance(result, str)
    assert result in VALID_DEPARTMENTS


def test_skin_rash_prediction_returns_department():
    symptoms = ["Skin rash"]

    result = predict_department(symptoms)

    assert isinstance(result, str)
    assert result in VALID_DEPARTMENTS


def test_joint_pain_prediction_returns_department():
    symptoms = ["Joint pain"]

    result = predict_department(symptoms)

    assert isinstance(result, str)
    assert result in VALID_DEPARTMENTS


def test_multiple_symptoms_return_department():
    symptoms = [
        "Headache",
        "Dizziness",
        "Fatigue"
    ]

    result = predict_department(symptoms)

    assert isinstance(result, str)
    assert result in VALID_DEPARTMENTS


def test_cough_prediction_returns_department():
    symptoms = ["Cough"]

    result = predict_department(symptoms)

    assert isinstance(result, str)
    assert result in VALID_DEPARTMENTS