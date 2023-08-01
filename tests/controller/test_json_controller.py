import json
from datetime import datetime

import pytest

from itom.controller.json_controller import ItomJSONDecoder, ItomJSONEncoder
from itom.model.character import Character
from itom.model.misc_models import (
    ArcanmumType,
    Arcanum,
    Armor,
    ArmorType,
    Die,
    Enterprise,
    InventoryItem,
    Item,
    Note,
    Weapon,
    WeaponType,
)


class TestCharacterModelJSONSerialization:
    def test_json_encode_character(self, simple_character_ulf: Character) -> None:
        assert (
            json.dumps(simple_character_ulf.repr_json(), cls=ItomJSONEncoder)
            == '{"__type__": "Character", '
            '"name": "Ulf", '
            '"strength": [12, 12], '
            '"dexterity": [9, 9], '
            '"willpower": [11, 11], '
            '"hit_points": [6, 6], '
            '"purse": [0, 50, 10], '
            '"critical_damage": false, '
            '"armor": 0, '
            '"advantages": null, '
            '"disadvantages": null, '
            '"possessions": null, '
            '"armor_items": null, '
            '"weapons": null, '
            '"notes": null, '
            '"experience_level": "Novice", '
            '"arcana": null}'
        )

    def test_json_encode_full_character_torsten(
        self, full_character_torsten: Character
    ) -> None:
        notes_json = json.dumps(full_character_torsten.notes, cls=ItomJSONEncoder)
        weapons_json = json.dumps(full_character_torsten.weapons, cls=ItomJSONEncoder)
        assert (
            json.dumps(full_character_torsten.repr_json(), cls=ItomJSONEncoder)
            == '{"__type__": "Character", '
            '"name": "Torsten", '
            '"strength": [10, 10], '
            '"dexterity": [12, 12], '
            '"willpower": [13, 13], '
            '"hit_points": [8, 8], '
            '"purse": [25, 89, 121], '
            '"critical_damage": false, '
            '"armor": 0, '
            '"advantages": ["Good looking", "Quick thinker"], '
            '"disadvantages": ["Curiousity"], '
            '"possessions": null, '
            '"armor_items": null, '
            f'"weapons": {weapons_json}, '
            f'"notes": {notes_json}, '
            '"experience_level": "Professional", '
            '"arcana": null}'
        )

    @pytest.mark.parametrize(
        "character_fixture_name", ["simple_character_ulf", "full_character_torsten"]
    )
    def test_json_decode_character(
        self, character_fixture_name: str, request: pytest.FixtureRequest
    ) -> None:
        character = request.getfixturevalue(character_fixture_name)
        json_file = json.dumps(character.repr_json(), cls=ItomJSONEncoder)
        decoded_character = json.loads(json_file, cls=ItomJSONDecoder)
        assert decoded_character == character


class TestNoteModelJSONSerialization:
    def test_json_encode_note(self) -> None:
        date = datetime(2023, 7, 28, 15, 15, 56)
        text = "This is a note."
        new_note = Note(creation_date=date, text=text)
        assert (
            json.dumps(new_note.repr_json(), cls=ItomJSONEncoder)
            == '{"__type__": "Note", '
            '"creation_date": "2023-07-28T15:15:56", '
            '"text": "This is a note."}'
        )

    def test_json_decode_note(self) -> None:
        date = datetime(2023, 7, 28, 15, 15, 56)
        text = "This is a note."
        new_note = Note(creation_date=date, text=text)
        json_file = json.dumps(new_note.repr_json(), cls=ItomJSONEncoder)
        decoded_note = json.loads(json_file, cls=ItomJSONDecoder)
        assert decoded_note == new_note


class TestEnumJSONSerialization:
    def test_json_encode_die(self) -> None:
        json_repr = json.dumps(Die.D4)
        assert json_repr == "4"

    def test_json_encode_weapon_type(self) -> None:
        json_repr = json.dumps(WeaponType.CRUDE_WEAPON)
        assert json_repr == '"Crude Weapon"'

    def test_json_encode_arcanum_type(self) -> None:
        json_repr = json.dumps(ArcanmumType.STANDARD)
        assert json_repr == '"Standard"'


