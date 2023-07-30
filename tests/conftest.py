import pytest

from itom.model.character import Character, ExperienceLevel
from utils.ito_mock_data_utils import generate_random_notes


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


@pytest.fixture
def full_character_torsten() -> Character:
    notes = generate_random_notes(3)
    return Character(
        name="Torsten",
        strength=(10, 10),
        dexterity=(12, 12),
        willpower=(13, 13),
        hit_points=(8, 8),
        purse=(25, 89, 121),
        critical_damage=False,
        armor=2,
        advantages=["Good looking", "Quick thinker"],
        disadvantages=["Curiousity"],
        possessions=None,
        weapons=None,
        notes=notes,
        experience_level=ExperienceLevel.PROFESSIONAL,
        arcana=None,
        enterprises=None,
    )
