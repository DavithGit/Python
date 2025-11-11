#Final project (Inventory manager)
# Davith Atwater
# Programming Logic ADD-100-004L
# November 2025
"""Project Overview
"""
    
    # This program is a backpack inventory manager designed for any backpack users
    #   
    # Users can add items, remove items, and list contents, 
    # Users can also store items in specific pockets, check content of those pockets, and empty those pockets
    #
    # The data stored will be:
        # Items the user provides
        # What pocket each item is in
        # How many items there are
        # Backpack contents as a whole

    # Possible actions will be:
        # List all possible commands
        # Backpack
            # list out all contents of backpack
            # list out how many items there are in the backpack
            # empty entire backpack, say what was removed
        # Pocket
            #there will be x pockets, (first, second, third, fourth)
            # list out all contents of specific pockets
            # list out how many items there are in a specific pocket
            # add an item to a pocket
            # remove an item from a pocket
            # empty specific pocket, say what was removed
        
    # The data style will be separate dictionaries
        #I chose this because adding and removing data without mixing it up will be important
        
    # Classes:
        # Class A name: inventory_manager
            # represents whole inventory holding all items
        #Class B name: pocket
            # represents one pocket
        #Class C name: item
            # represents individual items
    # class names, getters and setters, 
class inventory_manager:
    # Represents the entire backpack inventory

    def __init__(self):
        self.__categories = {}      # dictionary of categories or pockets

    # Getters and Setters
    def get_categories(self):
        return self.__categories

    def set_categories(self, value):
        self.__categories = value


class pocket:
    # Represents one pocket or compartment in the backpack

    def __init__(self, name: str):
        self.__name = name          # pocket name
        self.__items = []           # list of items in this pocket

    # Getters and Setters
    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value

    def get_items(self):
        return self.__items

    def set_items(self, value):
        self.__items = value


class item:
    # Represents a single item stored in the backpack

    def __init__(self, name: str, value: float):
        self.__name = name          # item name
        self.__value = value        # item value in dollars

    # Getters and Setters
    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value

    def get_value(self):
        return self.__value

    def set_value(self, value):
        self.__value = value

def initialize_inventory():
    # creates inventory with default pockets
    inv = inventory_manager()
    for p in ["First Pocket", "Second Pocket", "Third Pocket", "Fourth Pocket"]:
        inv.add_pocket(p)
    return inv


def display_menu():
    print("\n=== Backpack Inventory Manager ===")
    print("1. Add item to pocket")
    print("2. Remove item from pocket")
    print("3. List all backpack contents")
    print("4. List items in a specific pocket")
    print("5. Empty a pocket")
    print("6. Empty entire backpack")
    print("7. Save inventory to file")
    print("8. Load inventory from file")
    print("9. Quit")


def get_user_choice():
    while True:
        try:
            choice = int(input("Enter your choice (1-9): "))
            if 1 <= choice <= 9:
                return choice
            else:
                print("Choice must be between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def add_item_to_pocket(inventory):
    pocket_name = input("Enter pocket name: ").title()
    inventory.add_pocket(pocket_name)
    item_name = input("Enter item name: ").title()
    try:
        value = float(input("Enter item value ($): "))
    except ValueError:
        print("Invalid value entered. Item not added.")
        return
    new_item = item(item_name, value)
    target_pocket = inventory.get_pocket(pocket_name)
    target_pocket.add_item(new_item)
    print(f"Added {item_name} to {pocket_name}.")


def remove_item_from_pocket(inventory):
    pocket_name = input("Enter pocket name: ").title()
    target_pocket = inventory.get_pocket(pocket_name)
    if not target_pocket:
        print("That pocket does not exist.")
        return
    item_name = input("Enter item name to remove: ").title()
    removed = target_pocket.remove_item(item_name)
    if removed:
        print(f"Removed {removed.get_name()} from {pocket_name}.")
    else:
        print("Item not found in that pocket.")


def list_all_items(inventory):
    items = inventory.list_all_items()
    if not items:
        print("Backpack is empty.")
        return
    print("\nAll backpack contents:")
    for pocket_name, itm in items:
        print(f"{pocket_name}: {itm}")


def list_pocket_items(inventory):
    pocket_name = input("Enter pocket name: ").title()
    target_pocket = inventory.get_pocket(pocket_name)
    if not target_pocket:
        print("That pocket does not exist.")
        return
    items = target_pocket.get_items()
    if not items:
        print(f"{pocket_name} is empty.")
    else:
        print(f"\nItems in {pocket_name}:")
        for itm in items:
            print(f"- {itm}")


def empty_pocket(inventory):
    pocket_name = input("Enter pocket name to empty: ").title()
    target_pocket = inventory.get_pocket(pocket_name)
    if not target_pocket:
        print("That pocket does not exist.")
        return
    removed = target_pocket.empty_pocket()
    if removed:
        print(f"Emptied {pocket_name}. Removed items:")
        for itm in removed:
            print(f"- {itm}")
    else:
        print(f"{pocket_name} was already empty.")


def empty_entire_backpack(inventory):
    removed = inventory.empty_all()
    if not removed:
        print("Backpack already empty.")
    else:
        print("Backpack emptied. Removed items:")
        for itm in removed:
            print(f"- {itm}")


def save_inventory_to_file(inventory, filename="inventory.txt"):
    try:
        with open(filename, "w") as f:
            for pocket_name, pocket_obj in inventory.get_pockets().items():
                f.write(f"Pocket: {pocket_name}\n")
                for itm in pocket_obj.get_items():
                    f.write(f"  {itm.get_name()},{itm.get_value()}\n")
        print(f"Inventory saved to {filename}")
    except Exception as e:
        print("Error saving file:", e)


def load_inventory_from_file(inventory, filename="inventory.txt"):
    try:
        with open(filename, "r") as f:
            current_pocket = None
            for line in f:
                line = line.strip()
                if line.startswith("Pocket:"):
                    pocket_name = line.split(":", 1)[1].strip()
                    inventory.add_pocket(pocket_name)
                    current_pocket = inventory.get_pocket(pocket_name)
                elif line and current_pocket:
                    parts = line.split(",")
                    if len(parts) == 2:
                        name, value = parts[0].strip(), float(parts[1])
                        current_pocket.add_item(item(name, value))
        print(f"Inventory loaded from {filename}")
    except FileNotFoundError:
        print("File not found. Start a new inventory.")
    except Exception as e:
        print("Error loading file:", e)


def main_loop(inventory):
    while True:
        display_menu()
        choice = get_user_choice()
        if choice == 1:
            add_item_to_pocket(inventory)
        elif choice == 2:
            remove_item_from_pocket(inventory)
        elif choice == 3:
            list_all_items(inventory)
        elif choice == 4:
            list_pocket_items(inventory)
        elif choice == 5:
            empty_pocket(inventory)
        elif choice == 6:
            empty_entire_backpack(inventory)
        elif choice == 7:
            save_inventory_to_file(inventory)
        elif choice == 8:
            load_inventory_from_file(inventory)
        elif choice == 9:
            print("Goodbye!")
            break


def main():
    inventory = initialize_inventory()
    main_loop(inventory)

    
main()
