"""
Tests for the Mage class
"""
import unittest
from unittest.mock import patch
from mage import Mage
from character import Character


class TestMage(unittest.TestCase):
    """Test cases for the Mage class"""

    def setUp(self):
        """Set up test fixtures"""
        self.mage = Mage(
            name="test_mage",
            health=100,
            damage=20,
            weapon="magic",
            special_attack_chance=0.3,
            special_defense_chance=0.3,
            image="assets/mage.png"
        )
        self.enemy = Character(
            name="enemy",
            health=100,
            damage=15,
            weapon="axe",
            special_attack_chance=0.2,
            special_defense_chance=0.2,
            image="assets/knight.png"
        )

    def test_mage_inherits_from_character(self):
        """Test that Mage is a subclass of Character"""
        self.assertIsInstance(self.mage, Character)

    @patch('random.random', return_value=0.1)  # Force special attack
    def test_fireball_when_health_above_40(self, mock_random):
        """Test that mage casts fireball when health > 40"""
        initial_health = self.enemy.health
        self.mage.attack(self.enemy)
        # Fireball does base damage + 10
        expected_health = initial_health - (self.mage.damage + 10)
        self.assertEqual(self.enemy.health, expected_health)

    @patch('random.random', return_value=0.1)  # Force special attack
    def test_heal_when_health_below_40(self, mock_random):
        """Test that mage heals when health <= 40"""
        self.mage.health = 40
        initial_mage_health = self.mage.health
        self.mage.attack(self.enemy)
        # Mage should heal by 20
        expected_mage_health = initial_mage_health + 20
        self.assertEqual(self.mage.health, expected_mage_health)
        # Enemy should not take damage when mage heals
        self.assertEqual(self.enemy.health, 100)

    @patch('random.random', return_value=0.9)  # Force normal attack
    def test_normal_attack_when_no_special(self, mock_random):
        """Test that normal attack happens when special doesn't trigger"""
        initial_health = self.enemy.health
        self.mage.attack(self.enemy)
        # Normal attack does base damage only
        expected_health = initial_health - self.mage.damage
        self.assertEqual(self.enemy.health, expected_health)

    def test_heal_increases_health_by_20(self):
        """Test that heal increases health by exactly 20"""
        self.mage.health = 30
        initial_health = self.mage.health
        self.mage.heal()
        self.assertEqual(self.mage.health, initial_health + 20)

    def test_fireball_bonus_damage(self):
        """Test that fireball applies correct bonus damage"""
        bonus_damage = 10
        initial_health = self.enemy.health
        self.mage.fireball(self.enemy)
        damage_dealt = initial_health - self.enemy.health
        self.assertEqual(damage_dealt, self.mage.damage + bonus_damage)


if __name__ == '__main__':
    unittest.main()
