"""
Tests for the Soldier class
"""
import unittest
from unittest.mock import patch
from soldier import Soldier
from character import Character


class TestSoldier(unittest.TestCase):
    """Test cases for the Soldier class"""

    def setUp(self):
        """Set up test fixtures"""
        self.soldier = Soldier(
            name="test_soldier",
            health=100,
            damage=25,
            weapon="sword",
            special_attack_chance=0.3,
            special_defense_chance=0.3,
            image="assets/knight.png"
        )
        self.enemy = Character(
            name="enemy",
            health=100,
            damage=20,
            weapon="axe",
            special_attack_chance=0.2,
            special_defense_chance=0.2,
            image="assets/knight.png"
        )

    def test_soldier_inherits_from_character(self):
        """Test that Soldier is a subclass of Character"""
        self.assertIsInstance(self.soldier, Character)

    @patch('random.random', return_value=0.1)  # Force special attack
    def test_special_attack_triggers(self, mock_random):
        """Test that special attack triggers when random chance is met"""
        initial_health = self.enemy.health
        self.soldier.attack(self.enemy)
        # Special attack does base damage + 10 bonus
        expected_health = initial_health - (self.soldier.damage + 10)
        self.assertEqual(self.enemy.health, expected_health)

    @patch('random.random', return_value=0.9)  # Force normal attack
    def test_normal_attack_when_no_special(self, mock_random):
        """Test that normal attack happens when special doesn't trigger"""
        initial_health = self.enemy.health
        self.soldier.attack(self.enemy)
        # Normal attack does base damage only
        expected_health = initial_health - self.soldier.damage
        self.assertEqual(self.enemy.health, expected_health)

    @patch('random.random', return_value=0.1)  # Force special attack
    def test_special_attack_bonus_damage(self, mock_random):
        """Test that special attack applies correct bonus damage"""
        bonus_damage = 10
        initial_health = self.enemy.health
        self.soldier.attack(self.enemy)
        damage_dealt = initial_health - self.enemy.health
        self.assertEqual(damage_dealt, self.soldier.damage + bonus_damage)


if __name__ == '__main__':
    unittest.main()
