from core.converter import convert, convert_all
from core.display import all_text, pair_text

OPTIONS = {
    "1": ("binary", "octal"),
    "2": ("binary", "decimal"),
    "3": ("binary", "hexadecimal"),
    "4": ("binary", "character"),
    "5": ("octal", "binary"),
    "6": ("octal", "decimal"),
    "7": ("octal", "hexadecimal"),
    "8": ("octal", "character"),
    "9": ("decimal", "binary"),
    "10": ("decimal", "octal"),
    "11": ("decimal", "hexadecimal"),
    "12": ("decimal", "character"),
    "13": ("hexadecimal", "binary"),
    "14": ("hexadecimal", "octal"),
    "15": ("hexadecimal", "decimal"),
    "16": ("hexadecimal", "character"),
    "17": ("character", "binary"),
    "18": ("character", "octal"),
    "19": ("character", "decimal"),
    "20": ("character", "hexadecimal"),
    "21": ("binary", "all"),
    "22": ("octal", "all"),
    "23": ("decimal", "all"),
    "24": ("hexadecimal", "all"),
    "25": ("character", "all"),
}


def show_menu():
    print("\n" + "=" * 40)
    print("   NUMBER BASE & CHARACTER CONVERTER")
    print("=" * 40)

    last_group = ""
    for number in OPTIONS:  # noqa: PLC0206
        from_type, to_type = OPTIONS[number]

        if to_type == "all":
            group = "FULL TABLE"
        else:
            group = from_type.upper()

        if group != last_group:
            print("\n--- " + group + " ---")
            last_group = group
        print(f"[{number}] {from_type.title()} to {to_type.title()}")

    print("\n[0] Exit")


def get_input(from_type):
    if from_type == "character":
        return input("\nEnter character / text: ")
    return input(f"\nEnter {from_type} value(s) (space or comma separated): ")


def main():
    while True:
        show_menu()
        choice = input("\nEnter your choice: ").strip()

        if choice == "0":
            print("\nExiting... See You Soon....")
            break

        if choice not in OPTIONS:
            print("\nInvalid choice. Please select a number from the menu.")
            continue

        from_type, to_type = OPTIONS[choice]
        raw = get_input(from_type)

        try:
            if to_type == "all":
                print("\n" + all_text(convert_all(raw, from_type)))
            else:
                rows = convert(raw, from_type, to_type)
                print("\n" + pair_text(rows, from_type, to_type))
        except ValueError as error:
            print(f"\nError: {error}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nExiting...")
