import argparse

from core.converter import convert, convert_all
from core.display import all_text, pair_text

SHORT_NAMES = {
    "bin": "binary",
    "oct": "octal",
    "dec": "decimal",
    "hex": "hexadecimal",
    "char": "character",
}


def main():
    parser = argparse.ArgumentParser(description="Convert binary, octal, decimal, hexadecimal values and characters")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-b", "--bin", "--binary", dest="binary", nargs="+", help="binary value(s)")
    group.add_argument("-o", "--oct", "--octal", dest="octal", nargs="+", help="octal value(s)")
    group.add_argument("-d", "--dec", "--decimal", dest="decimal", nargs="+", help="decimal value(s)")
    group.add_argument(
        "-x",
        "--hex",
        "--hexadecimal",
        dest="hexadecimal",
        nargs="+",
        help="hexadecimal value(s)",
    )
    group.add_argument("-c", "--ch", "--char", dest="char", nargs="+", help="character or text")
    parser.add_argument(
        "-t",
        "--to",
        nargs="?",
        choices=list(SHORT_NAMES) + list(SHORT_NAMES.values()),
        help="convert to one type only (default: show everything)",
    )
    args = parser.parse_args()

    if args.binary:
        from_type, raw = "binary", " ".join(args.binary)
    elif args.octal:
        from_type, raw = "octal", " ".join(args.octal)
    elif args.decimal:
        from_type, raw = "decimal", " ".join(args.decimal)
    elif args.hexadecimal:
        from_type, raw = "hexadecimal", " ".join(args.hexadecimal)
    else:
        from_type, raw = "character", " ".join(args.char)

    try:
        if args.to:
            to_type = SHORT_NAMES.get(args.to, args.to)
            print(pair_text(convert(raw, from_type, to_type), from_type, to_type))
        else:
            print(all_text(convert_all(raw, from_type)))
    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
