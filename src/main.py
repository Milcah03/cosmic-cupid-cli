from ui import CosmicUI
from engine import get_compatibility_reading 
from exporter import export_as_image
import time
from rich.progress import Progress
from rich.console import Console
from rich.panel import Panel
from rich.align import Align

console = Console()

def run_app():
    ui = CosmicUI()
    
    console.print("\n[bold magenta]💘 COSMIC CUPID 2026: THE PARTNER RITUAL 💘[/]", justify="center")
    
    # 1. Collect Data for BOTH people
    name = input("Enter your name: ")
    bday = input("Enter your birthdate (e.g., Dec 03 1995): ")
    
    p_name = input("\nEnter your partner's name: ")
    p_bday = input("Enter partner's birthdate (e.g., May 20 1996): ")

    # 2. Dramatic Progress Bar
    with Progress() as progress:
        task = progress.add_task("[magenta]Syncing Souls & Transits...", total=100)
        while not progress.finished:
            time.sleep(0.01)
            progress.update(task, advance=2)

    # 3. GLOBAL CONTEXT: Show the Weekend Weather (Saturn/Venus/Eclipse facts)
    ui.show_cosmic_weather()
    time.sleep(1.5) # Pause for impact

    # 4. PERSONAL LOGIC: Calculate based on historical Saturn dates
    reading, badge_text, *_ = get_compatibility_reading(name, bday, p_name, p_bday)
    
    # 5. KARMIC ALERT: Special UI for the Saturn in Pisces Generation (1993-1996)
    # This specifically checks if the logic returned a "GRADUATION" status
    if "GRADUATION" in badge_text or "PISCES" in badge_text:
        ui.show_saturn_warning()
    
    # 6. DISPLAY RESULTS: Show the terminal card
    display_name = f"{name} & {p_name}"
    ui.show_card(display_name, reading, 95)

    # 7. EXPORT: Generate the PNG for the Valentine's Gift
    path = export_as_image(f"{name}_{p_name}", reading, 95)
    console.print(f"\n[bold green]✅ Success![/] Your shared destiny card is ready: [bold white]{path}[/]")

if __name__ == "__main__":
    run_app()