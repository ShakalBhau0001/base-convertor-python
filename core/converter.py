BASES = {"binary": 2, "octal": 8, "decimal": 10, "hexadecimal": 16}

SPECIAL_CHARS = {
    0: "NUL",
    7: "BEL",
    8: "BS",
    9: "TAB",
    10: "LF",
    13: "CR",
    27: "ESC",
    32: "SPACE",
    127: "DEL",
}


def to_decimal(value, base):
    value = value.strip().lower()
    try:
        # int() already understands the 0b / 0o / 0x prefixes
        number = int(value, BASES[base])
    except ValueError:
        raise ValueError(f"'{value}' is not a valid {base} number")

    if number < 0:
        raise ValueError("negative numbers are not supported")
    return number


def from_decimal(number, base):
    if base == "binary":
        return bin(number)[2:]
    if base == "octal":
        return oct(number)[2:]
    if base == "hexadecimal":
        return hex(number)[2:].upper()
    return str(number)


def number_to_char(number):
    # D800-DFFF are surrogates, chr() gives a broken character for them
    if number > 0x10FFFF or 0xD800 <= number <= 0xDFFF:
        return None
    return chr(number)


def show_char(char):
    code = ord(char)
    if code in SPECIAL_CHARS:
        return "<" + SPECIAL_CHARS[code] + ">"
    if not char.isprintable():
        return f"<U+{code:04X}>"
    return char


def read_numbers(raw, from_type):
    numbers = []

    if from_type == "character":
        if raw == "":
            raise ValueError("please enter some text")
        for char in raw:
            numbers.append((show_char(char), ord(char)))
    else:
        values = raw.replace(",", " ").split()
        if len(values) == 0:
            raise ValueError("please enter a value")
        for value in values:
            numbers.append((value, to_decimal(value, from_type)))

    return numbers


def convert(raw, from_type, to_type):
    rows = []
    for label, number in read_numbers(raw, from_type):
        char = number_to_char(number)

        if to_type == "character":
            if char is None:
                raise ValueError(f"{label} is not a valid unicode character")
            result = show_char(char)
        else:
            result = from_decimal(number, to_type)

        rows.append((label, result, char))
    return rows


def convert_all(raw, from_type):
    results = []
    for label, number in read_numbers(raw, from_type):
        results.append(
            {
                "input": label,
                "number": number,
                "binary": from_decimal(number, "binary"),
                "octal": from_decimal(number, "octal"),
                "decimal": from_decimal(number, "decimal"),
                "hexadecimal": from_decimal(number, "hexadecimal"),
                "char": number_to_char(number),
            }
        )
    return results
