from alchemy import elements


def main() -> None:
    print("=== Alembic 3 ===")
    print("Accessing alchemy/elements.py"
          " using 'from ... import ...' structure")
    air = elements.create_air()
    print(f"Testing create_air: {air}")


if __name__ == "__main__":
    main()
