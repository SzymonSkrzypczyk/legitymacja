from typing import Union
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

SAMPLE = Path(__file__).parent / 'images' / 'tyl_legitka.jpeg'
im = Image.open(SAMPLE)
im.show()
