from alchemy import create_air


def main():
    print("=== Alembic 5 ===")
    print("Accessing the alchemy module using "
          "'from ... import ...'")
    air = create_air()
    print(f"Testing create_air: {air}")


if __name__ == "__main__":
    main()
