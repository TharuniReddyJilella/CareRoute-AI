# ============================================================
# CareRoute AI - Safety / Emergency Detection
# ============================================================

RED_FLAG_ALWAYS = {
    "loss of consciousness",
    "fainting",
    "difficulty speaking",
    "severe bleeding",
    "coughing blood",
    "vomiting blood",
    "severe allergic reaction",
    "severe eye injury",
}

SEVERE_ONLY_SYMPTOMS = {
    "chest discomfort",
    "shortness of breath",
}


def check_red_flags(selected_symptoms, severity="Moderate"):
    """
    Checks whether the selected symptoms require urgent attention.

    Generic symptoms such as chest discomfort and shortness of breath
    are NOT automatically treated as emergencies. They become urgent
    only when the patient reports severe symptoms.

    This function is a safety layer, not a disease diagnosis.
    """

    normalized = {
        symptom.strip().lower()
        for symptom in selected_symptoms
    }

    # --------------------------------------------------------
    # Always-urgent symptoms
    # --------------------------------------------------------

    if normalized.intersection(RED_FLAG_ALWAYS):
        return True

    # --------------------------------------------------------
    # Symptoms that become urgent when severe
    # --------------------------------------------------------

    if severity.strip().lower() == "severe":
        if normalized.intersection(SEVERE_ONLY_SYMPTOMS):
            return True

    return False


def get_safety_message():
    """
    General emergency guidance.
    """

    return (
        "Some of the symptoms you selected may require "
        "urgent medical attention. Please seek immediate "
        "medical care or contact your local emergency service."
    )