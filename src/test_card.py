from ui import CosmicUI
from engine import get_compatibility_reading
import sys

def run_test():
    ui = CosmicUI()
    
    # Simulate a "Karmic Graduate" (Born 1995) meeting a "Karmic Initiate" (Born 1997)
    user_name = "Milcah"
    user_bday = "Jun 15 1995"
    partner_name = "Eve"
    partner_bday = "Aug 20 1997"
    
    # 1. Show the "Atmosphere"
    ui.show_cosmic_weather()
    
    # 2. Get the Logic & Reading
    reading, u1_stat, u2_stat = get_compatibility_reading(
        user_name, user_bday, partner_name, partner_bday
    )
    
    # 3. Show the Badges (The "Weight")
    ui.show_saturn_warning(u1_stat)
    ui.show_saturn_warning(u2_stat)
    
    # 4. Show the Final Card (The "Gift")
    # We'll use a high passion score for the demo
    ui.show_card(partner_name, reading, score=95)

if __name__ == "__main__":
    run_test()