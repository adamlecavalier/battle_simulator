"""
Tests for the King class
"""
import unittest
from unittest.mock import patch
from king import King
from character import Character


class TestKing(unittest.TestCase):
    """Test cases for the King class"""

    def setUp(self):
        """Set up test fixtures"""
        self.king = King(
            name="test_king",
            health=50,
            damage=5,
            weapon="crown",
            special_attack_chance=0.3,
            special_defense_chance=0.3,
            image="assets/king.png"
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

    def test_king_inherits_from_character(self):
        """Test that King is a subclass of Character"""
        self.assertIsInstance(self.king, Character)

    @patch('random.random', return_value=0.1)  # Force super attack
    def test_super_attack_triggers(self, mock_random):
        """Test that super attack triggers when random chance is met"""
        initial_health = self.enemy.health
        self.king.attack(self.enemy)
        # Super attack does 20 damage
        expected_health = initial_health - 20
        self.assertEqual(self.enemy.health, expected_health)

    @patch('random.random', return_value=0.9)  # Force normal attack
    def test_normal_attack_when_no_special(self, mock_random):
        """Test that normal attack happens when special doesn't trigger"""
        initial_health = self.enemy.health
        self.king.attack(self.enemy)
        # Normal attack does base damage only
        expected_health = initial_health - self.king.damage
        self.assertEqual(self.enemy.health, expected_health)

    @patch('random.random', return_value=0.1)  # Force special defense
    def test_special_defense_counter_attack(self, mock_random):
        """Test that special defense counter-attacks with poison"""
        initial_king_health = self.king.health
        initial_enemy_health = self.enemy.health
        self.king.defend(self.enemy)
        # King should counter-attack with poison (10 damage)
        expected_enemy_health = initial_enemy_health - 10
        self.assertEqual(self.enemy.health, expected_enemy_health)

    @patch('random.random', return_value=0.9)  # Force normal defense
    def test_normal_defense_takes_damage(self, mock_random):
        """Test that king takes damage when not using special defense"""
        initial_health = self.king.health
        self.king.defend(self.enemy)
        # King should take normal damage
        expected_health = initial_health - self.enemy.damage
        self.assertEqual(self.king.health, expected_health)

    @patch('random.random', return_value=0.1)  # Force special defense
    def test_poison_counter_deals_10_damage(self, mock_random):
        """Test that poison counter deals exactly 10 damage"""
        initial_health = self.enemy.health
        self.king.special_defense(self.enemy)
        damage_dealt = initial_health - self.enemy.health
        self.assertEqual(damage_dealt, 10)


if __name__ == '__main__':
    unittest.main()
