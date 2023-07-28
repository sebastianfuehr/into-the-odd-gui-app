from itom.model.character import Character, ExperienceLevel


def test_character_creation_default_values() -> None:
    new_character = Character(
        name="Ulf",
        strength=(10, 10),
        dexterity=(10, 10),
        willpower=(10, 10),
        hit_points=(6, 6),
        purse=(0, 0, 10),
    )
    assert new_character.critical_damage is False
    assert new_character.armor == 0
    assert new_character.experience_level == ExperienceLevel.NOVICE


def test_repr_json(simple_character_ulf: Character) -> None:
    assert simple_character_ulf.repr_json() == {
        "__type__": Character.__name__,
        "name": "Ulf",
        "strength": (12, 12),
        "dexterity": (9, 9),
        "willpower": (11, 11),
        "hit_points": (6, 6),
        "purse": (0, 50, 10),
        "critical_damage": False,
        "armor": 0,
        "advantages": None,
        "disadvantages": None,
        "possessions": None,
        "weapons": None,
        "notes": None,
        "experience_level": "Novice",
        "arcana": None,
        "enterprises": None,
    }
