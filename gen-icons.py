from PIL import Image, ImageDraw, ImageFont
import os

def make_icon(size, path):
    img = Image.new('RGB', (size, size), '#0f1117')
    draw = ImageDraw.Draw(img)
    # yellow rounded rect background
    margin = size // 8
    r = size // 5
    draw.rounded_rectangle([margin, margin, size-margin, size-margin], radius=r, fill='#e8c547')
    # emoji-like food symbol
    cx, cy = size//2, size//2
    fs = int(size * 0.45)
    try:
        font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', fs)
    except:
        font = ImageFont.load_default()
    draw.text((cx, cy), "🥗", font=font, anchor='mm', fill='#0f1117')
    img.save(path)

make_icon(192, '/home/claude/diet-pwa/icon-192.png')
make_icon(512, '/home/claude/diet-pwa/icon-512.png')
print("Icons created")
