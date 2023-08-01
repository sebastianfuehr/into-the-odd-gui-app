"""Provides functions to generate or manipulate test data connected to
the pen and paper game Into the Odd.

Methods
    generate_random_notes: Returns a set of random Note objects.
"""

from datetime import datetime
from random import choice, randint

from data.mock_data import COMMENTS, WEAPONS

from itom.model.misc_models import Note, Weapon


def generate_random_notes(amount: int) -> list[Note]:
    notes = []
    for nbr in range(0, amount):
        creation_date = datetime(
            year=randint(2020, 2025),
            month=randint(1, 12),
            day=randint(1, 28),
            hour=randint(0, 23),
            minute=randint(0, 59),
            second=randint(0, 59),
        )
        notes.append(Note(creation_date=creation_date, text=choice(COMMENTS)))
    return notes


def generate_random_weapons(amount: int) -> list[Weapon]:
    weapons = []
    for nbr in range(0, amount):
        rnd_weapon = choice(WEAPONS)
        weapons.append(rnd_weapon)
    return weapons
