from typing import Union
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

"""
Do zrobienia:
1) okreslenie lokalizacji pol na naklejki V
2.1) dopasowanie naklejek X
2.2) obliczanie miejsc na naklejki
2.3) zmiana rozmiaru naklejek
"""

SAMPLE = Path(__file__).parent / 'images' / 'tyl_legitka.jpeg'
SAMPLE_STICKER = Path(__file__).parent / 'images' / 'naklejka.png'
FIRST_FIELD_UL = 33, 37
STICKER_SIZE = 46, 41
FIELD_X_OFFSET, FIELD_Y_OFFSET = 66, 57


def _resize_sticker(sticker: Union[str, Path]):
    sticker = Path(sticker)
    im = Image.open(sticker)
    im = im.resize(STICKER_SIZE)
    return im


