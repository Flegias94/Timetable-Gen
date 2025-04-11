# scheduler/timeslots.py

DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri"]
hours = [f"{h:02}" for h in range(8, 20, 2)]  # 2-hour chunks


def generate_all_timeslots() -> list[str]:
    return [f"{day}-{hour}" for day in DAYS for hour in hours]
