def roll_call_dwarves(stuff):
    i = 1
    for each in stuff:
        print(f"{i}. {each}")
        i += 1

def summon_captain_planet(stuff):
    printing = []
    for each in stuff:
        x = each.capitalize()
        printing.append(f"{x}!")
    return printing

def long_planeteer_calls(stuff):
    stuff.sort(key=len, reverse=True)
    if len(stuff[0]) > 4:
        return True
    elif len(stuff[0]) <= 4:
        return False

def find_the_cheese(words):
    if "cheddar" in words:
        return "cheddar"
    elif "gouda" in words:
        return "gouda"
    elif "camambert" in words:
        return "camambert"
    else:
        return None
