from dataclasses import dataclass
from enum import Enum
from typing import Optional, Tuple


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
    advantages: Optional[list] = None
    disadvantages: Optional[list] = None
    possessions: Optional[list] = None
    weapons: Optional[list] = None
    notes: Optional[list] = None
    experience_level: ExperienceLevel = ExperienceLevel.NOVICE
    arcana: Optional[list] = None
    enterprises: Optional[list] = None
