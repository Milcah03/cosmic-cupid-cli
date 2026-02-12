import time
import os
import warnings
from src.ui import CosmicUI
from src.engine import get_compatibility_reading
from src.exporter import save_card_to_image
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.text import Text
from rich.prompt import Prompt
from rich.table import Table

warnings.filterwarnings("ignore")
console = Console()

def main():
    ui = CosmicUI()
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # --- 1. THE VALENTINE HEADER ---
    header_text = Text.assemble(
        ("\n🌹 ", "red"),
        ("COSMIC CUPID 2026 ", "bold deep_pink3"),
        ("🌹\n", "red"),
        ("A partner ritual for the fated.", "italic light_pink3")
    )
    console.print(Align.center(Panel(header_text, border_style="red", padding=(1, 5))))

    # --- 2. THE INPUT SANCTUARY ---
    console.print("\n" + " " * 20 + "[bold red]❤ YOUR DETAILS[/]")
    name = Prompt.ask(" " * 20 + "[hot_pink3]Your Name[/]")
    bday = Prompt.ask(" " * 20 + "[hot_pink3]Birthdate[/] [grey62](Dec 03 1995)[/]")
    
    console.print("\n" + " " * 20 + "[bold red]❤ PARTNER DETAILS[/]")
    p_name = Prompt.ask(" " * 20 + "[hot_pink3]Partner Name[/]")
    p_bday = Prompt.ask(" " * 20 + "[hot_pink3]Birthdate[/] [grey62](May 20 1996)[/]")

    # --- 3. THE RITUAL TRANSITION ---
    console.print("\n")
    # Switched to 'dots' for universal compatibility across terminal versions
    with console.status("[bold deep_pink3]Knitting your stars together...[/]", spinner="dots"):
        reading, badge_text, *_ = get_compatibility_reading(name, bday, p_name, p_bday)
        time.sleep(2.5) 

    # --- 4. SHOW RESULTS ---
    os.system('cls' if os.name == 'nt' else 'clear')
    
    if any(k in badge_text.upper() for k in ["GRADUATION", "PISCES", "INITIATE"]):
        ui.show_saturn_warning(badge_text)
    
    ui.show_card(f"{name} & {p_name}", reading, 95)

    # --- 5. EXPORT & SUCCESS ---
    path = save_card_to_image(f"{name}_{p_name}", reading, 95)
    
    final_box = Text.assemble(
        ("✨ Destiny Card Saved ✨\n", "bold white"),
        (f"{path}", "italic hot_pink3")
    )
    console.print(Align.center(Panel(final_box, border_style="red", expand=False)))
    
    # Keeps terminal open for the user to admire the card
    input("\n" + " " * 20 + "[Press Enter to leave the ritual...]")

if __name__ == "__main__":
    main()