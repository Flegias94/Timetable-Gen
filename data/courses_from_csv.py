from models.entities import Course, CourseSession


def load_courses():

    courses = [
        Course(
            id="AF1_Management",
            name="Management",
            semester=2,
            sessions=[
                CourseSession(
                    id="AF1_Management-sg1",
                    type="seminary",
                    teacher_id="simona_buta",
                    group_ids=["AF1sg1"],
                    duration=2,
                    required_features=["whiteboard"],
                    preferred_features=[],
                ),
                CourseSession(
                    id="AF1_Management-sg2",
                    type="seminary",
                    teacher_id="simona_buta",
                    group_ids=["AF1sg2"],
                    duration=2,
                    required_features=["whiteboard"],
                    preferred_features=[],
                ),
                CourseSession(
                    id="AF1_Management-sg3",
                    type="seminary",
                    teacher_id="simona_buta",
                    group_ids=["AF1sg3"],
                    duration=2,
                    required_features=["whiteboard"],
                    preferred_features=[],
                ),
                CourseSession(
                    id="AF1_Management-sg4",
                    type="seminary",
                    teacher_id="prof_titular_1",
                    group_ids=["AF1sg4"],
                    duration=2,
                    required_features=["whiteboard"],
                    preferred_features=[],
                ),
                CourseSession(
                    id="AF1_Management-sg5",
                    type="seminary",
                    teacher_id="prof_titular_1",
                    group_ids=["AF1sg5"],
                    duration=2,
                    required_features=["whiteboard"],
                    preferred_features=[],
                ),
                CourseSession(
                    id="AF1_Management-sg6",
                    type="seminary",
                    teacher_id="prof_titular_1",
                    group_ids=["AF1sg6"],
                    duration=2,
                    required_features=["whiteboard"],
                    preferred_features=[],
                ),
            ],
        ),
        # Add more Course(...) definitions here as needed
    ]
    return courses
