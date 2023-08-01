import pytest

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


@pytest.mark.parametrize(
    "character_fixture_name", ["simple_character_ulf", "full_character_torsten"]
)
def test_repr_json(character_fixture_name: str, request: pytest.FixtureRequest) -> None:
    character = request.getfixturevalue(character_fixture_name)
    assert character.repr_json() == {
        "__type__": Character.__name__,
        "name": character.name,
        "strength": character.strength,
        "dexterity": character.dexterity,
        "willpower": character.willpower,
        "hit_points": character.hit_points,
        "purse": character.purse,
        "critical_damage": character.critical_damage,
        "armor": character.armor,
        "advantages": character.advantages,
        "disadvantages": character.disadvantages,
        "possessions": character.possessions,
        "armor_items": character.armor_items,
        "weapons": character.weapons,
        "notes": character.notes,
        "experience_level": character.experience_level,
        "arcana": character.arcana,
        "enterprises": character.enterprises,
    }