class TestItemModelJSONSerialization:
    @pytest.fixture
    def item_lockpick(self) -> Item:
        return Item(name="Lockpicks", worth=(0, 1, 0))

    def test_json_encode_item(self, item_lockpick: Item) -> None:
        assert (
            json.dumps(item_lockpick.repr_json(), cls=ItomJSONEncoder)
            == '{"__type__": "Item", '
            f'"name": "{item_lockpick.name}", '
            '"description": null, '
            '"bulky": false, '
            '"worth": [0, 1, 0], '
            '"image_file_path": null}'
        )

    def test_json_decode_item(self, item_lockpick: Item) -> None:
        json_file = json.dumps(item_lockpick.repr_json(), cls=ItomJSONEncoder)
        decoded_item = json.loads(json_file, cls=ItomJSONDecoder)
        assert decoded_item == item_lockpick


class TestInventoryItemModelJSONSerialization:
    @pytest.fixture
    def item_lockpick(self) -> InventoryItem:
        return InventoryItem(name="Lockpick", worth=(0, 1, 0), amount=20)

    def test_json_encode_item(self, item_lockpick: InventoryItem) -> None:
        assert (
            json.dumps(item_lockpick.repr_json(), cls=ItomJSONEncoder)
            == f'{{"__type__": "{InventoryItem.__name__}", '
            f'"name": "{item_lockpick.name}", '
            '"description": null, '
            '"bulky": false, '
            '"worth": [0, 1, 0], '
            '"image_file_path": null, '
            f'"amount": {item_lockpick.amount}}}'
        )

    def test_json_decode_item(self, item_lockpick: InventoryItem) -> None:
        json_file = json.dumps(item_lockpick.repr_json(), cls=ItomJSONEncoder)
        decoded_item = json.loads(json_file, cls=ItomJSONDecoder)
        assert decoded_item == item_lockpick


class TestWeaponJSONSerialization:
    def test_json_encode_weapon(self) -> None:
        name = "Sword"
        worth = (0, 2, 0)
        dmg_die = Die.D6
        weapon_type = WeaponType.HAND_WEAPON
        new_weapon = Weapon(
            name=name, worth=worth, dmg_die=dmg_die, weapon_type=weapon_type
        )
        assert (
            json.dumps(new_weapon.repr_json(), cls=ItomJSONEncoder)
            == '{"__type__": "Weapon", '
            '"name": "Sword", '
            '"description": null, '
            '"bulky": false, '
            '"worth": [0, 2, 0], '
            '"image_file_path": null, '
            '"dmg_die": 6, '
            '"amt_dice": 1, '
            '"weapon_type": "Hand Weapon"}'
        )

    def test_json_decode_weapon(self) -> None:
        name = "Sword"
        worth = (0, 2, 0)
        dmg_die = Die.D6
        weapon_type = WeaponType.HAND_WEAPON
        new_weapon = Weapon(
            name=name, worth=worth, dmg_die=dmg_die, weapon_type=weapon_type
        )
        json_file = json.dumps(new_weapon.repr_json(), cls=ItomJSONEncoder)
        decoded_weapon = json.loads(json_file, cls=ItomJSONDecoder)
        assert decoded_weapon == new_weapon


class TestArmorJSONSerialization:
    @pytest.fixture
    def armor_breastplate_and_helm(self) -> Armor:
        return Armor(
            name="Breastplate and helm",
            worth=(0, 50, 0),
            protection_value=1,
            armor_type=ArmorType.MODERN_ARMOR,
        )

    def test_json_encode_armor(self, armor_breastplate_and_helm: Armor) -> None:
        assert (
            json.dumps(armor_breastplate_and_helm.repr_json(), cls=ItomJSONEncoder)
            == '{"__type__": "Armor", '
            '"name": "Breastplate and helm", '
            '"description": null, '
            '"bulky": false, '
            '"worth": [0, 50, 0], '
            '"image_file_path": null, '
            '"protection_value": 1, '
            '"armor_type": "Modern Armor", '
            '"equipped": true}'
        )

    def test_json_decode_armor(self, armor_breastplate_and_helm: Armor) -> None:
        json_file = json.dumps(
            armor_breastplate_and_helm.repr_json(), cls=ItomJSONEncoder
        )
        decoded_weapon = json.loads(json_file, cls=ItomJSONDecoder)
        assert decoded_weapon == armor_breastplate_and_helm


