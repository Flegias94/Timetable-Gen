from models.entities import Room, Teacher, Course, StudentGroup, CourseSession


def load_mock_data():
    rooms = [
        Room(id="R101", capacity=40, features=["projector", "whiteboard"]),
        Room(id="Lab201", capacity=25, features=["lab", "projector", "whiteboard"]),
        Room(id="R301", capacity=50, features=["whiteboard"]),
    ]

    teachers = [
        Teacher(
            id="T1",
            name="Prof. Alice",
            available_slots=["Mon-08", "Mon-10", "Tue-08", "Tue-10", "Wed-08"],
            preferred_slots=["Mon-10"],
            courses=["C1", "C2"],
        ),
        Teacher(
            id="T2",
            name="Dr. Bob",
            available_slots=["Tue-10", "Tue-12", "Thu-08", "Thu-10"],
            preferred_slots=["Thu-10"],
            courses=["C3", "C1"],
        ),
    ]

    groups = [
        StudentGroup(
            id="G1",
            specialization="Computer Science",
            year=1,
            size=35,
            course_ids=["C1", "C3"],
        ),
        StudentGroup(
            id="G2",
            specialization="Software Engineering",
            year=1,
            size=22,
            course_ids=["C2"],
        ),
        # Subgroups of G1 for lab/seminary
        StudentGroup(
            id="G1Aa",
            parent_id="G1",
            specialization="Computer Science",
            year=1,
            size=17,
            course_ids=["C1", "C3"],
        ),
        StudentGroup(
            id="G1Ab",
            parent_id="G1",
            specialization="Computer Science",
            year=1,
            size=18,
            course_ids=["C1", "C3"],
        ),
    ]

    courses = [
        Course(
            id="C1",
            name="Intro to CS",
            semester=1,
            sessions=[
                CourseSession(
                    id="C1-lecture",
                    type="lecture",
                    teacher_id="T1",
                    group_ids=["G1"],
                    duration=2,
                    required_features=["projector"],
                ),
                CourseSession(
                    id="C1-lab-A",
                    type="lab",
                    teacher_id="T2",
                    group_ids=["G1Aa", "G1Ab"],
                    duration=2,
                    required_features=["lab"],
                ),
            ],
        ),
        Course(
            id="C2",
            name="Data Structures",
            semester=1,
            sessions=[
                CourseSession(
                    id="C2-lecture",
                    type="lecture",
                    teacher_id="T1",
                    group_ids=["G2"],
                    duration=2,
                    required_features=["whiteboard"],
                ),
                CourseSession(
                    id="C2-seminar",
                    type="seminary",
                    teacher_id="T1",
                    group_ids=["G2"],
                    duration=2,
                    required_features=["whiteboard"],
                ),
            ],
        ),
        Course(
            id="C3",
            name="Algorithms",
            semester=1,
            sessions=[
                CourseSession(
                    id="C3-lab",
                    type="lab",
                    teacher_id="T2",
                    group_ids=["G1Aa", "G1Ab"],
                    duration=2,
                    required_features=["lab"],
                )
            ],
        ),
    ]

    return rooms, teachers, courses, groups
