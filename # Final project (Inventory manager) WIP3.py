# Final project (Inventory manager)
# Davith Atwater
# Programming Logic ADD-100-004L
# November 2025

"""Project Overview
Backpack inventory manager where users add/remove items,
store them in pockets, empty pockets, save/load, and list contents.
"""

class inventory_manager:
    def __init__(self):
        self.__categories = {}

    def get_categories(self):
        return self.__categories

    def set_categories(self, value):
        self.__categories = value

    def add_pocket(self, name):
        if name not in self.__categories:
            self.__categories[name] = pocket(name)

    def get_pocket(self, name):
        return self.__categories.get(name)

    def get_pockets(self):
        return self.__categories

    def list_all_items(self):
        all_items = []
        for p_name, p_obj in self.__categories.items():
            for itm in p_obj.get_items():
                all_items.append((p_name, itm.get_name()))
        return all_items

    def empty_all(self):
        removed = []
        for p_obj in self.__categories.values():
            removed.extend([i.get_name() for i in p_obj.get_items()])
            p_obj.set_items([])
        return removed


class pocket:
    def __init__(self, name: str):
        self.__name = name
        self.__items = []

    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value

    def get_items(self):
        return self.__items

    def set_items(self, value):
        self.__items = value

    def add_item(self, itm):
        self.__items.append(itm)

    def remove_item(self, name):
        for i in self.__items:
            if i.get_name() == name:
                self.__items.remove(i)
                return i
        return None

    def empty_pocket(self):
        removed = [i.get_name() for i in self.__items]
        self.__items = []
        return removed


class item:
    def __init__(self, name: str):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value


# ----------------------------------------------------

def initialize_inventory():
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
    print("10. Show total number of items")


def get_user_choice():
#gets user choice
    while True:
        try:
            choice = int(input("Enter your choice (1-10): "))
            if 1 <= choice <= 10:
                return choice
            else:
                print("Choice must be between 1 and 10.")
        except ValueError:
            print("Invalid input. Enter a number.")


def add_item_to_pocket(inventory):
#adds item to a specific pocket
    pocket_name = input("Enter pocket name: ").title()
    inventory.add_pocket(pocket_name)

    item_name = input("Enter item name: ").title()

    # create item with only name
    new_item = item(item_name)

    target_pocket = inventory.get_pocket(pocket_name)
    target_pocket.add_item(new_item)

    print(f"Added {item_name} to {pocket_name}.")

def remove_item_from_pocket(inventory):
#removes an item from a specific pocket
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
#lists all items in all pockets
    items = inventory.list_all_items()

    if not items:
        print("Backpack is empty.")
        return

    print("\nAll backpack contents:")
    for pocket_name, itm in items:
        print(f"{pocket_name}: {itm}")


def list_pocket_items(inventory):
#lists items in a specific  pocket
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
            print(f"- {itm.get_name()}")


def empty_pocket(inventory):
#empties a specific pocket
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
#removes all items and says what was removed
    removed = inventory.empty_all()

    if not removed:
        print("Backpack already empty.")
    else:
        print("Backpack emptied. Removed items:")
        for itm in removed:
            print(f"- {itm}")


def save_inventory_to_file(inventory, filename="inventory.txt"):
# Saves pockets with items to a text file 
    try:
        with open(filename, "w") as f:
            for pocket_name, pocket_obj in inventory.get_pockets().items():
                f.write(f"Pocket: {pocket_name}\n")
                for itm in pocket_obj.get_items():
                    f.write(f"  {itm.get_name()}\n")
        print(f"Inventory saved to {filename}")
    except Exception as e:
        print("Error saving file:", e)


def load_inventory_from_file(inventory, filename="inventory.txt"):
# Loads pocket names with items from a text file 
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
                    name = line.strip()
                    current_pocket.add_item(item(name))

        print(f"Inventory loaded from {filename}")

    except FileNotFoundError:
        print("File not found. Start a new inventory.")
    except Exception as e:
        print("Error loading file:", e)

def show_total_items(inventory):
#Calculates and displays the total number of items in all pockets.
    total = 0
    for _, pocket_obj in inventory.get_pockets().items():
        total += len(pocket_obj.get_items())
    print(f"Total items in backpack: {total}")


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
        elif choice == 10:
            show_total_items(inventory)

#added option 10 for the calculation requirement at the end so its option 10
#a little janky to have 9 be exit and 10 be something else but it works



#TODO
#DONE add a calc
#DONE docstrings
#



def main():
    inventory = initialize_inventory()
    main_loop(inventory)


main()

