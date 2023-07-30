import datetime
import json
from typing import Any

import dateutil.parser

from itom.model.character import Character
from itom.model.misc_models import Factory, Note


class ItomJSONDecoder(json.JSONDecoder):
    """Decodes JSON strings into Into the Odd objects.

    Supported modules and classes are:
    - Character
    """

    def __init__(self) -> None:
        json.JSONDecoder.__init__(self, object_hook=self.object_hook)

    def object_hook(self, json_dict: dict) -> Character | Note | Factory | dict:
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
                armor=json_dict["armor"],
                advantages=json_dict["advantages"],
                disadvantages=json_dict["disadvantages"],
                possessions=json_dict["possessions"],
                weapons=json_dict["weapons"],
                notes=json_dict["notes"],
                experience_level=json_dict["experience_level"],
                arcana=json_dict["arcana"],
                enterprises=json_dict["enterprises"],
            )
        if "__type__" in json_dict and json_dict["__type__"] == Note.__name__:
            date = dateutil.parser.parse(json_dict["creation_date"])
            return Note(creation_date=date, text=json_dict["text"])
        if "__type__" in json_dict and json_dict["__type__"] == Factory.__name__:
            creation_date = dateutil.parser.parse(json_dict["creation_date"])
            acquisition_date = None
            if json_dict["acquisition_date"]:
                acquisition_date = dateutil.parser.parse(
                    json_dict["acquisition_date"]
                ).date()
            return Factory(
                creation_date=creation_date,
                name=json_dict["name"],
                acquisition_date=acquisition_date,
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
