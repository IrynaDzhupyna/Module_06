import alchemy

def main() -> None:
    print("=== Distillation 1 ===")
    print("Using: 'import alchemy' structure to access potions")
    print("Testing strength_potion: ", end='')
    print(f"{alchemy.potions.strength_potion()}")
    print("Testing heal alias: ", end='')
    print(f"{alchemy.heal()}")


if __name__ == "__main__":
    main()