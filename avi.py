import random

class AviatorGame:
    def __init__(self):
        self.player_name = ""
        self.missions_completed = 0
        self.weather_conditions = ["sunny", "rainy", "stormy", "foggy"]
        self.player_aircraft = Aircraft()

    def start_game(self):
        print("Welcome to Sky Wings!")
        self.player_name = input("Enter your pilot name: ")
        print(f"Welcome, {self.player_name}! Let's start flying.")

        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice == "1":
                self.start_mission()
            elif choice == "2":
                print(f"{self.player_name}, your current aircraft:")
                self.player_aircraft.display_info()
            elif choice == "3":
                print("Exiting the game. Thanks for playing!")
                break
            else:
                print("Invalid choice. Please try again.")

    def display_menu(self):
        print("\nMain Menu:")
        print("1. Start Mission")
        print("2. Check Aircraft")
        print("3. Quit")

    def start_mission(self):
        print("\nStarting a new mission...")
        mission_weather = random.choice(self.weather_conditions)
        print(f"Current weather: {mission_weather}")
        # Implement mission logic here
        self.missions_completed += 1
        print("Mission completed!")

class Aircraft:
    def __init__(self):
        self.name = "Skyhawk"
        self.speed = 300
        self.capacity = 1
        self.weapon = "Machine Gun"

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Speed: {self.speed} km/h")
        print(f"Capacity: {self.capacity}")
        print(f"Weapon: {self.weapon}")


if __name__ == "__main__":
    game = AviatorGame()
    game.start_game()
