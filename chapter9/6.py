"""Assignment
Our player is selling the items in their inventory to the shopkeep! You should see a loop that iterates over each element.

Update the loop body to pop the last element into an item variable so that the code on line 19 prints the items in turn."""

def clear_inventory():
    inventory = [
        "Healing Potion",
        "Iron Bar",
        "Kite Shield",
        "Shortsword",
        "Leather Scraps",
        "Tattered Cloth",
    ]

    print(f"inventory: {inventory}")

    # don't touch above this line

    for i in range(0, len(inventory)):
        item = inventory.pop()

        # don't touch below this line
        print(f"Selling: {item}")
        print(f"inventory: {inventory}")


def test():
    clear_inventory()   
    print("=====================================")


def main():
    test()


main()
