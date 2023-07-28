import json
from datetime import datetime

from itom.controller.json_controller import ItomJSONDecoderFunction, ItomJSONEncoder
from itom.model.character import Character
from itom.model.utils import Note


def test_json_encode_character(simple_character_ulf: Character) -> None:
    assert json.dumps(simple_character_ulf.repr_json(), cls=ItomJSONEncoder) == (
        '{"__type__": "Character", '
        '"name": "Ulf", '
        '"strength": [12, 12], '
        '"dexterity": [9, 9], '
        '"willpower": [11, 11], '
        '"hit_points": [6, 6], '
        '"purse": [0, 50, 10], '
        '"critical_damage": false, '
        '"armor": 0, '
        '"advantages": null, '
        '"disadvantages": null, '
        '"possessions": null, '
        '"weapons": null, '
        '"notes": null, '
        '"experience_level": "Novice", '
        '"arcana": null, '
        '"enterprises": null}'
    )


def test_json_decode_character(simple_character_ulf: Character) -> None:
    json_file = json.dumps(simple_character_ulf.repr_json(), cls=ItomJSONEncoder)
    decoded_character = json.loads(json_file, object_hook=ItomJSONDecoderFunction)
    assert decoded_character == simple_character_ulf


def test_json_encode_note() -> None:
    date = datetime(2023, 7, 28, 15, 15, 56)
    text = "This is a note."
    new_note = Note(creation_date=date, text=text)
    assert json.dumps(new_note.repr_json(), cls=ItomJSONEncoder) == (
        '{"__type__": "Note", '
        '"creation_date": "2023-07-28T15:15:56", '
        '"text": "This is a note."}'
    )


def test_json_decode_note() -> None:
    date = datetime(2023, 7, 28, 15, 15, 56)
    text = "This is a note."
    new_note = Note(creation_date=date, text=text)
    json_file = json.dumps(new_note.repr_json(), cls=ItomJSONEncoder)
    decoded_note = json.loads(json_file, object_hook=ItomJSONDecoderFunction)
    assert decoded_note == new_note
