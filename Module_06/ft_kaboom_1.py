from alchemy.grimoire.dark_spellbook import dark_spell_record


def main() -> None:
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    ingredients = "bats, frogs, arsenic, eyeball"
    print(f"Testing record dark spell: "
          f"{dark_spell_record('Shadow Walk', ingredients)}")


if __name__ == "__main__":
    main()
