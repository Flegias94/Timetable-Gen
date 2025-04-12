from data.rooms_from_csv import load_rooms
from data.teachers_from_csv import load_teachers
from data.courses_from_csv import load_courses
from data.student_groups_legal_split import load_student_groups  # if defined

__all__ = ["load_rooms", "load_teachers", "load_courses", "load_student_groups"]


def load_all_data():
    rooms = load_rooms()
    teachers = load_teachers()
    courses = load_courses()
    student_groups = load_student_groups()
    return rooms, teachers, courses, student_groups
