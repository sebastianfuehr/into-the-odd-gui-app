import json
from datetime import datetime

import pytest

from itom.controller.json_controller import ItomJSONDecoder, ItomJSONEncoder
from itom.model.character import Character
from itom.model.misc_models import Die, Factory, Note


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


def test_json_encode_full_character_torsten(full_character_torsten: Character) -> None:
    notes_json = json.dumps(full_character_torsten.notes, cls=ItomJSONEncoder)
    assert json.dumps(full_character_torsten.repr_json(), cls=ItomJSONEncoder) == (
        '{"__type__": "Character", '
        '"name": "Torsten", '
        '"strength": [10, 10], '
        '"dexterity": [12, 12], '
        '"willpower": [13, 13], '
        '"hit_points": [8, 8], '
        '"purse": [25, 89, 121], '
        '"critical_damage": false, '
        '"armor": 2, '
        '"advantages": ["Good looking", "Quick thinker"], '
        '"disadvantages": ["Curiousity"], '
        '"possessions": null, '
        '"weapons": null, '
        f'"notes": {notes_json}, '
        '"experience_level": "Professional", '
        '"arcana": null, '
        '"enterprises": null}'
    )


@pytest.mark.parametrize(
    "character_fixture_name", ["simple_character_ulf", "full_character_torsten"]
)
def test_json_decode_character(
    character_fixture_name: str, request: pytest.FixtureRequest
) -> None:
    character = request.getfixturevalue(character_fixture_name)
    json_file = json.dumps(character.repr_json(), cls=ItomJSONEncoder)
    decoded_character = json.loads(json_file, cls=ItomJSONDecoder)
    assert decoded_character == character


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
    decoded_note = json.loads(json_file, cls=ItomJSONDecoder)
    assert decoded_note == new_note


def test_json_encode_die() -> None:
    json_repr = json.dumps(Die.D4)
    assert json_repr == "4"


def test_json_encode_factory_simple() -> None:
    creation_date = datetime(2023, 7, 28, 15, 18, 56)
    name = "Test Factory"
    new_factory = Factory(creation_date=creation_date, name=name)
    assert json.dumps(new_factory.repr_json(), cls=ItomJSONEncoder) == (
        '{"__type__": "Factory", '
        '"creation_date": "2023-07-28T15:18:56", '
        '"name": "Test Factory", '
        '"acquisition_date": null, '
        '"description": null, '
        '"location": null, '
        '"income_level": 4, '
        '"notes": null}'
    )


def test_json_decode_factory_simple() -> None:
    creation_date = datetime(2023, 7, 28, 15, 18, 56)
    name = "Test Factory"
    new_factory = Factory(creation_date=creation_date, name=name)
    json_file = json.dumps(new_factory.repr_json(), cls=ItomJSONEncoder)
    decoded_factory = json.loads(json_file, cls=ItomJSONDecoder)
    assert decoded_factory == new_factory


def test_json_encode_factory_with_notes() -> None:
    creation_date = datetime(2023, 7, 28, 15, 18, 56)
    notes = [Note(creation_date=creation_date, text="Bought a factory.")]
    name = "Test Factory"
    new_factory = Factory(creation_date=creation_date, name=name, notes=notes)
    assert json.dumps(new_factory.repr_json(), cls=ItomJSONEncoder) == (
        '{"__type__": "Factory", '
        '"creation_date": "2023-07-28T15:18:56", '
        '"name": "Test Factory", '
        '"acquisition_date": null, '
        '"description": null, '
        '"location": null, '
        '"income_level": 4, '
        '"notes": [{'
        '"__type__": "Note", '
        '"creation_date": "2023-07-28T15:18:56", '
        '"text": "Bought a factory."'
        "}]}"
    )
