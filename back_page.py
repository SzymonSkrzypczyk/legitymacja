from typing import Union
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

"""
Do zrobienia:
1) okreslenie lokalizacji pol na naklejki V
2.1) dopasowanie naklejek X
2.2) obliczanie miejsc na naklejki X
2.3) zmiana rozmiaru naklejek X
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


def place_sticker(image: Union[str, Path], sticker: Union[str, Path], index: int = 1):
    image = Path(image)
    sticker = Path(sticker)
    sticker = _resize_sticker(sticker)
    # sticker.show()
    im = Image.open(image)
    col = index % 3 - 1
    if index <= 3:
        row = 0
    elif 3 < index <= 6:
        row = 1
    else:
        row = 2
    im.paste(sticker,
             (FIRST_FIELD_UL[0] + FIELD_X_OFFSET * col, FIRST_FIELD_UL[1] + FIELD_Y_OFFSET * row),
             )
    im.show()


if __name__ == '__main__':
    place_sticker(SAMPLE, SAMPLE_STICKER, 7)
