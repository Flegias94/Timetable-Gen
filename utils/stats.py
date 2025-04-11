from collections import defaultdict


def print_teacher_workload(schedule):
    workload = defaultdict(int)

    for session in schedule.values():
        teacher_id = session["teacher_id"]
        duration = 2  # fixed 2-hour blocks
        workload[teacher_id] += duration

    print("\n👨‍🏫 Weekly Teacher Workload:")
    for teacher_id, hours in workload.items():
        print(f" - {teacher_id}: {hours} hours")