class TestArcanumJSONSerialization:
    @pytest.fixture
    def arcanum_pale_flame(self) -> Arcanum:
        return Arcanum(
            name="Pale Flame",
            description="An object ...",
            idx_nbr=13,
            arcanum_type=ArcanmumType.STANDARD,
        )

    def test_json_encode_arcanum(self, arcanum_pale_flame: Arcanum) -> None:
        assert (
            json.dumps(arcanum_pale_flame.repr_json(), cls=ItomJSONEncoder)
            == '{"__type__": "Arcanum", '
            '"name": "Pale Flame", '
            '"description": "An object ...", '
            '"bulky": false, '
            '"worth": null, '
            '"image_file_path": null, '
            '"idx_nbr": 13, '
            '"arcanum_type": "Standard"}'
        )

    def test_json_decode_arcanum(self, arcanum_pale_flame: Arcanum) -> None:
        json_file = json.dumps(arcanum_pale_flame.repr_json(), cls=ItomJSONEncoder)
        decoded_arcanum = json.loads(json_file, cls=ItomJSONDecoder)
        assert decoded_arcanum == arcanum_pale_flame


class TestEnterpriseModelJSONSerialization:
    def test_json_encode_enterprise_simple(self) -> None:
        creation_date = datetime(2023, 7, 28, 15, 18, 56)
        name = "Test Enterprise"
        enterprise_type = "Coal production factory"
        owners = ["Ulf", "Torsten"]
        new_enterprise = Enterprise(
            creation_date=creation_date,
            name=name,
            enterprise_type=enterprise_type,
            owners=owners,
        )
        assert (
            json.dumps(new_enterprise.repr_json(), cls=ItomJSONEncoder)
            == '{"__type__": "Enterprise", '
            '"creation_date": "2023-07-28T15:18:56", '
            '"name": "Test Enterprise", '
            '"enterprise_type": "Coal production factory", '
            '"owners": ["Ulf", "Torsten"], '
            '"founding_date": null, '
            '"income_level": 4, '
            '"description": null, '
            '"location": null, '
            '"notes": null}'
        )

    def test_json_decode_enterprise_simple(self) -> None:
        creation_date = datetime(2023, 7, 28, 15, 18, 56)
        name = "Test Enterprise"
        enterprise_type = "Coal production factory"
        owners = ["Ulf", "Torsten"]
        new_enterprise = Enterprise(
            creation_date=creation_date,
            name=name,
            enterprise_type=enterprise_type,
            owners=owners,
        )
        json_file = json.dumps(new_enterprise.repr_json(), cls=ItomJSONEncoder)
        decoded_factory = json.loads(json_file, cls=ItomJSONDecoder)
        assert decoded_factory == new_enterprise

    def test_json_encode_enterprise_with_notes(self) -> None:
        creation_date = datetime(2023, 7, 28, 15, 18, 56)
        notes = [Note(creation_date=creation_date, text="Bought a factory.")]
        name = "Test Enterprise"
        enterprise_type = "Coal production factory"
        owners = ["Ulf", "Torsten"]
        new_enterprise = Enterprise(
            creation_date=creation_date,
            name=name,
            enterprise_type=enterprise_type,
            owners=owners,
            notes=notes,
        )
        assert (
            json.dumps(new_enterprise.repr_json(), cls=ItomJSONEncoder)
            == '{"__type__": "Enterprise", '
            '"creation_date": "2023-07-28T15:18:56", '
            '"name": "Test Enterprise", '
            '"enterprise_type": "Coal production factory", '
            '"owners": ["Ulf", "Torsten"], '
            '"founding_date": null, '
            '"income_level": 4, '
            '"description": null, '
            '"location": null, '
            '"notes": [{'
            '"__type__": "Note", '
            '"creation_date": "2023-07-28T15:18:56", '
            '"text": "Bought a factory."'
            "}]}"
        )
