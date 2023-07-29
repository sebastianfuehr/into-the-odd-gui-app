from datetime import datetime

from itom.model.utils import Die, Note, Factory


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
