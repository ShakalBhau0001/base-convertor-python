from core.converter import show_char


def combined_text(chars):
    if len(chars) < 2 or None in chars:
        return ""
    text = "".join(chars)
    if text.isprintable():
        return text
    return ""


def pair_text(rows, from_type, to_type):
    lines = [f"{from_type.title()} -> {to_type.title()}", "-" * 40]

    for label, result, char in rows:
        line = f"{label} -> {result}"
        if to_type != "character" and char is not None:
            line += f"   (char: {show_char(char)})"
        lines.append(line)

    text = combined_text([row[2] for row in rows])
    if text != "":
        lines.append("\nCombined text: " + text)
    return "\n".join(lines)


def all_text(results):
    blocks = []

    for i, item in enumerate(results, 1):
        lines = [f"[{i}] Input: {item['input']}"]
        lines.append(f"  Binary      : {item['binary']}")
        lines.append(f"  Octal       : {item['octal']}")
        lines.append(f"  Decimal     : {item['decimal']}")
        lines.append(f"  Hexadecimal : {item['hexadecimal']}")
        if item["char"] is None:
            lines.append("  Character   : (no valid character)")
        else:
            lines.append(f"  Character   : {show_char(item['char'])}")
            lines.append(f"  Unicode     : U+{item['number']:04X}")
        blocks.append("\n".join(lines))

    text = combined_text([item["char"] for item in results])
    if text != "":
        blocks.append("Combined text: " + text)
    return "\n\n".join(blocks)
