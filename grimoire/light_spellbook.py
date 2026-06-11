import alchemy.elements
'''
import sys


if 'alchemy' in sys.modules:
    print("alchemy IS imported")
else:
    print("alchemy not imported")'''

from elements import create_water, create_fire
from alchemy.elements import create_air
from .light_validator import validate_ingredients


def light_spell_allowed_ingredients() -> list[str]:
    earth = alchemy.elements.create_earth()
    air = create_air()
    fire = create_fire()
    water = create_water()
    return [earth, air, fire, water]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    return validate_ingredients(ingredients)