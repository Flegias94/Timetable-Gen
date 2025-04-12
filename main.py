from scheduler.scheduler import Scheduler
from csv_loader import load_all_data
import csv
from models.entities import Course
from utils.stats import print_teacher_workload

rooms, teachers, courses, student_groups = load_all_data()
scheduler = Scheduler(rooms, teachers, courses, student_groups, debug_mode=True)
result = scheduler.assign_courses()

print("📅 Schedule:")
for session_id, session_data in result.items():
    room = session_data["room"]
    timeslot = session_data["timeslot"]
    group_ids = session_data["group_ids"]
    fallback = session_data.get("fallback_used", False)

    status_icon = "⚠️" if fallback else "✅"
    print(
        f"{status_icon} {session_id}: {room} at {timeslot} for {', '.join(group_ids)}"
    )

if scheduler.unassigned:
    print("\n❌ Could not schedule the following sessions:")
    for sid in scheduler.unassigned:
        print(f" - {sid}")


def export_schedule_to_csv(schedule, courses, filename="outputs/timetable.csv"):
    # Flatten sessions for lookup
    session_lookup = {}
    for course in courses:
        for session in course.sessions:
            session_lookup[session.id] = {
                "course_name": course.name,
                "session_type": session.type,
                "teacher_id": session.teacher_id,
            }

    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(
            [
                "Session ID",
                "Course Name",
                "Session Type",
                "Room",
                "Timeslot",
                "Teacher ID",
                "Group IDs",
                "Fallback Used",
            ]
        )

        for session_id, session_data in schedule.items():
            session_info = session_lookup.get(session_id, {})
            writer.writerow(
                [
                    session_id,
                    session_info.get("course_name", ""),
                    session_info.get("session_type", ""),
                    session_data["room"],
                    session_data["timeslot"],
                    session_data["teacher_id"],
                    ", ".join(session_data["group_ids"]),
                    "Yes" if session_data.get("fallback_used") else "No",
                ]
            )

    print(f"\n📁 Timetable exported to: {filename}")


export_schedule_to_csv(result, courses)
print_teacher_workload(result)
