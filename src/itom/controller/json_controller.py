import datetime
import json
from typing import Any

import dateutil.parser

from itom.model.character import Character
from itom.model.utils import Note


def ItomJSONDecoderFunction(jsonDict: dict) -> Note | Character | None:
    """Decodes JSON strings into Into the Odd objects.

    Supported modules and classes are:
    - Character
    """
    if "__type__" in jsonDict and jsonDict["__type__"] == Character.__name__:
        strength = int(jsonDict["strength"][0]), int(jsonDict["strength"][1])
        dexterity = int(jsonDict["dexterity"][0]), int(jsonDict["dexterity"][1])
        willpower = int(jsonDict["willpower"][0]), int(jsonDict["willpower"][1])
        hit_points = int(jsonDict["hit_points"][0]), int(jsonDict["hit_points"][1])
        purse = (
            int(jsonDict["purse"][0]),
            int(jsonDict["purse"][1]),
            int(jsonDict["purse"][2]),
        )
        return Character(
            name=jsonDict["name"],
            strength=strength,
            dexterity=dexterity,
            willpower=willpower,
            hit_points=hit_points,
            purse=purse,
        )
    if "__type__" in jsonDict and jsonDict["__type__"] == Note.__name__:
        date = dateutil.parser.parse(jsonDict["creation_date"])
        return Note(creation_date=date, text=jsonDict["text"])
    return None


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
