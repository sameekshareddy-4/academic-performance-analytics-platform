from generators.departments import generate_departments


def main():

    print("=" * 60)
    print("Academic Performance Analytics Platform")
    print("=" * 60)

    generate_departments()

    print("\nDataset Generation Completed Successfully!")


if __name__ == "__main__":
    main()