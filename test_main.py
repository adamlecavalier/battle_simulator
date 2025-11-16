"""
Tests for the main module functions
"""
import unittest
from unittest.mock import patch, mock_open, MagicMock
import json
from main import battle_round
from character import Character
from soldier import Soldier
from mage import Mage
from elf import Elf
from king import King


class TestBattleRound(unittest.TestCase):
    """Test cases for the battle_round function"""

    def setUp(self):
        """Set up test fixtures"""
        self.character1 = Character(
            name="fighter",
            health=100,
            damage=25,
            weapon="sword",
            special_attack_chance=0.3,
            special_defense_chance=0.3,
            image="assets/knight.png"
        )
        self.character2 = Character(
            name="defender",
            health=80,
            damage=20,
            weapon="shield",
            special_attack_chance=0.2,
            special_defense_chance=0.2,
            image="assets/knight.png"
        )

    def test_battle_round_attacker_attacks(self):
        """Test that attacker deals damage in battle round"""
        initial_defender_health = self.character2.health
        battle_round(self.character1, self.character2)
        self.assertLess(self.character2.health, initial_defender_health)

    def test_battle_round_defender_counterattacks_when_alive(self):
        """Test that defender counterattacks if still alive"""
        initial_attacker_health = self.character1.health
        battle_round(self.character1, self.character2)
        # Defender should counterattack since they survive the first hit
        self.assertLess(self.character1.health, initial_attacker_health)

    def test_battle_round_no_counterattack_when_defender_dies(self):
        """Test that defender doesn't counterattack if killed"""
        # Create a weak defender that will die in one hit
        weak_defender = Character(
            name="weak",
            health=10,
            damage=50,
            weapon="dagger",
            special_attack_chance=0.2,
            special_defense_chance=0.2,
            image="assets/knight.png"
        )
        initial_attacker_health = self.character1.health
        battle_round(self.character1, weak_defender)
        # Attacker should not take damage since defender died
        self.assertEqual(self.character1.health, initial_attacker_health)
        self.assertFalse(weak_defender.is_alive())

    def test_battle_round_both_characters_take_damage(self):
        """Test that both characters can take damage in a round"""
        initial_char1_health = self.character1.health
        initial_char2_health = self.character2.health
        battle_round(self.character1, self.character2)
        # Both should have taken damage
        self.assertLess(self.character1.health, initial_char1_health)
        self.assertLess(self.character2.health, initial_char2_health)


class TestTypeMap(unittest.TestCase):
    """Test cases for character type mapping"""

    def test_type_map_imports(self):
        """Test that type_map can be imported and contains expected types"""
        from type_map import type_map
        self.assertIn("soldier", type_map)
        self.assertIn("mage", type_map)
        self.assertIn("elf", type_map)
        self.assertIn("king", type_map)

    def test_type_map_correct_classes(self):
        """Test that type_map maps to correct character classes"""
        from type_map import type_map
        self.assertEqual(type_map["soldier"], Soldier)
        self.assertEqual(type_map["mage"], Mage)
        self.assertEqual(type_map["elf"], Elf)
        self.assertEqual(type_map["king"], King)

    def test_character_creation_from_json_data(self):
        """Test that characters can be created from JSON data using type_map"""
        from type_map import type_map
        
        character_data = {
            "name": "soldier",
            "health": 100,
            "damage": 25,
            "weapon": "sword",
            "special_attack_chance": 0.3,
            "special_defense_chance": 0.3,
            "image": "assets/knight.png"
        }
        
        CharClass = type_map.get(character_data["name"], Character)
        character = CharClass(**character_data)
        
        self.assertIsInstance(character, Soldier)
        self.assertEqual(character.name, "soldier")
        self.assertEqual(character.health, 100)
        self.assertEqual(character.damage, 25)


if __name__ == '__main__':
    unittest.main()
