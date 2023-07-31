from datetime import datetime

from utils.ito_mock_data_utils import generate_random_notes

from itom.model.misc_models import (
    Arcanmum,
    ArcanmumType,
    Armor,
    ArmorType,
    Die,
    Enterprise,
    Item,
    Note,
    Weapon,
    WeaponType,
)


def test_note_repr_json() -> None:
    date = datetime(2023, 7, 28, 15, 18, 56)
    text = "This is a note."
    new_note = Note(creation_date=date, text=text)
    assert new_note.repr_json() == {
        "__type__": Note.__name__,
        "creation_date": date,
        "text": text,
    }


def test_item_repr_json() -> None:
    name = "Test Item"
    new_item = Item(name=name)
    assert new_item.repr_json() == {
        "__type__": Item.__name__,
        "name": name,
        "description": None,
        "bulky": False,
        "worth": None,
        "image_file_path": None,
    }


def test_weapon_repr_json() -> None:
    name = "Pitchfork"
    new_weapon = Weapon(
        name=name,
        bulky=True,
        worth=(0, 1, 0),
        dmg_die=Die.D6,
        weapon_type=WeaponType.CRUDE_WEAPON,
    )
    assert new_weapon.repr_json() == {
        "__type__": Weapon.__name__,
        "name": name,
        "description": None,
        "bulky": True,
        "worth": (0, 1, 0),
        "image_file_path": None,
        "dmg_die": Die.D6,
        "amt_dice": 1,
        "weapon_type": "Crude Weapon",
    }


def test_armor_repr_json() -> None:
    name = "Ceremonial Armor"
    new_armor = Armor(
        name=name,
        bulky=True,
        worth=(0, 25, 0),
        protection_value=1,
        armor_type=ArmorType.CRUDE_ARMOR,
    )
    assert new_armor.repr_json() == {
        "__type__": Armor.__name__,
        "name": name,
        "description": None,
        "bulky": True,
        "worth": (0, 25, 0),
        "image_file_path": None,
        "protection_value": 1,
        "armor_type": "Crude Armor",
        "equipped": True,
    }


def test_arcanum_repr_json() -> None:
    name = "Pierced Heart"
    description = (
        "State an object that you desire. The heart indicated its direction and vague"
        " distance."
    )
    new_arcanum = Arcanmum(
        name=name,
        description=description,
        idx_nbr=12,
        arcanum_type=ArcanmumType.STANDARD,
    )
    assert new_arcanum.repr_json() == {
        "__type__": Arcanmum.__name__,
        "name": name,
        "description": description,
        "bulky": False,
        "worth": None,
        "image_file_path": None,
        "idx_nbr": 12,
        "arcanum_type": "Standard",
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
