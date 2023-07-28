import pytest

from itom.model.character import Character


@pytest.fixture
def simple_character_ulf() -> Character:
    return Character(
        name="Ulf",
        strength=(12, 12),
        dexterity=(9, 9),
        willpower=(11, 11),
        hit_points=(6, 6),
        purse=(0, 50, 10),
    )
