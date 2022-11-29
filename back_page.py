from typing import Union, Iterable
from pathlib import Path
from PIL import Image

"""
Do zrobienia:
1) okreslenie lokalizacji pol na naklejki V
2.1) dopasowanie naklejek V
2.2) obliczanie miejsc na naklejki V
2.3) zmiana rozmiaru naklejek V
3) przetwarzanie wielu naklejek X
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


def place_sticker(im: Image, sticker: Union[str, Path], row: int = 0, col: int = 0):
    sticker = Path(sticker)
    sticker = _resize_sticker(sticker)
    # sticker.show()
    im.paste(sticker,
             (FIRST_FIELD_UL[0] + (col % 3) * FIELD_X_OFFSET,
              FIRST_FIELD_UL[1] + (row % 3) * FIELD_Y_OFFSET))
    return im


def process_stickers(image: Union[str, Path], stickers: Iterable[Union[str, Path]]):
    image = Path(image)
    image = Image.open(image)
    col = 0
    row = 1
    for ind, i in enumerate(stickers, 1):
        sticker = Path(i)
        image = place_sticker(image, sticker, row, col)
        if ind % 3 == 0:
            col += 1
        row += 1
        row %= 3
    image.show()


if __name__ == '__main__':
    # place_sticker(SAMPLE, SAMPLE_STICKER, 1, 2)
    process_stickers(SAMPLE, 7 * [SAMPLE_STICKER])
