def healing_potion() -> str:
    earth = create_earth()
    water = create_water()
    return (f"Healing potion brewed with '{earth}'"
           f"and '{water}'")


def strength_potion() -> str:
    fire = create_fire()
    water = create_water()
    return "Strength potion brewed with '{fire}' and '{water}'"
