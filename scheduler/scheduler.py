from collections import defaultdict
from models.entities import Room, Teacher, Course, StudentGroup, CourseSession
from scheduler.timeslots import generate_all_timeslots
from utils.group_merging import get_mergeable_subgroups


class Scheduler:
    def __init__(self, rooms, teachers, courses, student_groups, debug_mode=False):
        self.debug_mode = debug_mode
        self.rooms = rooms
        self.teachers = teachers
        self.courses = courses
        self.student_groups = student_groups
        self.timeslots = generate_all_timeslots()
        self.schedule = {}  # session_id -> dict with room, timeslot, etc.
        self.unassigned = []
        self.group_day_slots = defaultdict(
            lambda: defaultdict(list)
        )  # group_id -> day -> [hours]

    def assign_courses(self):
        for course in self.courses:
            for session in course.sessions:
                assigned = False

                unassigned_groups = [
                    g for g in self.student_groups if g.id in session.group_ids
                ]

                sorted_rooms = sorted(
                    self.rooms,
                    key=lambda room: self.compute_room_score(room, session),
                    reverse=True,
                )

                for room in sorted_rooms:
                    valid_combos = get_mergeable_subgroups(
                        unassigned_groups, room.capacity
                    )
                    valid_combos.sort(
                        key=lambda combo: sum(g.size for g in combo), reverse=True
                    )

                    scored_timeslots = sorted(
                        self.timeslots,
                        key=lambda ts: (
                            self.compute_timeslot_score(session, ts)
                            + self.compute_group_day_score(
                                [g.id for g in unassigned_groups], ts
                            )
                        ),
                        reverse=True,
                    )

                    for timeslot in scored_timeslots:
                        for group_combo in valid_combos:
                            if self.is_valid_assignment(
                                session, room, timeslot, group_combo
                            ):
                                self.schedule[session.id] = {
                                    "room": room.id,
                                    "timeslot": timeslot,
                                    "group_ids": [g.id for g in group_combo],
                                    "teacher_id": session.teacher_id,
                                    "session_type": session.type,
                                }
                                self._register_group_timeslot(group_combo, timeslot)
                                assigned = True
                                break
                        if assigned:
                            break
                    if assigned:
                        break

                if not assigned:
                    self.unassigned.append(session.id)

        # Fallback scheduling
        if self.unassigned:
            print("\n🔁 Trying fallback scheduling for unassigned sessions...")
            remaining = self.unassigned.copy()
            self.unassigned.clear()

            for session_id in remaining:
                session = next(
                    (s for c in self.courses for s in c.sessions if s.id == session_id),
                    None,
                )
                if not session:
                    continue

                unassigned_groups = [
                    g for g in self.student_groups if g.id in session.group_ids
                ]

                for room in self.rooms:
                    valid_combos = get_mergeable_subgroups(
                        unassigned_groups, room.capacity
                    )
                    valid_combos.sort(
                        key=lambda combo: sum(g.size for g in combo), reverse=True
                    )

                    scored_timeslots = sorted(
                        self.timeslots,
                        key=lambda ts: (
                            self.compute_timeslot_score(session, ts)
                            + self.compute_group_day_score(
                                [g.id for g in unassigned_groups], ts
                            )
                        ),
                        reverse=True,
                    )

                    for timeslot in scored_timeslots:
                        for group_combo in valid_combos:
                            if self.is_valid_assignment(
                                session, room, timeslot, group_combo
                            ):
                                self.schedule[session.id] = {
                                    "room": room.id,
                                    "timeslot": timeslot,
                                    "group_ids": [g.id for g in group_combo],
                                    "teacher_id": session.teacher_id,
                                    "session_type": session.type,
                                    "fallback_used": True,
                                }
                                self._register_group_timeslot(group_combo, timeslot)
                                print(
                                    f"✅ Fallback scheduled: {session.id} at {room.id} - {timeslot}"
                                )
                                break
                        else:
                            continue
                        break
                    else:
                        continue
                    break

                if session.id not in self.schedule:
                    self.unassigned.append(session.id)

        return self.schedule

    def compute_room_score(self, room: Room, session: CourseSession) -> int:
        return sum(
            1 for feature in session.preferred_features if feature in room.features
        )

    def compute_timeslot_score(self, session: CourseSession, timeslot: str) -> int:
        _, hour = timeslot.split("-")
        hour = int(hour)
        is_lab_or_seminar = session.type in ["lab", "seminary"]

        if is_lab_or_seminar:
            if hour == 8:
                return 0
            elif 10 <= hour < 16:
                return 5
            elif hour == 16:
                return 3
            else:
                return 1
        else:
            if hour == 8:
                return 2
            elif 10 <= hour < 16:
                return 3
            elif hour == 16:
                return 2
            else:
                return 1

    def compute_group_day_score(self, group_ids, timeslot: str) -> int:
        day, hour = timeslot.split("-")
        hour = int(hour)
        score = 0

        for gid in group_ids:
            times = self.group_day_slots[gid][day]
            if not times:
                score += 2  # filling a new day is okay
            elif hour in times:
                score += 3  # perfect slot
            elif any(abs(hour - t) == 2 for t in times):
                score += 2  # adjacent slot
            elif any(abs(hour - t) >= 4 for t in times):
                score -= 1  # big gap penalty
            else:
                score += 1  # mild benefit

        return score

    def _register_group_timeslot(self, group_combo, timeslot: str):
        day, hour = timeslot.split("-")
        hour = int(hour)
        for g in group_combo:
            self.group_day_slots[g.id][day].append(hour)

    def is_valid_assignment(self, session, room, timeslot, group_combo):
        teacher = next((t for t in self.teachers if t.id == session.teacher_id), None)
        group_ids = [g.id for g in group_combo]

        if not all(feature in room.features for feature in session.required_features):
            if self.debug_mode:
                print(f"❌ Room {room.id} missing required features for {session.id}")
            return False

        total_size = sum(g.size for g in group_combo)
        if total_size > room.capacity:
            if self.debug_mode:
                print(
                    f"❌ Room {room.id} too small for {session.id} (needs {total_size})"
                )
            return False

        if teacher is None or timeslot not in teacher.available_slots:
            if self.debug_mode:
                print(
                    f"❌ Teacher {session.teacher_id} not available at {timeslot} for {session.id}"
                )
            return False

        for assignment in self.schedule.values():
            if assignment["timeslot"] == timeslot:
                if assignment["room"] == room.id:
                    if self.debug_mode:
                        print(f"❌ Room {room.id} already booked at {timeslot}")
                    return False
                if assignment["teacher_id"] == session.teacher_id:
                    if self.debug_mode:
                        print(
                            f"❌ Teacher {session.teacher_id} already teaching at {timeslot}"
                        )
                    return False
                if set(assignment["group_ids"]) & set(group_ids):
                    if self.debug_mode:
                        print(
                            f"❌ Group conflict at {timeslot} for {session.id}: {group_ids}"
                        )
                    return False

        return True
