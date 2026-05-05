import os
import art
from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt, FloatPrompt

console = Console()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def calculator(a, b, opr):
    match opr:
        case "+": return a + b
        case "-": return a - b
        case "*": return a * b
        case "/":
            return a / b if b != 0 else "Error: Division by zero"

def show_history():
    clear_screen()
    table = Table(title="Calculation History", style="magenta")
    table.add_column("Timestamp", style="cyan")
    table.add_column("Expression", style="green")
    
    try:
        with open("calculatehistory.txt", "r") as file:
            for line in file:
                if ":" in line:
                    time, data = line.split(": Result == ")
                    table.add_row(time.strip(), data.strip())
        console.print(table)
    except FileNotFoundError:
        console.print("[red]No history file found.[/red]")
    
    Prompt.ask("\nPress Enter to return to the menu")

def start_calculator():
    clear_screen()
    console.print(art.logo, style="bold blue")
    
    # Input Guard for the first number
    a = FloatPrompt.ask("[bold cyan]Enter first number[/]")
    
    while True:
        opr = Prompt.ask("[bold yellow]Enter operator[/]", choices=["+", "-", "*", "/"])
        b = FloatPrompt.ask("[bold cyan]Enter another number[/]")
        
        result = calculator(a, b, opr)
        
        # Display Result in a Panel
        res_style = "bold green" if not str(result).startswith("Error") else "bold red"
        console.print(Panel(f"{a} {opr} {b} = {result}", title="Result", style=res_style, expand=False))

        # Persistent Storage
        with open("calculatehistory.txt", "a") as file:
            file.write(f"{datetime.now().strftime('%H:%M:%S')}: Result == {a} {opr} {b} = {result}\n")

        # Control Logic using choices (replacing while-loop checks)
        choice = Prompt.ask(
            "[bold yellow]1[/]: Continue, [bold yellow]2[/]: New, [bold yellow]3[/]: History, [bold yellow]4[/]: Exit\nWhat would you like to do?", 
            choices=["1", "2", "3", "4"],
            default="1"
)
        # 1: Continue, 2: New, 3: History, 4: Exit

        if choice == "1":
            a = result if not str(result).startswith("Error") else 0
            clear_screen()
            console.print(f"[bold green]Current Value: {a}[/]\n" + "-"*20)
        elif choice == "2":
            start_calculator()
            return
        elif choice == "3":
            show_history()
            start_calculator()
            return
        else:
            console.print("[bold italic magenta]Thank you for using the calculator. Goodbye![/]")
            break

if __name__ == "__main__":
    start_calculator()