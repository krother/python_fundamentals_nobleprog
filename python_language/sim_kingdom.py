"""
Kingdom Simulator
"""
# initialize resources
wood = 0
...
mana = 0

lumber_mills, quarries = 0, 0

castle_built = False
months = 1

buildings = ['lumber mill', 'quarry', 'castle']

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

Select what you want to build (and press <ENTER>):
""")

    # 2. print the menu
    counter = 1
    for name in buildings:
        ...
        counter += 1

    # 3. decide what to build
    selected = input()

    # 4. build a new building if possible
    if selected == '1':
        lumber_mills += 1
    elif selected == '2' and wood >= 2:
        ...
        wood -= 2
    elif ...:
        castle_built = True
    else:
        print('not enough resources!\n')

    # 5. produce goods
    wood += lumber_mills
    ...

print(f"\nYou built the enchanted castle in {months} months.")
