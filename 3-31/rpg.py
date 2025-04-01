import random
import time
import sys
import json
import os

class Player:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.max_health = 100
        self.health = 100
        self.attack = 10
        self.defense = 5
        self.exp = 0
        self.gold = 10
        self.inventory = []
        self.potions = 2

    def display_stats(self):
        print(f"\n=== {self.name}'s Stats ===")
        print(f"Level: {self.level}")
        print(f"Health: {self.health}/{self.max_health}")
        print(f"Attack: {self.attack}")
        print(f"Defense: {self.defense}")
        print(f"Experience: {self.exp}")
        print(f"Gold: {self.gold}")
        print(f"Potions: {self.potions}")
        print(f"Inventory: {', '.join(self.inventory) if self.inventory else 'Empty'}")

    def level_up(self):
        self.level += 1
        self.max_health += 20
        self.health = self.max_health
        self.attack += 5
        self.defense += 2
        print(f"\n🎉 LEVEL UP! 🎉")
        print(f"{self.name} is now level {self.level}!")
        print(f"Health +20 | Attack +5 | Defense +2")

    def use_potion(self):
        if self.potions > 0:
            heal_amount = 50
            self.potions -= 1
            self.health = min(self.health + heal_amount, self.max_health)
            print(f"\nYou used a health potion and recovered {heal_amount} health!")
            print(f"Current health: {self.health}/{self.max_health}")
            print(f"Potions remaining: {self.potions}")
            return True
        else:
            print("\nYou don't have any potions left!")
            return False

    # Convert player data to dictionary for saving
    def to_dict(self):
        return {
            "name": self.name,
            "level": self.level,
            "max_health": self.max_health,
            "health": self.health,
            "attack": self.attack,
            "defense": self.defense,
            "exp": self.exp,
            "gold": self.gold,
            "inventory": self.inventory,
            "potions": self.potions
        }

    # Load player data from dictionary
    @classmethod
    def from_dict(cls, data):
        player = cls(data["name"])
        player.level = data["level"]
        player.max_health = data["max_health"]
        player.health = data["health"]
        player.attack = data["attack"]
        player.defense = data["defense"]
        player.exp = data["exp"]
        player.gold = data["gold"]
        player.inventory = data["inventory"]
        player.potions = data["potions"]
        return player


class Enemy:
    def __init__(self, name, level, health, attack, defense, exp_reward, gold_reward):
        self.name = name
        self.level = level
        self.health = health
        self.max_health = health
        self.attack = attack
        self.defense = defense
        self.exp_reward = exp_reward
        self.gold_reward = gold_reward

    def display_stats(self):
        print(f"\n=== {self.name} (Level {self.level}) ===")
        print(f"Health: {self.health}/{self.max_health}")
        print(f"Attack: {self.attack}")
        print(f"Defense: {self.defense}")


