from character import Character
import random

class Mage(Character):
    def attack(self, defender):
        if random.random() < self.special_attack_chance:
            self.special_attack(defender)
        else:
            super().attack(defender)

    def defend(self, attacker):
        # if random.random() < self.special_defense_chance:
        #     self.special_defense(attacker)
        # else:
            super().defend(attacker)

    def special_attack(self, defender):
        if self.health <= 40:
            self.heal()
        else:
            self.fireball(defender)

    def fireball(self, defender):
        msg = f"{self.name.capitalize()} casts a fireball!"
        self.display(msg, tag="orange")
        defender.take_damage(self.damage + 10)

    def heal(self):
        if self.health > 0:
            self.health += 20
            msg = f"{self.name.capitalize()} heals and now has {self.health} health!"
            self.display(msg, tag="green")
