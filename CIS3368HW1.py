fish_details = []

def add_fish():
    superclass = input("Enter the superclass of the fish: ")
    species = input("Enter the species of the fish: ")
    color = input("Enter the color of the fish: ")
    acquired = input("Enter the acquired of the fish: ")
    alive = input("Enter the alive of the fish: ")



    fish_details.append({ "species": species, "color": color, acquired:"acquired", alive:"alive"})

def output_fish():
    for fish in fish_details:
        print(f"Species: {fish['species']}, Color: {fish['color']}, Acquired: {fish['acquired']}, Alive: {fish['alive']}")

def show_menu():
    print("\nMENU")
    print("a - Add fish")
    print("o - Output all fish in console")
    print("q - Quit")
    choice = input("Enter your choice: ").lower()
    if choice == 'a':
        add_fish()
    elif choice == 'o':
        output_fish()
    elif choice == 'q':
        return
    else:
        print("Invalid choice, please try again.")

while True:
    show_menu()
    if len(fish_details) == 0:
        continue
    break
