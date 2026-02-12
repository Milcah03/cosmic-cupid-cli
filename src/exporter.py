from PIL import Image, ImageDraw, ImageFont
import os

def save_card_to_image(name, reading, score):
    # Ensure exports folder exists
    if not os.path.exists("exports"):
        os.makedirs("exports")

    # Card Configuration
    width, height = 800, 500
    background_color = (15, 15, 15)  # Dark Grey/Black (grey11)
    gold_border = (255, 215, 0)     # Gold1
    text_color = (255, 255, 255)    # White
    accent_color = (199, 21, 133)   # DeepPink3

    # Create Image
    img = Image.new('RGB', (width, height), color=background_color)
    draw = ImageDraw.Draw(img)

    # Draw Gold Border
    draw.rectangle([10, 10, width-10, height-10], outline=gold_border, width=3)

    # Add Text (Using default font for reliability, or you can point to a .ttf)
    try:
        # If you have a font file, you can load it here
        font_title = ImageFont.load_default() 
        font_body = ImageFont.load_default()
    except:
        font_title = None
        font_body = None

    # Title
    draw.text((width/2, 50), "★ 2026 VALENTINE ★", fill=gold_border, anchor="mm")
    
    # Message
    draw.text((40, 120), f"Dearest {name.upper()},", fill=text_color)
    
    # Reading (Simple wrap logic)
    wrapped_text = ""
    words = reading.split()
    line = ""
    for word in words:
        if len(line + word) < 60:
            line += word + " "
        else:
            wrapped_text += line + "\n"
            line = word + " "
    wrapped_text += line
    
    draw.text((40, 160), wrapped_text, fill=text_color)

    # Footer
    hearts = "💖 " * (score // 10)
    draw.text((width/2, 400), hearts, fill=accent_color, anchor="mm")
    draw.text((width/2, 450), "Bound by Stardust and Steel", fill=gold_border, anchor="mm")

    # Save
    filename = f"exports/{name}_valentine_2026.png"
    img.save(filename)
    return filename