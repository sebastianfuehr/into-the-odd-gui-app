from dataclasses import dataclass
from enum import Enum
from typing import Tuple


class ExperienceLevel(Enum):
    NOVICE = "Novice"
    PROFESSIONAL = "Professional"
    EXPERT = "Expert"
    VETERAN = "Veteran"
    MASTER = "Master"
    BEYOND = "Beyond"


@dataclass
class Character:
    name: str
    strength: Tuple[int, int]
    dexterity: Tuple[int, int]
    willpower: Tuple[int, int]
    hit_points: Tuple[int, int]
    purse: Tuple[int, int, int]
    critical_damage: bool = False
    armor: int = 0
    advantages: list = None
    disadvantages: list = None
    possessions: list = None
    weapons: list = None
    notes: str = None
    experience_level: ExperienceLevel = ExperienceLevel.NOVICE
    arcana: list = None
    enterprises: list = None
