from character import Character
import random

class King(Character):
    def attack(self, defender):
        if random.random() < self.special_attack_chance:
            self.super_attack(defender)
        else:
            super().attack(defender)

    def defend(self, attacker):
        if random.random() < self.special_defense_chance:
            self.special_defense(attacker)
        else:
            super().defend(attacker)

    def super_attack(self, defender):
        msg = f"{self.name.capitalize()} is using his super chess board!"
        self.display(msg, tag="red")
        defender.take_damage(20)

    def special_defense(self, attacker):
        poison_damage = 10
        msg = f"{self.name.capitalize()} counter-attacks with poison! {attacker.name.capitalize()} loses {poison_damage} health instantly."
        self.display(msg, tag="green")
        attacker.take_damage(poison_damage)