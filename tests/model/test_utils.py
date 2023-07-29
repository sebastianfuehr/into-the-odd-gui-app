from datetime import datetime

from itom.model.utils import Note


def test_note_repr_json() -> None:
    date = datetime(2023, 7, 28, 15, 18, 56)
    text = "This is a note."
    new_note = Note(creation_date=date, text=text)
    assert new_note.repr_json() == {
        "__type__": Note.__name__,
        "creation_date": date,
        "text": text,
    }
