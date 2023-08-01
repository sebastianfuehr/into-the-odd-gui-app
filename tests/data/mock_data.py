from itom.model.misc_models import Die, Weapon, WeaponType

# Comments have been generated via randomiandfy.com
COMMENTS = [
    "This is a random comment.",
    "A comment for testing purposes.",
    "Funny, you are funny, but thing is that being funny isn't enough anymore.",
    "Can't read? Just zoom in, what's the problem? It is a very simple solution.",
    "Top meme? I guess it is “Hey there miss”, so many people love this meme.",
    (
        "I can't even work in this environment, noise is too loud and the temperature"
        " is way too low."
    ),
    "Guys do you think that world which is present in WoW is absolutely amazing?",
    (
        "Which movie was the funniest of all? I think Very Scary Movie was super"
        " hilarious.How do you usually perform disk check? It takes too much time, is"
        " there any quicker way?"
    ),
    (
        "Bet it felt good, to swim in the sea after all these months of working, I"
        " could use vacation as well."
    ),
    (
        "Using other people's kindness for your own egoistic interests is a very bad"
        " thing to do."
    ),
]

WEAPONS = [
    Weapon(
        name="Sword",
        description="A simple sword.",
        bulky=False,
        worth=(0, 2, 0),
        image_file_path=None,
        dmg_die=Die.D6,
        amt_dice=1,
        weapon_type=WeaponType.HAND_WEAPON,
    ),
    Weapon(
        name="Musket",
        description="A ranged weapon.",
        bulky=True,
        worth=(0, 10, 0),
        image_file_path=None,
        dmg_die=Die.D8,
        amt_dice=1,
        weapon_type=WeaponType.FIELD_WEAPON,
    ),
    Weapon(
        name="Elephant gun",
        description="Cannot move and fire.",
        bulky=True,
        worth=(0, 0, 1),
        image_file_path=None,
        dmg_die=Die.D10,
        amt_dice=1,
        weapon_type=WeaponType.HEAVY_GUN,
    ),
]
