from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.align import Align

console = Console()

class CosmicUI:
    def __init__(self):
        self.pink = "deep_pink3"
        self.gold = "gold1"

    def show_saturn_warning(self, status_text):
        """Displays the Karmic context BEFORE the card appears."""
        if "Graduate" in status_text:
            title, subtitle = "🎓 THE KARMIC GRADUATE", "Your 3-year trial ends tonight. You have mastered the lesson."
        elif "Initiate" in status_text:
            title, subtitle = "🔥 THE KARMIC INITIATE", "Your 3-year journey begins today. Fortune favors the bold."
        else:
            title, subtitle = "⚠️ KARMIC THRESHOLD", "You are navigating a 30-year cycle. This love is destined."

        badge_content = Text.assemble((f"{title}\n", "bold gold1"), (f"{subtitle}", "italic white"))
        badge = Panel(Align.center(badge_content), style="on grey11", border_style=self.gold, expand=False)
        console.print("\n", Align.center(badge))

    def show_card(self, name, reading, score):
        """Displays a beautiful, intimate Valentine's Card."""
        hearts = "💖 " * (score // 10)
        
        # This is where card_content must be defined
        card_content = Text()
        card_content.append(f"\n❤  A MESSAGE FROM THE STARS  ❤\n\n", style="bold deep_pink3")
        card_content.append(f"Dearest {name.upper()},\n\n", style="bold white")
        card_content.append(f"{reading}\n\n", style="italic white")
        card_content.append(f"Yours, Always.\n", style="bold deep_pink3")
        card_content.append(f"\n{hearts}\n", style="bold")

        card = Panel(
            Align.center(card_content),
            title="[bold white]★ 2026 VALENTINE ★[/]",
            subtitle="[italic pink1]Bound by Stardust and Steel[/]",
            border_style=self.gold,
            padding=(1, 4),
            width=65
        )
        console.print("\n", Align.center(card))

    def show_cosmic_weather(self):
        """Displays the 'Astrology Weather' for the Feb 14th weekend."""
        weather_text = Text.assemble(
            ("\n🌹 VALENTINE'S WEEKEND 2026 CLIMATE 🌹\n\n", "bold bright_magenta"),
            ("• ", "white"), ("VENUS EXALTED: ", "deep_pink3"), ("Deep, soulful romance is at a 30-year peak.\n", "white"),
            ("• ", "white"), ("SATURN IN ARIES: ", "gold1"), ("A new era of commitment begins tonight.\n", "white"),
            ("• ", "white"), ("ECLIPSE PORTAL: ", "cyan1"), ("Fated events are moving rapidly; trust the flow.", "white")
        )
        
        weather_panel = Panel(
            Align.center(weather_text),
            title="[bold white]LIVE COSMIC FEED[/]",
            border_style="bright_blue",
            padding=(1, 2),
            expand=False
        )
        console.print("\n", Align.center(weather_panel))