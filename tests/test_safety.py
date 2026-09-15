import sys
from pathlib import Path

# Add the app folder to Python path
APP_DIR = Path(__file__).parent.parent / "app"
sys.path.insert(0, str(APP_DIR))

from safety import check_red_flags


def test_chest_discomfort_is_red_flag():
    symptoms = ["Chest discomfort"]

    result = check_red_flags(symptoms)

    assert result is True


def test_shortness_of_breath_is_red_flag():
    symptoms = ["Shortness of breath"]

    result = check_red_flags(symptoms)

    assert result is True


def test_normal_symptoms_are_not_red_flags():
    symptoms = ["Headache", "Fatigue"]

    result = check_red_flags(symptoms)

    assert result is False


def test_empty_symptoms_are_not_red_flags():
    symptoms = []

    result = check_red_flags(symptoms)

    assert result is False


def test_multiple_symptoms_with_red_flag():
    symptoms = [
        "Headache",
        "Fever",
        "Chest discomfort"
    ]

    result = check_red_flags(symptoms)

    assert result is True