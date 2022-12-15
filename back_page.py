from typing import Union, Set, List
from pathlib import Path
from PIL import Image
from tomli import load
__all__ = ['back_page']
"""
Do zrobienia:
1) okreslenie lokalizacji pol na naklejki V
2.1) dopasowanie naklejek V
2.2) obliczanie miejsc na naklejki V
2.3) zmiana rozmiaru naklejek V
3) przetwarzanie wielu naklejek V
4) naprawienie ilosci rzedow i kolumn V
5) ostateczne sprawdzenie, czy dziala V
6) Dokumentacja V
"""

SAMPLE = Path(__file__).parent / 'images' / 'tyl_legitka.jpeg'
SAMPLE_STICKER = Path(__file__).parent / 'images' / 'naklejka.png'
with (Path(__file__).parent / 'constants.toml').open(mode='rb') as f:
    CONSTANTS = load(f)
FIRST_FIELD_UL = CONSTANTS['sticker']['first_field_ul']['x'], CONSTANTS['sticker']['first_field_ul']['y']
STICKER_SIZE = CONSTANTS['sticker']['sticker_size']['x'], CONSTANTS['sticker']['sticker_size']['y']
FIELD_X_OFFSET, FIELD_Y_OFFSET = CONSTANTS['sticker']['field_x_offset'], CONSTANTS['sticker']['field_y_offset']


def _resize_sticker(sticker: Union[str, Path]):
    """Resizes A Given Sticker (46x41)

    Args:
        sticker (Union[str, Path]): A Sticker To Be Resized
    Returns:
        Image.Image: The Resized Image
    """
    sticker = Path(sticker)
    im = Image.open(sticker)
    im = im.resize(STICKER_SIZE)
    return im


def _place_sticker(im: Image, sticker: Union[str, Path], row: int = 0, col: int = 0):
    """Places A Sticker In A Selected Spot Of The ID By An Offset (X_offset = 66, Y_offset = 57)

    Args:
        im (Image.Image): The Back Page Of The ID
        sticker (Union[str, Path]): A Sticker To Be Inserted
        row (int): A Row For The Calculation Of The Final Y Offset
        col (int): A Col For The Calculation Of The Final X Offset
    Returns:
        Image.Image: The Back Page With The Inserted Sticker
    """
    sticker = Path(sticker)
    sticker = _resize_sticker(sticker)
    # sticker.show()
    im.paste(sticker,
             (FIRST_FIELD_UL[0] + (col % 3) * FIELD_X_OFFSET,
              FIRST_FIELD_UL[1] + (row % 4) * FIELD_Y_OFFSET))
    return im


def back_page(image: Union[str, Path],
              stickers: Union[Set[Union[str, Path]], List[Union[str, Path]]],
              ):
    """Generates The Back Page

    Args:
        image (Union[str, Path]): The Back Page Of The ID
        stickers (Union[Set[Union[str, Path]], List[Union[str, Path]]]): A Set Or A List Of Stickers To Be Inserted
    Returns:
        Image.Image: The Complete Back Page Of The ID
    """
    image = Path(image)
    image = Image.open(image)
    row = 0
    col = 0
    for i in stickers:
        if col == 3:
            col = 0
            row += 1
        sticker = Path(i)
        image = _place_sticker(image, sticker, row, col)
        col += 1
    return image


if __name__ == '__main__':
    # place_sticker(SAMPLE, SAMPLE_STICKER, 1, 2)
    _im = back_page(SAMPLE, 11 * [SAMPLE_STICKER])
    _im.show()
