from character import Character
import random

class Soldier(Character):
    def attack(self, defender):
        if random.random() < self.special_attack_chance:
            self.special_attack(defender)
        else:
            super().attack(defender)

    def special_attack(self, defender):
        bonus_damage = 10
        msg = f"{self.name.capitalize()} performs a wonderful slash with +{bonus_damage} bonus damage!"
        self.display(msg, tag="blue")
        defender.take_damage(self.damage + bonus_damage)