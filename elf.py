from character import Character
import random

class Elf(Character):
    def defend(self, attacker):
        if random.random() < 0.4:
            self.dodge()
        else:
            super().defend(attacker)

    def dodge(self):
        msg = f"{self.name.capitalize()} dodges the attack gracefully!"
        self.display(msg, tag="blue")