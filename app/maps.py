# CareRoute AI - Google Maps Integration

from urllib.parse import quote_plus


DEPARTMENT_SEARCH_TERMS = {
    "General Medicine": "general medicine hospital",
    "Cardiology": "cardiology hospital",
    "Pulmonology": "pulmonology hospital",
    "Neurology": "neurology hospital",
    "Dermatology": "dermatology hospital",
    "Gastroenterology": "gastroenterology hospital",
    "ENT": "ENT hospital",
    "Orthopedics": "orthopedic hospital",
    "Ophthalmology": "eye hospital",
    "Gynecology": "gynecology hospital",
}


def get_hospital_search_term(department):
    return DEPARTMENT_SEARCH_TERMS.get(
        department,
        "hospital"
    )


def get_nearby_hospitals_url(department):
    search_term = get_hospital_search_term(department)

    query = f"{search_term} near me"

    return (
        "https://www.google.com/maps/search/?api=1&query="
        + quote_plus(query)
    )


def get_emergency_hospital_url():
    query = "emergency hospital near me"

    return (
        "https://www.google.com/maps/search/?api=1&query="
        + quote_plus(query)
    )


def get_navigation_url(destination):
    destination_encoded = quote_plus(destination)

    return (
        "https://www.google.com/maps/dir/?api=1"
        f"&destination={destination_encoded}"
        "&travelmode=driving"
        "&dir_action=navigate"
    )