class Game:
    def __init__(self):
        self.player = None
        self.running = True
        self.save_directory = "saves"
        self.enemies = [
            {"name": "Goblin", "level": 1, "health": 50, "attack": 8, "defense": 2, "exp": 20, "gold": 5},
            {"name": "Wolf", "level": 2, "health": 75, "attack": 12, "defense": 3, "exp": 30, "gold": 8},
            {"name": "Bandit", "level": 3, "health": 100, "attack": 15, "defense": 5, "exp": 45, "gold": 12},
            {"name": "Orc", "level": 4, "health": 130, "attack": 18, "defense": 8, "exp": 60, "gold": 15},
            {"name": "Troll", "level": 5, "health": 180, "attack": 22, "defense": 10, "exp": 80, "gold": 20},
            {"name": "Dragon", "level": 10, "health": 300, "attack": 35, "defense": 20, "exp": 200, "gold": 100}
        ]
        self.shop_items = [
            {"name": "Rusty Sword", "type": "weapon", "bonus": 5, "cost": 20},
            {"name": "Steel Sword", "type": "weapon", "bonus": 10, "cost": 50},
            {"name": "Knight's Blade", "type": "weapon", "bonus": 15, "cost": 100},
            {"name": "Leather Armor", "type": "armor", "bonus": 5, "cost": 25},
            {"name": "Chain Mail", "type": "armor", "bonus": 10, "cost": 60},
            {"name": "Plate Armor", "type": "armor", "bonus": 15, "cost": 120},
            {"name": "Health Potion", "type": "potion", "bonus": 1, "cost": 15}
        ]
        
        # Create saves directory if it doesn't exist
        if not os.path.exists(self.save_directory):
            os.makedirs(self.save_directory)

    def slow_print(self, text, delay=0.03):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

    def start_game(self):
        self.slow_print("\n=== WELCOME TO PYTHON RPG ===", 0.05)
        time.sleep(0.5)
        
        print("\n1. New Game")
        print("2. Load Game")
        print("3. Quit")
        
        choice = input("\nSelect an option: ")
        
        if choice == "1":
            self.new_game()
        elif choice == "2":
            self.load_game_menu()
        elif choice == "3":
            print("Goodbye!")
            return
        else:
            print("Invalid choice. Starting new game...")
            self.new_game()
            
        # Main game loop
        self.main_menu()

    def new_game(self):
        self.slow_print("\nYou find yourself at the edge of a mysterious land filled with dangers and treasures...")
        time.sleep(0.5)
        
        player_name = input("\nWhat is your name, brave adventurer? ")
        self.player = Player(player_name)
        
        self.slow_print(f"\nWelcome, {player_name}! Your adventure begins now!")
        time.sleep(1)

    def main_menu(self):
        while self.running:
            print("\n=== MAIN MENU ===")
            print("1. Explore")
            print("2. Visit Shop")
            print("3. Rest")
            print("4. Check Stats")
            print("5. Save Game")
            print("6. Quit Game")
            
            choice = input("\nWhat would you like to do? ")
            
            if choice == "1":
                self.explore()
            elif choice == "2":
                self.shop()
            elif choice == "3":
                self.rest()
            elif choice == "4":
                self.player.display_stats()
            elif choice == "5":
                self.save_game()
            elif choice == "6":
                self.quit_game()
            else:
                print("\nInvalid choice. Please try again.")

    def save_game(self):
        if not self.player:
            print("No player data to save!")
            return
            
        # Create the save file name
        save_file = f"{self.player.name.lower().replace(' ', '_')}.json"
        save_path = os.path.join(self.save_directory, save_file)
        
        # Convert player data to a dictionary
        save_data = self.player.to_dict()
        
        try:
            with open(save_path, "w") as f:
                json.dump(save_data, f, indent=4)
                
            print(f"\nGame saved successfully as '{save_file}'!")
        except Exception as e:
            print(f"\nError saving game: {e}")

    def load_game_menu(self):
        # Check for save files
        save_files = []
        
        try:
            for file in os.listdir(self.save_directory):
                if file.endswith(".json"):
                    save_files.append(file)
        except:
            print("No save directory found. Creating one...")
            os.makedirs(self.save_directory)
            
        if not save_files:
            print("\nNo save files found. Starting new game...")
            self.new_game()
            return
            
        print("\n=== LOAD GAME ===")
        print("Available save files:")
        
        for i, file in enumerate(save_files, 1):
            print(f"{i}. {file[:-5]}")  # Remove .json extension
            
        print(f"{len(save_files) + 1}. Back to Main Menu")
        
        try:
            choice = int(input("\nSelect a save file to load: "))
            
            if choice == len(save_files) + 1:
                self.new_game()
                return
                
            if 1 <= choice <= len(save_files):
                self.load_game(save_files[choice - 1])
            else:
                print("Invalid choice. Starting new game...")
                self.new_game()
        except ValueError:
            print("Invalid input. Starting new game...")
            self.new_game()
    
    def load_game(self, save_file):
        save_path = os.path.join(self.save_directory, save_file)
        
        try:
            with open(save_path, "r") as f:
                save_data = json.load(f)
                
            self.player = Player.from_dict(save_data)
            print(f"\nWelcome back, {self.player.name}!")
            self.player.display_stats()
        except Exception as e:
            print(f"\nError loading save file: {e}")
            print("Starting new game...")
            self.new_game()

    def explore(self):
        self.slow_print("\nYou venture forth into the wilderness...")
        time.sleep(1)
        
        # Random chance for different events
        encounter = random.randint(1, 10)
        
        if encounter <= 7:  # 70% chance of enemy encounter
            self.enemy_encounter()
        elif encounter <= 9:  # 20% chance of finding treasure
            self.find_treasure()
        else:  # 10% chance of nothing happening
            self.slow_print("\nYou explore the area but find nothing of interest.")

    def enemy_encounter(self):
        # Choose an enemy based on player level
        suitable_enemies = [e for e in self.enemies if e["level"] <= self.player.level + 2]
        if not suitable_enemies:
            suitable_enemies = [self.enemies[0]]  # Fallback to first enemy
            
        enemy_data = random.choice(suitable_enemies)
        enemy = Enemy(
            enemy_data["name"], 
            enemy_data["level"], 
            enemy_data["health"], 
            enemy_data["attack"], 
            enemy_data["defense"],
            enemy_data["exp"],
            enemy_data["gold"]
        )
        
        self.slow_print(f"\nYou encountered a {enemy.name}!")
        time.sleep(0.5)
        
        # Battle loop
        while enemy.health > 0 and self.player.health > 0:
            enemy.display_stats()
            
            print("\n=== BATTLE MENU ===")
            print("1. Attack")
            print("2. Use Potion")
            print("3. Run Away")
            
            choice = input("\nWhat will you do? ")
            
            if choice == "1":
                self.battle_attack(enemy)
            elif choice == "2":
                if not self.player.use_potion():
                    continue  # Skip enemy turn if potion use failed
            elif choice == "3":
                escape_chance = random.randint(1, 10)
                if escape_chance <= 6:  # 60% chance to escape
                    self.slow_print("\nYou successfully escaped!")
                    return
                else:
                    self.slow_print("\nYou failed to escape!")
            else:
                print("\nInvalid choice. Please try again.")
                continue  # Skip enemy turn if input was invalid
            
            # Enemy turn (if still alive)
            if enemy.health > 0:
                self.enemy_attack(enemy)
                
        # Battle aftermath
        if self.player.health <= 0:
            self.player_death()
        else:
            self.battle_victory(enemy)

    def battle_attack(self, enemy):
        # Calculate damage
        base_damage = self.player.attack - enemy.defense // 2
        damage_variance = random.randint(-2, 5)
        damage = max(1, base_damage + damage_variance)
        
        enemy.health = max(0, enemy.health - damage)
        
        self.slow_print(f"\nYou attack the {enemy.name} for {damage} damage!")
        
        # Critical hit chance
        if random.randint(1, 10) == 10:
            crit_damage = damage // 2
            enemy.health = max(0, enemy.health - crit_damage)
            self.slow_print(f"Critical hit! You deal an additional {crit_damage} damage!")

    def enemy_attack(self, enemy):
        # Calculate damage
        base_damage = enemy.attack - self.player.defense // 2
        damage_variance = random.randint(-2, 3)
        damage = max(1, base_damage + damage_variance)
        
        self.player.health = max(0, self.player.health - damage)
        
        self.slow_print(f"\nThe {enemy.name} attacks you for {damage} damage!")
        self.slow_print(f"Your health: {self.player.health}/{self.player.max_health}")

    def battle_victory(self, enemy):
        self.slow_print(f"\nYou defeated the {enemy.name}!")
        
        # Rewards
        self.player.exp += enemy.exp_reward
        self.player.gold += enemy.gold_reward
        
        self.slow_print(f"You gained {enemy.exp_reward} experience points!")
        self.slow_print(f"You found {enemy.gold_reward} gold!")
        
        # Random chance to find a potion
        if random.randint(1, 10) <= 3:  # 30% chance
            self.player.potions += 1
            self.slow_print("You found a health potion!")
            
        # Check for level up
        exp_needed = self.player.level * 100
        if self.player.exp >= exp_needed:
            self.player.exp -= exp_needed
            self.player.level_up()

    def find_treasure(self):
        treasure_type = random.randint(1, 3)
        
        if treasure_type == 1:  # Gold
            gold_amount = random.randint(5, 20) * self.player.level
            self.player.gold += gold_amount
            self.slow_print(f"\nYou found a treasure chest containing {gold_amount} gold!")
        elif treasure_type == 2:  # Potion
            potion_count = random.randint(1, 2)
            self.player.potions += potion_count
            potion_text = "potion" if potion_count == 1 else "potions"
            self.slow_print(f"\nYou found {potion_count} health {potion_text}!")
        else:  # Random item
            if random.randint(1, 10) <= 3:  # 30% chance to find good item
                affordable_items = [item for item in self.shop_items if item["type"] != "potion"]
                if affordable_items:
                    item = random.choice(affordable_items)
                    self.slow_print(f"\nYou found a {item['name']}!")
                    self.add_item_to_player(item)
            else:
                self.slow_print("\nYou found a treasure chest, but it's empty!")

    def shop(self):
        self.slow_print("\nWelcome to the shop! What would you like to buy?")
        
        while True:
            print(f"\nYour gold: {self.player.gold}")
            print("\n=== SHOP INVENTORY ===")
            
            for i, item in enumerate(self.shop_items, 1):
                bonus_text = f"+{item['bonus']} Attack" if item['type'] == 'weapon' else f"+{item['bonus']} Defense" if item['type'] == 'armor' else "Health Potion"
                print(f"{i}. {item['name']} - {bonus_text} - {item['cost']} gold")
                
            print(f"{len(self.shop_items) + 1}. Exit Shop")
            
            try:
                choice = int(input("\nEnter the number of the item you wish to buy: "))
                
                if choice == len(self.shop_items) + 1:
                    self.slow_print("\nThank you for visiting! Come again soon!")
                    return
                    
                if 1 <= choice <= len(self.shop_items):
                    selected_item = self.shop_items[choice - 1]
                    
                    if self.player.gold >= selected_item["cost"]:
                        self.player.gold -= selected_item["cost"]
                        
                        if selected_item["type"] == "potion":
                            self.player.potions += 1
                            self.slow_print(f"\nYou bought a Health Potion! You now have {self.player.potions} potions.")
                        else:
                            self.add_item_to_player(selected_item)
                            self.slow_print(f"\nYou bought {selected_item['name']}!")
                    else:
                        self.slow_print("\nYou don't have enough gold for that item!")
                else:
                    print("\nInvalid choice. Please try again.")
            except ValueError:
                print("\nPlease enter a valid number.")

    def add_item_to_player(self, item):
        if item["type"] == "weapon":
            self.player.attack += item["bonus"]
            self.player.inventory.append(item["name"])
        elif item["type"] == "armor":
            self.player.defense += item["bonus"]
            self.player.inventory.append(item["name"])

    def rest(self):
        rest_cost = 10
        
        if self.player.gold >= rest_cost:
            self.slow_print("\nYou decide to rest at the local inn...")
            time.sleep(1)
            
            self.player.gold -= rest_cost
            self.player.health = self.player.max_health
            
            self.slow_print(f"\nYou've fully restored your health for {rest_cost} gold!")
            self.slow_print(f"Current health: {self.player.health}/{self.player.max_health}")
        else:
            self.slow_print(f"\nYou need {rest_cost} gold to rest at the inn!")

    def player_death(self):
        self.slow_print("\nYou have been defeated...")
        time.sleep(1)
        
        gold_lost = self.player.gold // 2
        self.player.gold -= gold_lost
        
        self.slow_print(f"\nYou lost {gold_lost} gold.")
        self.slow_print("You wake up at the village, barely alive.")
        
        self.player.health = self.player.max_health // 2

    def quit_game(self):
        save_prompt = input("\nDo you want to save before quitting? (y/n): ")
        
        if save_prompt.lower() == "y" or save_prompt.lower() == "yes":
            self.save_game()
        
        confirm = input("\nAre you sure you want to quit? (y/n): ")
        
        if confirm.lower() == "y" or confirm.lower() == "yes":
            self.slow_print("\nThank you for playing Python RPG! Farewell, brave adventurer!")
            self.running = False

# Start the game if this file is run directly
if __name__ == "__main__":
    game = Game()
    game.start_game()

