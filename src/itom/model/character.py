from dataclasses import dataclass
from enum import Enum
from typing import Optional, Tuple

from itom.model.misc_models import InventoryItem, Note


class ExperienceLevel(str, Enum):
    """
    Inherits from str to allow to be serialized into JSON in form of
    the string representation.
    """

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
    advantages: Optional[list[str]] = None
    disadvantages: Optional[list[str]] = None
    possessions: Optional[list[InventoryItem]] = None
    armor_items: Optional[list] = None
    weapons: Optional[list] = None
    notes: Optional[list[Note]] = None
    experience_level: ExperienceLevel = ExperienceLevel.NOVICE
    arcana: Optional[list] = None

    @property
    def armor(self) -> int:
        if self.armor_items:
            return sum(
                armor_item["protection_value"] for armor_item in self.armor_items
            )
        else:
            return 0

    def repr_json(self) -> dict:
        return dict(
            __type__=Character.__name__,
            name=self.name,
            strength=self.strength,
            dexterity=self.dexterity,
            willpower=self.willpower,
            hit_points=self.hit_points,
            purse=self.purse,
            critical_damage=self.critical_damage,
            armor=self.armor,
            advantages=self.advantages,
            disadvantages=self.disadvantages,
            possessions=self.possessions,
            armor_items=self.armor_items,
            weapons=self.weapons,
            notes=self.notes,
            experience_level=self.experience_level,
            arcana=self.arcana,
            enterprises=self.enterprises,
        )
