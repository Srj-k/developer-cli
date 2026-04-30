from rich.console import Console
from rich.table import Table

console = Console()

# Prints multiple objects as a table
def print_table(title, columns, rows):
    table = Table(title=title)

    for column in columns:
        table.add_column(column)

    for row in rows:
        table.add_row(*map(str,row))

    console.print(table)

# Prints detail of one object
def print_detail(title: str, data: dict):
    table = Table(title=title, show_header=False)

    table.add_column("Field", style="bold cyan")
    table.add_column("Value", style="white")

    for key, value in data.items():
        table.add_row(str(key), str(value))

    console.print(table)