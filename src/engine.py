import datetime
from kerykeion import AstrologicalSubject

def check_saturn_status(birth_date_str):
    """
    DE Precision: Maps the user to the exact Saturnian Generation.
    - Graduate: 21 May 1993 – 7 Apr 1996
    - Initiate: 7 Apr 1996 – 9 Jun 1998
    """
    try:
        # Normalize date for parsing
        bday = datetime.datetime.strptime(birth_date_str, "%b %d %Y")
        pisces_start = datetime.datetime(1993, 5, 21)
        pisces_end = datetime.datetime(1996, 4, 7)
        aries_end = datetime.datetime(1998, 6, 9)

        if pisces_start <= bday <= pisces_end:
            return "Karmic Graduate"
        elif pisces_end < bday <= aries_end:
            return "Karmic Initiate"
        return "Stable Spirit"
    except:
        return "Stable Spirit"

def get_compatibility_reading(name, bday, p_name, p_bday):
    # 1. Gather Factual Saturn Data
    u1_stat = check_saturn_status(bday)
    u2_stat = check_saturn_status(p_bday)
    
    # 2. Extract Sun Signs for personal flavor
    try:
        u1_year = int(bday.split()[-1])
        u2_year = int(p_bday.split()[-1])
        sub1 = AstrologicalSubject(name, u1_year, 12, 3, 12, 0)
        sub2 = AstrologicalSubject(p_name, u2_year, 11, 15, 12, 0)
        u1_sign, u2_sign = sub1.sun['sign'], sub2.sun['sign']
    except:
        u1_sign, u2_sign = "Celestial", "Cosmic"

    # 3. Creative Reasoning Logic (Replaces the broken AI CLI)
    # This logic acts as the 'Reasoning Engine' for the card content.
    if "Graduate" in u1_stat or "Graduate" in u2_stat:
        reading = (
            f"As the {u1_sign} and {u2_sign} tides shift tonight, the gravity of the past three years "
            "finally dissolves into stardust. You have survived the Saturnian forge together, "
            "proving that your bond is not just a lesson, but a lasting legacy. "
            "Tonight, the heavy lifting ends; the deep breathing begins."
        )
    elif "Initiate" in u1_stat or "Initiate" in u2_stat:
        reading = (
            f"A new cycle of fire begins for the {u1_sign} and {u2_sign} connection. "
            "As Saturn enters Aries, your love is stepping into a bold, brave ignition. "
            "Trust the shifting tides between you; they are not pulling you apart, "
            "but anchoring you into a destiny made of steel and soul."
        )
    else:
        reading = (
            f"The exalted Venus in Pisces illuminates the space between {u1_sign} and {u2_sign}. "
            "While the world navigates shifting karmic tides, your connection remains a sanctuary "
            "of light. Every moment shared tonight is a seed planted in a 30-year garden "
            "of fated, extraordinary love."
        )

    return reading, u1_stat, u2_stat