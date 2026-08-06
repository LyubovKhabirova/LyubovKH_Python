# Требования:
# Напишите минимум три теста: по одному на добавление, изменение и удаление любой сущности (например, предмет или студенты).
# Тесты должны использовать библиотеку pytest.
# Тесты должны использовать библиотеку SQLAlchemy.
# Дополнительно поставьте библиотеку psycopg2-binary.
# Тесты должны удалять за собой созданные данные через обращение к БД.
# Тесты должны быть стабильны:
# их не нужно редактировать перед каждым запуском;
# повторный запуск теста приводит к тому же статусу.

# Работа будет оценена по следующим критериям
# Созданы ветка lesson9 и папка 09_lesson.
# Pull Request создан из ветки lesson9 в master/main, ссылка приложена в формате https://github.com/.../pull/N.
# Отчет линтера не содержит ошибок (errors) и предупреждений (warnings).
# Все тестовые файлы (test_*.py) и функции (test_*) названы корректно. Команда pytest 09_lesson находит и запускает все тесты.
# Все тесты написаны с использованием pytest.
# Для выполнения всех операций с БД используется библиотека SQLAlchemy (ORM или Core).
# Тесты можно запускать в любом порядке многократно без падений. Каждый тест удаляет созданные им данные через обращение к БД (через SQLAlchemy) после своего выполнения.
# Реализован тест, который добавляет новую сущность в БД и проверяет успешность операции (напр., через проверку наличия сущности с определенными данными после добавления).
# Реализован тест, который изменяет существующую сущность в БД (созданную в рамках теста) и проверяет успешность операции (напр., через проверку обновленных данных).
# Реализован тест, который удаляет существующую сущность из БД (созданную в рамках теста) и проверяет успешность операции (напр., через проверку отсутствия сущности после удаления).

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
    max_id = db.get_max_id()
    for level in levels:
        db.update_student_by_id(max_id, level=level)
        row = db.get_student_by_id(max_id)
        assert row["level"] == level

def test_update_student_by_id_education(educations_form):
    max_id = db.get_max_id()
    for education_form in educations_form:
        db.update_student_by_id(max_id, education_form=education_form)
        row = db.get_student_by_id(max_id)
        assert row["education_form"] == education_form

def test_update_student_by_id(subjects_id):
    max_id = db.get_max_id()
    for subject_id in subjects_id:
        db.update_student_by_id(max_id, subject_id=subject_id)
        row = db.get_student_by_id(max_id)
        assert row["subject_id"] == subject_id

def test_delete_student_by_id():
    count_before = db.get_count_student().scalar()

    max_id = db.get_max_id()
    db.delete_student_by_id(max_id)

    count_after = db.get_count_student().scalar()

    assert count_before > count_after
