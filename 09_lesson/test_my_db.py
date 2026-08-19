from config import Config
from StudentTable import StudentTable

db = StudentTable(Config.DATABASE_URL)


def test_add_student_by_id():
    max_id = db.get_max_id()
    student_new = db.add_new_student_by_id(max_id)

    first_maximum_id = db.first_maximum_id()[0][0]
    assert student_new[0][0] == first_maximum_id

    db.delete_student_by_id(first_maximum_id)


def test_update_student_by_id_level(levels):
    count_before = db.get_count_student().scalar()

    max_id = db.get_max_id()
    new_max_id = db.add_new_student_by_id(max_id)[0][0]
    for level in levels:
        db.update_student_by_id(new_max_id, level=level)
        row = db.get_student_by_id(new_max_id)
        assert row["level"] == level

    db.delete_student_by_id(new_max_id)

    count_after = db.get_count_student().scalar()
    assert count_before == count_after


def test_update_student_by_id_education(educations_form):
    count_before = db.get_count_student().scalar()

    max_id = db.get_max_id()
    new_max_id = db.add_new_student_by_id(max_id)[0][0]
    for education_form in educations_form:
        db.update_student_by_id(new_max_id, education_form=education_form)
        row = db.get_student_by_id(new_max_id)
        assert row["education_form"] == education_form

    db.delete_student_by_id(new_max_id)

    count_after = db.get_count_student().scalar()
    assert count_before == count_after


def test_update_student_by_id(subjects_id):
    count_before = db.get_count_student().scalar()

    max_id = db.get_max_id()
    new_max_id = db.add_new_student_by_id(max_id)[0][0]
    for subject_id in subjects_id:
        db.update_student_by_id(new_max_id, subject_id=subject_id)
        row = db.get_student_by_id(new_max_id)
        assert row["subject_id"] == subject_id

    db.delete_student_by_id(new_max_id)

    count_after = db.get_count_student().scalar()
    assert count_before == count_after


def test_delete_student_by_id():
    count_before = db.get_count_student().scalar()

    max_id = db.get_max_id()
    new_max_id = db.add_new_student_by_id(max_id)[0][0]
    db.delete_student_by_id(new_max_id)

    count_after = db.get_count_student().scalar()

    assert count_before == count_after
