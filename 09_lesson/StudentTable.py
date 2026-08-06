from sqlalchemy import create_engine
from sqlalchemy.sql import text

class StudentTable:
    __scripts = {
        "count list": text("SELECT count (*) from student"),
        "get by id": text("SELECT * from student where user_id = :id_to_get"),
        "get max id": text("SELECT MAX(user_id) from student"),
        "get new id": text("SELECT MAX(user_id) + 1 FROM student"),
        "select by id": text(
            'INSERT into student ("user_id") '
            'values (:new_id) RETURNING user_id'),
        "first maximum id": text(
            "SELECT * from student order by user_id desc LIMIT 1"),
        "delete id": text("DELETE from student where user_id = :id_to_delete"),
        "updated text": text("UPDATE student "
                             "SET level = :level_to_updated, "
                             "education_form = :education_form_to_updated, "
                             "subject_id = :subject_id_to_updated "
                             "WHERE user_id = :id_to_updated "
                             "RETURNING level, education_form, subject_id")
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def get_count_student(self):
        return self.__db.execute(self.__scripts["count list"])

    def get_student_by_id(self, id):
        return self.__db.execute(
            self.__scripts["get by id"], id_to_get = id).mappings().fetchone()

    def get_max_id(self):
        return self.__db.execute(self.__scripts["get max id"]).scalar()

    def add_new_student_by_id(self, max_id):
        new_id = max_id + 1
        return self.__db.execute(
            self.__scripts["select by id"], new_id = new_id).fetchall()

    def first_maximum_id(self):
        return self.__db.execute(self.__scripts["first maximum id"]).fetchall()

    def update_student_by_id(self, id, level=None, education_form=None,
                             subject_id=None):
        updated_student = self.__db.execute(
            self.__scripts["updated text"],
            id_to_updated = id, level_to_updated = level,
            education_form_to_updated = education_form,
            subject_id_to_updated = subject_id)

        return updated_student.fetchone()

    def delete_student_by_id(self, id):
        return self.__db.execute(
            self.__scripts["delete id"], id_to_delete = id)
