"""
Interactive Story Game

Choose your path and reach different endings.

Usage:
Run script and input choices.

"""

def start():
    print("You wake up in a dark forest. Do you:")
    print("1) Follow the light")
    print("2) Walk into the darkness")

    choice = input("> ")
    if choice == '1':
        light_path()
    elif choice == '2':
        dark_path()
    else:
        print("Invalid choice.")
        start()

def light_path():
    print("You find a friendly village. Do you:")
    print("1) Stay and rest")
    print("2) Explore further")

    choice = input("> ")
    if choice == '1':
        print("You live happily in the village. The End.")
    elif choice == '2':
        print("You discover a hidden treasure. The End.")
    else:
        print("Invalid choice.")
        light_path()

def dark_path():
    print("You encounter a wild beast. Do you:")
    print("1) Fight")
    print("2) Run")

    choice = input("> ")
    if choice == '1':
        print("You bravely defeat the beast! The End.")
    elif choice == '2':
        print("You escape safely. The End.")
    else:
        print("Invalid choice.")
        dark_path()

if __name__ == "__main__":
    start()
