import requests

class Pokemon:
    def __init__(self, name):
        self.name = name.lower()
        self.abilities = []
        self.selected_ability = None
        self.moves = []
        self.available_moves = []
        self.types = []
        self.weaknesses = []
        self.resistances = []
        self.immunities = []
        self.strengths = []

# Gets data from API
    def fetch_data(self):
        """Fetch Pokémon details from PokeAPI."""
        url = f"https://pokeapi.co/api/v2/pokemon/{self.name}"
        response = requests.get(url)

    # Gets Ability Name, Type Name, and Move Name
        if response.status_code == 200:
            data = response.json()
            self.abilities = [ability['ability']['name'] for ability in data['abilities']]
            self.types = [ptype['type']['name'] for ptype in data['types']]
            self.available_moves = [move['move']['name'] for move in data['moves']]
            self.get_type_effectiveness()
            return True
        else:
            print(f"Error: Pokémon '{self.name}' not found. Please try again.") # Error if pokemon is not enter correctly
            return False

    # Gets Effectiveness
    def get_type_effectiveness(self):
        """Retrieves type effectiveness based on Pokémon type(s)."""
        self.weaknesses = []
        self.resistances = []
        self.immunities = []
        self.strengths = []

        for ptype in self.types:
            url = f"https://pokeapi.co/api/v2/type/{ptype}"
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                self.immunities.extend([entry['name'] for entry in data['damage_relations']['no_damage_from']])
                self.resistances.extend([entry['name'] for entry in data['damage_relations']['half_damage_from']])
                self.weaknesses.extend([entry['name'] for entry in data['damage_relations']['double_damage_from']])
                self.strengths.extend([entry['name'] for entry in data['damage_relations']['double_damage_to']])

    # Gets abilities from pokemon
    def choose_ability(self):
        """Allows the user to choose an ability."""
        if len(self.abilities) == 1:
            self.selected_ability = self.abilities[0]
            print(f"{self.name.capitalize()} has only one ability: {self.selected_ability}. It has been selected automatically.")
        else:
            print(f"\nChoose an ability for {self.name.capitalize()}:")
            for idx, ability in enumerate(self.abilities, 1):
                print(f"{idx}. {ability}")

            while True:
                choice = input("Enter the number of the ability you want to select: ")
                if choice.isdigit() and 1 <= int(choice) <= len(self.abilities):
                    self.selected_ability = self.abilities[int(choice) - 1]
                    print(f"Selected ability: {self.selected_ability}")
                    break
                else:
                    print("Invalid choice. Please enter a valid number.")

    # Gets moveset list
    def choose_moves(self):
        """Allows the user to choose four moves for the Pokémon."""
        print(f"\nAvailable moves for {self.name.capitalize()}:")
        for idx, move in enumerate(self.available_moves, 1):
            print(f"{idx}. {move}")

        while len(self.moves) < 4:
            move_choice = input(f"Select move {len(self.moves) + 1} (type the move name): ").lower()
            if move_choice in self.available_moves and move_choice not in self.moves:
                self.moves.append(move_choice)
                print(f"Move '{move_choice}' added!")
            elif move_choice in self.moves:
                print("You already selected this move. Choose a different one.")
            else:
                print("Invalid move. Please enter a move from the available list.")

