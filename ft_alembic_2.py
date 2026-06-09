import alchemy


def main() -> None:
    print("=== Alembic 3 ===")
    print("Accessing alchemy/elements.py"
          " using 'import ...' structure")
    earth = alchemy.elements.create_earth()
    print(f"Testing create_air: {earth}")


if __name__ == "__main__":
    main()
