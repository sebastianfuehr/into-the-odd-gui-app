from datetime import datetime

from utils.ito_mock_data_utils import generate_random_notes

from itom.model.misc_models import Die, Enterprise, Note


def test_note_repr_json() -> None:
    date = datetime(2023, 7, 28, 15, 18, 56)
    text = "This is a note."
    new_note = Note(creation_date=date, text=text)
    assert new_note.repr_json() == {
        "__type__": Note.__name__,
        "creation_date": date,
        "text": text,
    }


class TestEnterpriseModel:
    def test_enterprise_repr_json(self) -> None:
        creation_date = datetime(2023, 7, 28, 15, 18, 56)
        name = "Test Enterprise"
        enterprise_type = "Coal production factory"
        new_enterprise = Enterprise(
            creation_date=creation_date, name=name, enterprise_type=enterprise_type
        )
        assert new_enterprise.repr_json() == {
            "__type__": Enterprise.__name__,
            "creation_date": creation_date,
            "name": name,
            "enterprise_type": enterprise_type,
            "founding_date": None,
            "income_level": Die.D4,
            "description": None,
            "location": None,
            "notes": None,
        }

    def test_enterprise_with_notes_repr_json(self) -> None:
        notes = generate_random_notes(amount=5)
        creation_date = datetime(2023, 7, 28, 15, 18, 56)
        name = "Test Factory"
        enterprise_type = "Coal production factory"
        new_enterprise = Enterprise(
            creation_date=creation_date,
            name=name,
            enterprise_type=enterprise_type,
            notes=notes,
        )
        assert new_enterprise.repr_json() == {
            "__type__": Enterprise.__name__,
            "creation_date": creation_date,
            "name": name,
            "enterprise_type": enterprise_type,
            "founding_date": None,
            "income_level": Die.D4,
            "description": None,
            "location": None,
            "notes": notes,
        }
