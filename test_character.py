"""
Tests for the Character base class
"""
import unittest
from character import Character


class TestCharacter(unittest.TestCase):
    """Test cases for the Character class"""

    def setUp(self):
        """Set up test fixtures"""
        self.character1 = Character(
            name="test_warrior",
            health=100,
            damage=25,
            weapon="sword",
            special_attack_chance=0.3,
            special_defense_chance=0.3,
            image="assets/knight.png"
        )
        self.character2 = Character(
            name="test_defender",
            health=80,
            damage=20,
            weapon="shield",
            special_attack_chance=0.2,
            special_defense_chance=0.2,
            image="assets/knight.png"
        )

    def test_character_initialization(self):
        """Test that a character is initialized with correct attributes"""
        self.assertEqual(self.character1.name, "test_warrior")
        self.assertEqual(self.character1.health, 100)
        self.assertEqual(self.character1.damage, 25)
        self.assertEqual(self.character1.weapon, "sword")
        self.assertEqual(self.character1.special_attack_chance, 0.3)
        self.assertEqual(self.character1.special_defense_chance, 0.3)
        self.assertEqual(self.character1.image, "assets/knight.png")

    def test_is_alive_when_healthy(self):
        """Test that a character with health > 0 is alive"""
        self.assertTrue(self.character1.is_alive())

    def test_is_alive_when_dead(self):
        """Test that a character with health = 0 is not alive"""
        self.character1.health = 0
        self.assertFalse(self.character1.is_alive())

    def test_take_damage_reduces_health(self):
        """Test that taking damage reduces health correctly"""
        initial_health = self.character1.health
        damage_amount = 30
        self.character1.take_damage(damage_amount)
        self.assertEqual(self.character1.health, initial_health - damage_amount)

    def test_take_damage_cannot_go_below_zero(self):
        """Test that health doesn't go below 0"""
        self.character1.take_damage(150)  # More than current health
        self.assertEqual(self.character1.health, 0)
        self.assertFalse(self.character1.is_alive())

    def test_attack_calls_defender_defend(self):
        """Test that attack method calls defend on the defender"""
        initial_defender_health = self.character2.health
        self.character1.attack(self.character2)
        # After attack, defender should have taken damage
        self.assertLess(self.character2.health, initial_defender_health)

    def test_defend_reduces_health(self):
        """Test that defend method reduces health"""
        initial_health = self.character2.health
        self.character2.defend(self.character1)
        self.assertEqual(self.character2.health, initial_health - self.character1.damage)

    def test_multiple_attacks(self):
        """Test that multiple attacks accumulate damage"""
        initial_health = self.character2.health
        self.character1.attack(self.character2)
        self.character1.attack(self.character2)
        expected_health = initial_health - (self.character1.damage * 2)
        self.assertEqual(self.character2.health, expected_health)

    def test_character_death_after_sufficient_damage(self):
        """Test that character dies after taking enough damage"""
        # Deal enough damage to kill the character
        self.character2.take_damage(100)
        self.assertFalse(self.character2.is_alive())
        self.assertEqual(self.character2.health, 0)


if __name__ == '__main__':
    unittest.main()
