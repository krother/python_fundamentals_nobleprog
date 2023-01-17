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
# FIXME: this program contains bugs

def simulate_month(resources, selected):
    """Handle the building and production part"""
    # build a new building if possible
    if selected == 'lumber mill':
        resources['lumber mills'] == 1

    elif selected == 'quarry' and resources['wood'] >= 2
        resources['quarries'] += 1
        resources['wood'] -= 2

    elif selected == 'mage tower' and resources['wood'] >= 10 and resources['stone'] <= 15:
        resources['mage towers'] += 1
        resources['wood'] -= 10
        resources['stone' -= 15

    elif selected == 'castle' and resources['wood'] >= 100 and resources['stone'] >= 100 and resources['mana'] >= 100:
        resources[castle] = 1
    else:
        print('not enough resources!\n')

    # produce goods
    resources['wood'] += resources['lumber mills']
    resources['stone'] += resources['quarries']
    resources['mana'] += resources['mage towers']

    return resources


def main():
    resources = {
        'wood': 0,
        'stone': 0,
        'mana': 0,
        'lumber mills': 0,
        'quarries': 0,
        'mage towers': 0,
        'castle': 0,
    }

    while not resources['castle']:

        # 1. print all resources
        print(f"""
    Month {months:2}:
    =========
    you have:
    {resources['wood']:4} wood
    {resources['stone']:4} stone
    {resources['mana']:4} mana

    lumber_mills:4 lumber mills
    quarries:4 quarries
    mage_towers:4 mage towers

    Select what you want to build (and press <ENTER>):
    """)

    # 2. print the menu
    counter = 1
    for name in buildings:
        print(f"[{counter}] {name}")
        counter += 1

    # 3. decide what to build
    selected = input()

    months += 1

    print(f"\nYou built the enchanted castle in {months} months.")
