"""
Tests for the Elf class
"""
import unittest
from unittest.mock import patch
from elf import Elf
from character import Character


class TestElf(unittest.TestCase):
    """Test cases for the Elf class"""

    def setUp(self):
        """Set up test fixtures"""
        self.elf = Elf(
            name="test_elf",
            health=150,
            damage=30,
            weapon="bow",
            special_attack_chance=0.3,
            special_defense_chance=0.3,
            image="assets/elf.png"
        )
        self.attacker = Character(
            name="attacker",
            health=100,
            damage=20,
            weapon="sword",
            special_attack_chance=0.2,
            special_defense_chance=0.2,
            image="assets/knight.png"
        )

    def test_elf_inherits_from_character(self):
        """Test that Elf is a subclass of Character"""
        self.assertIsInstance(self.elf, Character)

    @patch('random.random', return_value=0.2)  # Force dodge (< 0.4)
    def test_dodge_avoids_damage(self, mock_random):
        """Test that elf dodges and takes no damage"""
        initial_health = self.elf.health
        self.elf.defend(self.attacker)
        # Elf should dodge and take no damage
        self.assertEqual(self.elf.health, initial_health)

    @patch('random.random', return_value=0.6)  # Force normal defense (>= 0.4)
    def test_normal_defense_takes_damage(self, mock_random):
        """Test that elf takes damage when not dodging"""
        initial_health = self.elf.health
        self.elf.defend(self.attacker)
        # Elf should take normal damage
        expected_health = initial_health - self.attacker.damage
        self.assertEqual(self.elf.health, expected_health)

    @patch('random.random', return_value=0.0)  # Force dodge
    def test_dodge_called_when_chance_met(self, mock_random):
        """Test that dodge is called when random chance is met"""
        initial_health = self.elf.health
        self.elf.defend(self.attacker)
        # Health should remain unchanged
        self.assertEqual(self.elf.health, initial_health)

    def test_elf_can_still_attack(self):
        """Test that elf retains normal attack ability"""
        enemy = Character(
            name="enemy",
            health=100,
            damage=15,
            weapon="axe",
            special_attack_chance=0.2,
            special_defense_chance=0.2,
            image="assets/knight.png"
        )
        initial_health = enemy.health
        self.elf.attack(enemy)
        # Enemy should take damage from elf's attack
        expected_health = initial_health - self.elf.damage
        self.assertEqual(enemy.health, expected_health)


if __name__ == '__main__':
    unittest.main()
