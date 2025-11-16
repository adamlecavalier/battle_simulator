import tkinter as tk
from tkinter import messagebox
import random
import json
from main import Character
from type_map import type_map
from PIL import Image, ImageTk

class CombatGUI:
    def __init__(self, master):
        # master is the parent widget
        self.master = master
        master.title("Combat Simulator")

        # Frame du haut pour les images
        self.top_frame = tk.Frame(master)
        self.top_frame.pack(side=tk.TOP, fill=tk.X)

        # Frame du bas pour les événements
        self.bottom_frame = tk.Frame(master)
        self.bottom_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        # Placeholders pour les images des combattants
        self.left_image_label = tk.Label(self.top_frame)
        self.left_image_label.pack(side=tk.LEFT, padx=20, pady=10)
        self.right_image_label = tk.Label(self.top_frame)
        self.right_image_label.pack(side=tk.RIGHT, padx=20, pady=10)

        # Zone de texte pour les événements
        self.text = tk.Text(self.bottom_frame, width=60, height=20)
        self.text.pack(fill=tk.BOTH, expand=True)

        self.start_button = tk.Button(master, text="Start a combat", command=self.start_battle, font = ("Old English Text MT", 14))
        self.start_button.pack()
        
        self.text.insert(tk.END, "Welcome to Combat Simulator!\n")
        print("Welcome to the Combat Simulator!\n")


        self.text.tag_config("green", foreground="green")
        self.text.tag_config("red", foreground="red")
        self.text.tag_config("blue", foreground="blue")
        self.text.tag_config("orange", foreground="orange")

    def start_battle(self):
        self.text.delete(1.0, tk.END)
        with open("character.json", "r") as f:
            data = json.load(f)
            
        selected = random.sample(data, 2)
        characters = [
            type_map.get(char.get("name"), Character)(**char)
            for char in selected
        ]
                        
        for c in characters:
            c.output_func = lambda msg, tag=None: self.text.insert(tk.END, msg + "\n", tag) if tag else self.text.insert(tk.END, msg + "\n")
            self.text.insert(tk.END, f"{c.name.capitalize()} - Health : {c.health}, Damage : {c.damage}\n")
        self.text.insert(tk.END, "\nLet the games begin!\n")

        left_img = Image.open(characters[0].image)
        right_img = Image.open(characters[1].image)
        left_img = left_img.resize((100, 100))
        right_img = right_img.resize((100, 100))
        self.left_photo = ImageTk.PhotoImage(left_img)
        self.right_photo = ImageTk.PhotoImage(right_img)
        self.left_image_label.config(image=self.left_photo)
        self.right_image_label.config(image=self.right_photo)

        round_num = 1
        
        while all(c.is_alive() for c in characters):
            print(f"\n--- Round {round_num} ---\n")
            self.text.insert(tk.END, f"\n--- Round {round_num} ---\n")
            attacker, defender = random.sample(characters, 2)
            attacker.attack(defender)
            if defender.is_alive():
                defender.attack(attacker)
            self.text.insert(tk.END, "\n")
            for c in characters:
                self.text.insert(tk.END, f"{c.name.capitalize()} - Health : {c.health}\n")
            round_num += 1

        winner = next(c for c in characters if c.is_alive())
        self.text.insert(tk.END, f"\n{winner.name.capitalize()} wins!\n")
        print(f"\n{winner.name.capitalize()} wins!\n")
        with open("winners.txt", "a", encoding="utf-8") as f:
            f.write(f"{winner.name.capitalize()}\n")        

if __name__ == "__main__":
    root = tk.Tk()
    gui = CombatGUI(root)
    root.mainloop()