from datetime import datetime

from utils.ito_mock_data_utils import generate_random_notes

from itom.model.misc_models import Die, Factory, Note


def test_note_repr_json() -> None:
    date = datetime(2023, 7, 28, 15, 18, 56)
    text = "This is a note."
    new_note = Note(creation_date=date, text=text)
    assert new_note.repr_json() == {
        "__type__": Note.__name__,
        "creation_date": date,
        "text": text,
    }


def test_factory_repr_json() -> None:
    creation_date = datetime(2023, 7, 28, 15, 18, 56)
    name = "Test Factory"
    new_factory = Factory(creation_date=creation_date, name=name)
    assert new_factory.repr_json() == {
        "__type__": Factory.__name__,
        "creation_date": creation_date,
        "name": name,
        "acquisition_date": None,
        "description": None,
        "location": None,
        "income_level": Die.D4,
        "notes": None,
    }


def test_factory_with_notes_repr_json() -> None:
    notes = generate_random_notes(amount=5)
    creation_date = datetime(2023, 7, 28, 15, 18, 56)
    name = "Test Factory"
    new_factory = Factory(creation_date=creation_date, name=name, notes=notes)
    assert new_factory.repr_json() == {
        "__type__": Factory.__name__,
        "creation_date": creation_date,
        "name": name,
        "acquisition_date": None,
        "description": None,
        "location": None,
        "income_level": Die.D4,
        "notes": notes,
    }
