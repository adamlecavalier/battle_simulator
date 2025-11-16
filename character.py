class Character:
    def __init__(self, name, health, damage, weapon,
                special_attack_chance, special_defense_chance, image):
        self.name = name
        self.health = health
        self.damage = damage
        self.weapon = weapon
        self.special_attack_chance = special_attack_chance
        self.special_defense_chance = special_defense_chance
        self.image = image
        
            
    def attack(self, defender):
        msg = f"{self.name.capitalize()} attacks the {defender.name} with his {self.weapon}!"
        self.display(msg)
        defender.defend(self)

    def defend(self, attacker):
        self.take_damage(attacker.damage)

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.health = 0
        msg = f"{self.name.capitalize()} takes {amount} damage! Health is now {self.health}."
        self.display(msg)
        if self.health == 0:
            self.display(f"{self.name.capitalize()} is dead")
    
    def display(self, msg, tag=None):
        print(msg)
        if hasattr(self, "output_func"):
            if tag:
                self.output_func(msg, tag)
            else:
                self.output_func(msg)

    def is_alive(self):
        return self.health > 0