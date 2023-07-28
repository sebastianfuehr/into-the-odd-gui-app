import json
import dataclasses
from itom.model.character import Character, ExperienceLevel


def test_character_creation_default_values():
    new_character = Character(
        name="Ulf",
        strength=(10, 10),
        dexterity=(10, 10),
        willpower=(10, 10),
        hit_points=(6, 6),
        purse=(0, 0, 10),
    )
    assert new_character.critical_damage == False
    assert new_character.armor == 0
    assert new_character.experience_level == ExperienceLevel.NOVICE
