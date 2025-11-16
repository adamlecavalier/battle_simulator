import json
import random
from character import Character
from type_map import type_map


def battle_round(attacker, defender):
    attacker.attack(defender)
    if defender.is_alive():
        defender.attack(attacker)

def main():
    with open("character.json", "r") as f:
        data = json.load(f)

    selected = random.sample(data, 2)
    characters = [
        type_map.get(char.get("name"), Character)(**char)
        for char in selected
    ]
    
    print("Welcome to the Combat Simulator!\n")

    for c in characters:
        print(f"{c.name.capitalize()} - Health : {c.health}, Damage : {c.damage}")
    print("\nLet the games begin!")

    round_num = 1
    
    while all(c.is_alive() for c in characters):
        print(f"\n--- Round {round_num} ---")
        attacker, defender = random.sample(characters, 2)
        battle_round(attacker, defender)
        round_num += 1

    winner = next(c for c in characters if c.is_alive())
    print(f"\n{winner.name.capitalize()} wins!")

    with open("winners.txt", "a", encoding="utf-8") as f:
        f.write(f"{winner.name.capitalize()}\n")

if __name__ == "__main__":
    main()