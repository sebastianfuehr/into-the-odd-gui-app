import datetime
import json
from typing import Any

import dateutil.parser

from itom.model.character import Character
from itom.model.misc_models import (
    Arcanum,
    Armor,
    Enterprise,
    InventoryItem,
    Item,
    Note,
    Weapon,
)


class ItomJSONDecoder(json.JSONDecoder):
    """Decodes JSON strings into Into the Odd objects.

    Supported modules and classes are:
    - Character
    """

    def __init__(self) -> None:
        json.JSONDecoder.__init__(self, object_hook=self.object_hook)

    def object_hook(
        self, json_dict: dict
    ) -> Character | Note | Item | Enterprise | dict:
        if "__type__" in json_dict and json_dict["__type__"] == Character.__name__:
            strength = int(json_dict["strength"][0]), int(json_dict["strength"][1])
            dexterity = int(json_dict["dexterity"][0]), int(json_dict["dexterity"][1])
            willpower = int(json_dict["willpower"][0]), int(json_dict["willpower"][1])
            hit_points = int(json_dict["hit_points"][0]), int(
                json_dict["hit_points"][1]
            )
            purse = (
                int(json_dict["purse"][0]),
                int(json_dict["purse"][1]),
                int(json_dict["purse"][2]),
            )
            return Character(
                name=json_dict["name"],
                strength=strength,
                dexterity=dexterity,
                willpower=willpower,
                hit_points=hit_points,
                purse=purse,
                critical_damage=json_dict["critical_damage"],
                advantages=json_dict["advantages"],
                disadvantages=json_dict["disadvantages"],
                possessions=json_dict["possessions"],
                armor_items=json_dict["armor_items"],
                weapons=json_dict["weapons"],
                notes=json_dict["notes"],
                experience_level=json_dict["experience_level"],
                arcana=json_dict["arcana"],
            )
        if "__type__" in json_dict and json_dict["__type__"] == Item.__name__:
            worth = None
            if json_dict["worth"]:
                worth = (
                    int(json_dict["worth"][0]),
                    int(json_dict["worth"][1]),
                    int(json_dict["worth"][2]),
                )
            return Item(
                name=json_dict["name"],
                description=json_dict["description"],
                bulky=json_dict["bulky"],
                worth=worth,
                image_file_path=json_dict["image_file_path"],
            )
        if "__type__" in json_dict and json_dict["__type__"] == InventoryItem.__name__:
            worth = None
            if json_dict["worth"]:
                worth = (
                    int(json_dict["worth"][0]),
                    int(json_dict["worth"][1]),
                    int(json_dict["worth"][2]),
                )
            return InventoryItem(
                name=json_dict["name"],
                description=json_dict["description"],
                bulky=json_dict["bulky"],
                worth=worth,
                image_file_path=json_dict["image_file_path"],
                amount=json_dict["amount"],
            )
        if "__type__" in json_dict and json_dict["__type__"] == Weapon.__name__:
            worth = None
            if json_dict["worth"]:
                worth = (
                    int(json_dict["worth"][0]),
                    int(json_dict["worth"][1]),
                    int(json_dict["worth"][2]),
                )
            return Weapon(
                name=json_dict["name"],
                description=json_dict["description"],
                bulky=json_dict["bulky"],
                worth=worth,
                image_file_path=json_dict["image_file_path"],
                dmg_die=json_dict["dmg_die"],
                amt_dice=json_dict["amt_dice"],
                weapon_type=json_dict["weapon_type"],
            )
        if "__type__" in json_dict and json_dict["__type__"] == Armor.__name__:
            worth = None
            if json_dict["worth"]:
                worth = (
                    int(json_dict["worth"][0]),
                    int(json_dict["worth"][1]),
                    int(json_dict["worth"][2]),
                )
            return Armor(
                name=json_dict["name"],
                description=json_dict["description"],
                bulky=json_dict["bulky"],
                worth=worth,
                image_file_path=json_dict["image_file_path"],
                protection_value=json_dict["protection_value"],
                armor_type=json_dict["armor_type"],
                equipped=json_dict["equipped"],
            )
        if "__type__" in json_dict and json_dict["__type__"] == Arcanum.__name__:
            worth = None
            if json_dict["worth"]:
                worth = (
                    int(json_dict["worth"][0]),
                    int(json_dict["worth"][1]),
                    int(json_dict["worth"][2]),
                )
            return Arcanum(
                name=json_dict["name"],
                description=json_dict["description"],
                bulky=json_dict["bulky"],
                worth=worth,
                image_file_path=json_dict["image_file_path"],
                idx_nbr=json_dict["idx_nbr"],
                arcanum_type=json_dict["arcanum_type"],
            )
        if "__type__" in json_dict and json_dict["__type__"] == Note.__name__:
            date = dateutil.parser.parse(json_dict["creation_date"])
            return Note(creation_date=date, text=json_dict["text"])
        if "__type__" in json_dict and json_dict["__type__"] == Enterprise.__name__:
            creation_date = dateutil.parser.parse(json_dict["creation_date"])
            founding_date = None
            if json_dict["founding_date"]:
                founding_date = dateutil.parser.parse(json_dict["founding_date"]).date()
            return Enterprise(
                creation_date=creation_date,
                name=json_dict["name"],
                enterprise_type=json_dict["enterprise_type"],
                owners=json_dict["owners"],
                founding_date=founding_date,
                description=json_dict["description"],
                location=json_dict["location"],
                income_level=json_dict["income_level"],
                notes=json_dict["notes"],
            )
        return json_dict


class ItomJSONEncoder(json.JSONEncoder):
    """Encodes Into the Odd objects, as well as datetime objects into
    JSON format.
    """

    def default(self, obj: object) -> dict | Any:  # type: ignore[misc] # noqa: F821
        if hasattr(obj, "repr_json"):
            return obj.repr_json()
        elif isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()
        else:
            return json.JSONEncoder.default(self, obj)
