from dataclasses import dataclass
from datetime import date, datetime
from enum import IntEnum, StrEnum
from typing import Optional, Tuple


class Die(IntEnum):
    D4 = 4
    D6 = 6
    D8 = 8
    D10 = 10
    D12 = 12
    D20 = 20


@dataclass
class Note:
    creation_date: datetime
    text: str

    def repr_json(self) -> dict:
        return dict(
            __type__=Note.__name__,
            creation_date=self.creation_date,
            text=self.text,
        )


@dataclass
class Item:
    name: str
    description: Optional[str] = None
    bulky: bool = False
    # A worth of None means the value of the item is unknown
    worth: Optional[Tuple[int, int, int]] = None
    image_file_path: Optional[str] = None

    def repr_json(self) -> dict:
        return dict(
            __type__=Item.__name__,
            name=self.name,
            description=self.description,
            bulky=self.bulky,
            worth=self.worth,
            image_file_path=self.image_file_path,
        )


@dataclass
class InventoryItem(Item):
    """An item which is in the possession of a character.

    A spearate class is introduced to prohibit other item types like
    Weapon or Armor to be stacked.

    Attributes
        amount: How many items the character has in their inventory.
    """

    amount: int = 1

    def repr_json(self) -> dict:
        parent_dict = super().repr_json()
        parent_dict["__type__"] = InventoryItem.__name__
        return dict(**parent_dict, amount=self.amount)


class WeaponType(StrEnum):
    CRUDE_WEAPON = "Crude Weapon"
    HAND_WEAPON = "Hand Weapon"
    FIELD_WEAPON = "Field Weapon"
    NOBLE_WEAPON = "Noble Weapon"
    HEAVY_GUN = "Heavy Gun"


@dataclass(kw_only=True)
class Weapon(Item):
    dmg_die: Die
    amt_dice: int = 1
    # A weapon type of None means the weapon type is unknown
    weapon_type: Optional[WeaponType] = None

    def repr_json(self) -> dict:
        parent_dict = super().repr_json()
        parent_dict["__type__"] = Weapon.__name__
        return {
            **parent_dict,
            **dict(
                dmg_die=self.dmg_die,
                amt_dice=self.amt_dice,
                weapon_type=self.weapon_type,
            ),
        }


class ArmorType(StrEnum):
    CRUDE_ARMOR = "Crude Armor"
    MODERN_ARMOR = "Modern Armor"
    SHIELD = "Shield"


@dataclass(kw_only=True)
class Armor(Item):
    protection_value: int
    # An armor type of None means the armor type is unknown
    armor_type: Optional[ArmorType] = None
    equipped: bool = True

    def repr_json(self) -> dict:
        parent_dict = super().repr_json()
        parent_dict["__type__"] = Armor.__name__
        return {
            **parent_dict,
            **dict(
                protection_value=self.protection_value,
                armor_type=self.armor_type,
                equipped=self.equipped,
            ),
        }


class ArcanmumType(StrEnum):
    STANDARD = "Standard"
    GREATER = "Greater"
    LEGENDARY = "Legendary"


@dataclass(kw_only=True)
class Arcanum(Item):
    idx_nbr: int
    arcanum_type: ArcanmumType

    def repr_json(self) -> dict:
        parent_dict = super().repr_json()
        parent_dict["__type__"] = Arcanum.__name__
        return {
            **parent_dict,
            **dict(idx_nbr=self.idx_nbr, arcanum_type=self.arcanum_type),
        }


@dataclass
class Enterprise:
    creation_date: datetime
    name: str
    enterprise_type: str
    owners: list[str]
    founding_date: Optional[date] = None
    income_level: Die = Die.D4
    description: Optional[str] = None
    location: Optional[str] = None
    notes: Optional[list[Note]] = None

    def repr_json(self) -> dict:
        return dict(
            __type__=Enterprise.__name__,
            creation_date=self.creation_date,
            name=self.name,
            enterprise_type=self.enterprise_type,
            founding_date=self.founding_date,
            income_level=self.income_level,
            description=self.description,
            location=self.location,
            notes=self.notes,
        )
