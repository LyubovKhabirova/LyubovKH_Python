import pytest

LEVELS = [
    "Elementary", "Intermediate", "Advanced",
    "Upper-Intermediate", "Pre-Intermediate", "Beginner", None
]
EDUCATIONS_FORM = [
    "group", "personal", None
]
SUBJECTS_ID = [1, None]

@pytest.fixture
def levels():
    return LEVELS

@pytest.fixture
def educations_form():
    return EDUCATIONS_FORM

@pytest.fixture
def subjects_id():
    return SUBJECTS_ID

