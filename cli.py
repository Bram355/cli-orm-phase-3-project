from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
from services.bot_service import create_bot, list_bots, delete_bot, add_session_to_bot

console = Console()

def show_menu():
    console.print(Panel("[bold green]Node Trader CLI[/bold green]", width=50))
    table = Table(show_header=False, box=None, padding=(0, 1))
    items = [
        "1. Create Bot",
        "2. List Bots",
        "3. Delete Bot",
        "4. Add Session to Bot",
        "5. Exit"
    ]
    for item in items:
        table.add_row(f"[cyan]{item}[/cyan]")
    console.print(table)

def handle_choice(choice):
    if choice == '1':
        name = Prompt.ask("Enter bot name")
        bot = create_bot(name)
        console.print(f"[green]Bot created:[/green] {bot}")
    elif choice == '2':
        bots = list_bots()
        if not bots:
            console.print("[yellow]No bots found.[/yellow]")
        else:
            for bot in bots:
                console.print(f"[blue]{bot.name}[/blue] (ID: {bot.id})")
    elif choice == '3':
        name = Prompt.ask("Enter bot name to delete")
        delete_bot(name)
        console.print("[red]Bot deleted.[/red]")
    elif choice == '4':
        bots = list_bots()
        if not bots:
            console.print("[yellow]No bots available.[/yellow]")
            return
        for bot in bots:
            console.print(f"{bot.id}. {bot.name}")
        bot_id = int(Prompt.ask("Enter Bot ID"))
        description = Prompt.ask("Enter session description")
        session = add_session_to_bot(bot_id, description)
        console.print(f"[green]Session added:[/green] {session}")
    elif choice == '5':
        console.print("[bold red]Exiting...[/bold red]")
        return False
    else:
        console.print("[red]Invalid choice.[/red]")
    input("\nPress Enter to continue...")
    return True
