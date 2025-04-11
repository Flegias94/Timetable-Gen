# models/entities.py

from dataclasses import dataclass, field
from typing import List, Optional
from typing import Literal


@dataclass
class Room:
    id: str
    capacity: int
    features: List[str]  # e.g. ["lab", "projector"]
    available_slots: Optional[List[str]] = None  # e.g. ["Mon-08", "Tue-10"]


@dataclass
class Teacher:
    id: str
    name: str
    available_slots: List[str]  # times they can teach
    preferred_slots: Optional[List[str]] = None
    courses: List[str] = field(default_factory=list)  # course IDs


@dataclass
class CourseSession:
    id: str  # "C101-lecture" or "C101-lab-A"
    type: Literal["lecture", "lab", "seminary"]
    teacher_id: str
    group_ids: List[str]
    duration: int = 2  # Default 2 hours
    required_features: List[str] = field(default_factory=list)
    preferred_features: List[str] = field(default_factory=list)  # Nice-to-have


@dataclass
class Course:
    id: str  # e.g., "C101"
    name: str
    semester: int
    sessions: List[CourseSession]  # Each course has multiple sessions


@dataclass
class StudentGroup:
    id: str
    specialization: str
    year: int
    size: int
    course_ids: List[str]
    parent_id: Optional[str] = None


@dataclass
class TimeSlot:
    day: str  # "Mon", "Tue", etc.
    hour: str  # "08", "10", ..., "18"

    def __str__(self):
        return f"{self.day}-{self.hour}"
