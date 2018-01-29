"""

Write a function named displayInventory that would take any possible inventory and display it like the following

#You are creating a fantasy video game. The data structure to model the player's inventory will be a dictionary where the keys are string values
# #describing the item in the inventory and the value is an integer value detailing how many of that item the player has. For example, the dictionary 
# #value {'rope: 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} means the player has 1 rope, 6 torches, 42 gold coins, and so on.


Inventory:
12 arrow
42 gold coin
1 rope
6 torch
1 dagger
Total number of items: 62
"""
print ("\nPart 1 of Challenge\n")

inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}



def displayInventory(inventory):
    count = 0
    for item, num in inventory.items():
        count += num
        print ("%i %s" % (num, item))
    print ("Total number of items: %i" % count)

displayInventory(inventory)

"""
Imagine that a vanquished dragon's loot is represented as a list of strings like this:


dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
Write a function named addToInventory(inventory, addedItems), where the inventory parameter is a dictionary representing the player's inventory (like in the previous project) and the addedItems parameter is a list like dragonLoot. The addToInventory() function should return a dictionary that represents the updated inventory. Note that the addedItems list can contain multiples of the same item. Your code could look something like this:


def addToInventory(inventory, addedItems):
    # your code goes here

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
The previous program (with your displayInventory() function from the previous project) would output the following:


Inventory:
45 gold coin
1 rope
1 ruby
1 dagger

Total number of items: 48
"""
print ("\n\nPart 2 of Challenge\n")

def addToInventory(inventory, addedItems):
    inv_items = inventory.values()
    for item in addedItems:
        inventory[item] = inventory.get(item,0) + 1
    return inventory
    

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

inv = addToInventory(inv, dragonLoot)

displayInventory(inv)