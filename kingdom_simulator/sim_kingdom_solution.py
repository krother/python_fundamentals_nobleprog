"""
Sim Kingdom
===========

The ruler of is planning to build a new enchanted castle.
Enchanted castles are a complicated matter.
You are tasked with providing enough resources, coordinating construction work.
Basically your job is running the economy of half the realm.

Actually, it is not that complicated.
Every month, you can build one facility:

* a lumber mill (costs nothing and produces 1 unit of wood per month)
* a quarry (costs 2 wood and produces 1 unit of stone per month)
* a mage tower (costs 15 stone and 10 wood and produces 1 unit of mana per month)
* an enchanted castle (costs 100 wood, 100 stone and 100 units of mana)

The ruler wants to know how many months the construction work will take?
"""

# initialize goods
wood = 0
stone = 0
mana = 0

lumber_mills = 0
quarries = 0
mage_towers = 0

castle_built = False
months = 1

buildings = ['lumber mill', 'quarry', 'mage tower', 'castle']


while not castle_built:

    # 1. print all resources
    print(f"""
Month {months:2}:
=========
you have:
{wood:4} wood
{stone:4} stone
{mana:4} mana

{lumber_mills:4} lumber mills
{quarries:4} quarries
{mage_towers:4} mage towers

Select what you want to build (and press <ENTER>):
""")

    # 2. print the menu
    counter = 1
    for name in buildings:
        print(f"[{counter}] {name}")
        counter += 1

    # 3. decide what to build
    selected = input()

    # 4. build a new building if possible
    if selected == '1':
        lumber_mills += 1
    elif selected == '2' and wood >= 2:
        quarries += 1
        wood -= 2
    elif selected == '3' and wood >= 10 and stone >= 15:
        mage_towers += 1
        wood -= 10
        stone -= 15
    elif selected == '4' and wood >= 100 and stone >= 100 and mana >= 100:
        castle_built = True
    else:
        print('not enough resources!\n')

    # 5. produce goods
    wood += lumber_mills
    stone += quarries
    mana += mage_towers

    months += 1

print(f"\nYou built the enchanted castle in {months} months.")