class PokemonTeam:
    def __init__(self, name):
        self.name = name
        self.pokemon_list = []
    # After team is created User gets to add pokemon immediately
    def add_pokemon(self):
        """Adds a Pokémon to the team (immediately after team creation)."""
        if len(self.pokemon_list) >= 6:
            print("Team is full. Cannot add more Pokémon.")
            return

        while True:
            pokemon_name = input("Enter the name of a Pokémon to add (or type 'done' to finish): ").lower() # Enter Pokemon name
            if pokemon_name == 'done':
                break

            new_pokemon = Pokemon(pokemon_name)
            if new_pokemon.fetch_data():
                new_pokemon.choose_ability()
                new_pokemon.choose_moves()
                self.pokemon_list.append(new_pokemon)
                print(f"{new_pokemon.name.capitalize()} added to team '{self.name}' with ability '{new_pokemon.selected_ability}' and moves: {', '.join(new_pokemon.moves)}!")

    # Shows team
    def show_team(self):
        """Displays the team's Pokémon."""
        if not self.pokemon_list:
            print(f"Team '{self.name}' has no Pokémon yet.")
            return

        print(f"\nTeam '{self.name}' Pokémon:")
        for idx, pokemon in enumerate(self.pokemon_list, 1):
            print(f"{idx}. {pokemon.name.capitalize()} (Types: {', '.join(pokemon.types)})")
            print(f"   Ability: {pokemon.selected_ability}")
            print(f"   Moves: {', '.join(pokemon.moves) if pokemon.moves else 'No moves selected'}")
            print(f"   Weaknesses: {', '.join(pokemon.weaknesses) if pokemon.weaknesses else 'None'}")
            print(f"   Strengths: {', '.join(pokemon.strengths) if pokemon.strengths else 'None'}")
            print("-" * 40)

# Manage Team Menu
def manage_team(team):
    while True:
        print("\nManage Team Menu:")
        print("1. View Pokémon on Team")
        print("2. Add Pokémon to Team (if space available)")
        print("3. Remove Pokémon from Team")
        print("4. Add Moves to a Pokémon")
        print("5. Remove Moves from a Pokémon")
        print("6. Return to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            team.show_team()

        elif choice == "2":
            team.add_pokemon()

        elif choice == "3":
            team.show_team()
            if not team.pokemon_list:
                print("No Pokémon in the team to remove.") # Shows no pokemon in team
                continue

            selection = input("Enter the Pokémon name to remove: ").strip().lower() # Removes pokemon selected
            team.pokemon_list = [pokemon for pokemon in team.pokemon_list if pokemon.name != selection]
            print(f"{selection.capitalize()} removed from the team.")

        elif choice == "4":  # Add Moves
            team.show_team()
            selection = input("Enter Pokémon name to add moves: ").strip().lower()
            found_pokemon = next((p for p in team.pokemon_list if p.name == selection), None)
            if found_pokemon:
                found_pokemon.choose_moves()
            else:
                print("Invalid selection.")

        elif choice == "5":  # Remove Moves
            team.show_team()
            selection = input("Enter Pokémon name to remove moves: ").strip().lower()
            found_pokemon = next((p for p in team.pokemon_list if p.name == selection), None)
            if found_pokemon and found_pokemon.moves:
                print(f"Current moves: {', '.join(found_pokemon.moves)}")
                move_to_remove = input("Enter move to remove: ").strip().lower()
                if move_to_remove in found_pokemon.moves:
                    found_pokemon.moves.remove(move_to_remove)
                    print(f"Move '{move_to_remove}' removed.")
                else:
                    print("Invalid move.")
            else:
                print("No moves available to remove.")

        elif choice == "6":
            break

# Main menu
def main():
    teams = {}

    while True:
        print("\n--- Pokémon Team Builder ---")
        print("1. Create a Team")
        print("2. View Teams")
        print("3. Manage a Team")
        print("4. Delete a Team")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            team_name = input("Enter team name: ") # Create team
            teams[team_name] = PokemonTeam(team_name)
            teams[team_name].add_pokemon()

        elif choice == "2":
            if not teams:  # If there are no teams, display a message
                print("\nNo teams available. Create a team first.")
            else:
                for team in teams.values():
                    team.show_team()

        elif choice == "3":
            team_name = input("Enter team name to manage: ")
            if team_name in teams:
                manage_team(teams[team_name])
            else:
                print("Team not found.")   # If there are no teams, display a message

        elif choice == "4":
            team_name = input("Enter team name to delete: ") # Delete pokemon team
            if team_name in teams:
                del teams[team_name]
                print(f"Deleted team '{team_name}'.")
            else:
                print("Team not found.")   # If there are no teams, display a message

        elif choice == "5":
            print("Exiting Pokémon Team Builder. Goodbye!")   # Display exiting message
            break
if __name__ == "__main__":
    main()