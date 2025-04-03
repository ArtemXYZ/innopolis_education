"""
    Модуль содержит все запросы.
"""

SQL_CREATE_TABLE = """
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        course_number INTEGER NOT NULL CHECK(course_number > 0),
        age INTEGER NOT NULL CHECK(age >= 16 AND age <= 100),
        enrollment_date TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
    )
"""

SQL_DROP_TABLE = """DROP TABLE IF EXISTS students"""

SQL_SELECT_STUDENTS = """SELECT * FROM students"""

SQL_SELECT_STUDENTS_BY_NAME = """
    SELECT 
        st.first_name,
        st.last_name,
        st.course_number,
        st.age,
        st.enrollment_date
    FROM 
        students AS st 
    WHERE 
        st.last_name = :last_name_value
"""

SQL_INSERT_ROW_STUDENTS = """
    INSERT INTO students ( 
        first_name,
        last_name,
        course_number,
        age
    ) 
    VALUES (
        :first_name_value,
        :last_name_value,
        :course_number_value,
        :age_value
    )
"""

SQL_DELETE_ROW_STUDENTS = """
    DELETE FROM students
    WHERE last_name = :last_name_value
"""

SQL_UPDATE_ROW_STUDENTS = """
    UPDATE students
    SET 
        course_number = :course_number_value
    WHERE last_name = :last_name_value
"""