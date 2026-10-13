from rich import box
from rich.align import Align
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.rule import Rule
from rich.table import Table
from rich.text import Text

from core.converter import convert, convert_all
from core.display import all_text, pair_text

console = Console()

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

EMOJIS = {
    "binary": "🔢",
    "octal": "🎱",
    "decimal": "🔟",
    "hexadecimal": "🔣",
    "character": "🔤",
    "all": "📊",
}

LABELS = {
    "binary": "Binary",
    "octal": "Octal",
    "decimal": "Decimal",
    "hexadecimal": "HexaDecimal",
    "character": "Character",
    "all": "ALL",
}

CHOICES = list(OPTIONS) + ["26", "0"]


def print_banner():
    console.clear()
    banner = Text()
    banner.append("██████      ████      ██████  ████████    ██████    ████    ██      ██    ██      ██  ████████  ██████    ██████████  ████████  ██████\n",style="bold cyan",)
    banner.append("██    ██  ██    ██  ██        ██        ██        ██    ██  ████    ██    ██      ██  ██        ██    ██      ██      ██        ██    ██\n",style="bold blue",)
    banner.append("██████    ████████    ████    ██████    ██        ██    ██  ██  ██  ██    ██      ██  ██████    ██████        ██      ██████    ██████\n",style="bold magenta",)
    banner.append("██    ██  ██    ██        ██  ██        ██        ██    ██  ██    ████      ██  ██    ██        ██    ██      ██      ██        ██    ██\n",style="bold cyan",)
    banner.append("██████    ██    ██  ██████    ████████    ██████    ████    ██      ██        ██      ████████  ██    ██      ██      ████████  ██    ██\n",style="bold blue",)
    banner.append(" NUMBER BASE CONVERTER • CHARACTER CONVERTER • Created By ShakalBhau0001 ",style="dim white",)
    console.print(
        Panel(
            Align.center(banner),
            border_style="cyan",
            box=box.DOUBLE_EDGE,
        )
    )


def divider(title=""):
    console.print(
        Rule(
            title,
            style="cyan",
        )
    )


def success(message):
    console.print(f"\n[bold green]✔[/bold green] {message}\n")


def error(message):
    console.print(f"\n[bold red]✘[/bold red] {message}\n")


def info(message):
    console.print(f"[bold yellow]ℹ[/bold yellow] {message}")


def menu():
    table = Table(
        title="Main Menu",
        title_style="bold cyan",
        box=box.DOUBLE_EDGE,
        border_style="cyan",
        padding=(0, 2),
    )
    table.add_column(
        "Option",
        justify="center",
        style="bold yellow",
    )
    table.add_column("Action", style="green",)
    last_group = ""
    for number, (from_type, to_type) in OPTIONS.items():
        if to_type == "all":
            group = "all"
        else:
            group = from_type

        # a line between each group of options
        if last_group != "" and group != last_group:
            table.add_section()
        last_group = group
        action = (
            f"{EMOJIS[from_type]} {LABELS[from_type]} To "
            f"{EMOJIS[to_type]} {LABELS[to_type]}"
        )
        table.add_row(number, action)

    table.add_section()
    table.add_row("26", "ℹ  About")
    table.add_row("0", "🚪 Exit")
    console.print(table)


def about():
    divider("About")
    text = Text()
    text.append("Number Base & Character Converter\n\n", style="bold cyan")
    text.append("Converts binary, octal, decimal and hexadecimal values\n")
    text.append("into each other and into characters (and back).\n\n")
    text.append("Tips:\n", style="bold yellow")
    text.append("  - You can enter many values at once (space or comma separated)\n")
    text.append("  - 0b, 0o and 0x prefixes are accepted\n")
    text.append("  - Character options accept full text, not just one letter\n\n")
    text.append("Created By ShakalBhau0001", style="dim white")
    console.print(Panel(text, border_style="cyan", box=box.ROUNDED))


def get_value(from_type):
    if from_type == "character":
        return console.input("\n[bold yellow]Enter character / text:[/bold yellow] ")
    return console.input(
        f"\n[bold yellow]Enter {from_type} value(s)[/bold yellow] "
        "[dim](space or comma separated)[/dim]: "
    )


def show_result(from_type, to_type, raw):
    if to_type == "all":
        text = all_text(convert_all(raw, from_type))
    else:
        text = pair_text(convert(raw, from_type, to_type), from_type, to_type)

    console.print()
    divider("Result")
    console.print(Panel(Text(text), border_style="green", box=box.ROUNDED))
    success("Conversion completed")


def main():
    while True:
        print_banner()
        menu()
        choice = Prompt.ask(
            "\n[bold cyan]Select Option[/bold cyan]",
            choices=CHOICES,
            show_choices=False,
            default="1",
        )

        if choice == "0":
            console.print()
            console.print(
                Panel(
                    Align.center(
                        Text(
                            "See You Soon! | Stay safe, stay secure. 🕵️",
                            style="bold cyan",
                        )
                    ),
                    border_style="magenta",
                    box=box.DOUBLE_EDGE,
                )
            )
            break
        elif choice == "26":
            about()
        else:
            from_type, to_type = OPTIONS[choice]
            raw = get_value(from_type)
            try:
                show_result(from_type, to_type, raw)
            except ValueError as e:
                error(str(e))

        Prompt.ask(
            "\n[dim]Press Enter to return to menu…[/dim]",
            default="",
            show_default=False,
        )


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n\n[bold cyan]See You Soon![/bold cyan]\n")
