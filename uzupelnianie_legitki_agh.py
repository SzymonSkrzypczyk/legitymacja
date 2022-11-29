from typing import Union
from configparser import ConfigParser
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

"""
Punkt (0, 0) Gorny Lewy Róg!!!
DO ZROBIENIA: 
    1) zmienic rozmiar V
    2) dopasowac obrazek V
    3) zrobic napisy V
    4) ustawic imie i nazwisko V
    5) dopracowac obraz V
    6) dodac AGH V
    7) stale do configparsera X
    8) chip V
    9) druga strona X
    10) poprawienie chipu X
"""
config = ConfigParser()
config.read(Path(__file__).parent / 'constants.ini')
SAMPLE = Path(__file__).parent / 'images' / 'legitymacja_wzor.jpg'
SAMPLE_FACE = Path(__file__).parent / 'images' / 'escobar.jpg'
CHIP_IMAGE = Path(__file__).parent / 'images' / 'chip.png'
FONT_FILE = Path(__file__).parent / 'ArchivoNarrow-VariableFont_wght.ttf'
BOLD_FONT_FILE = Path(__file__).parent / 'ArchivoNarrow-Bold.ttf'
HEIGHT_FACE, WIDTH_FACE = 124, 100
COLUMN1 = 79, 173
COLUMN2 = 79, 186
COLUMN3 = 79, 200
IMAGE_FIELD_UL = 281, 115
IMAGE_FIELD_LL = 281, 115 + HEIGHT_FACE
IMAGE_FIELD_UR = 281 + WIDTH_FACE, 115
IMAGE_FIELD_LR = 281 + WIDTH_FACE, 115 + HEIGHT_FACE
OFFSET = 2
UNIVERSITY = 228, 30
CHIP_UL = 44, 75
CHIP_LR = 102, 113


class NotAFileError(FileExistsError):
    ...


def _get_resized_face(face: Union[str, Path]):
    face = Path(face)
    im = Image.open(face)
    return im.resize((WIDTH_FACE, HEIGHT_FACE))


def _paste_in_image(image: Union[str, Path], face: Union[str, Path]):
    image1 = Path(image)
    im1 = Image.open(image1)
    im2 = _get_resized_face(Path(face))
    im1.paste(im2, IMAGE_FIELD_UL)
    return im1


def _add_text(image: Image, col1: str, col2: str, col3: str, name: str):
    im_draw = ImageDraw.Draw(image)
    my_font = ImageFont.truetype(str(FONT_FILE), 9)
    second_font = ImageFont.truetype(str(FONT_FILE), 12)
    im_draw.text(COLUMN1, col1, fill=(0, 0, 0), font=my_font)
    im_draw.text(COLUMN2, col2, fill=(0, 0, 0), font=my_font)
    im_draw.text(COLUMN3, col3, fill=(0, 0, 0), font=my_font)
    im_draw.text((image.size[0] // 2 - len(name) * OFFSET,
                  image.size[1] // 2 - len(name) * OFFSET),
                 '\n'.join(name.split(' ')),
                 fill=(0, 0, 0),
                 font=second_font,
                 align='center')
    # image.show()
    return image


def _add_university(image: Image):
    im_draw = ImageDraw.Draw(image)
    my_font = ImageFont.truetype(str(BOLD_FONT_FILE), 9)
    text = 'Akademia Górniczo-Hutnicza\nim. St. Staszica\nw Krakowie'
    im_draw.text((UNIVERSITY[0] - len(text), UNIVERSITY[1]),
                 text,
                 fill=(0, 0, 0),
                 font=my_font,
                 align='right')
    return image


def _add_chip(image: Image):
    chip = Image.open(CHIP_IMAGE)
    chip = chip.resize((CHIP_LR[0] - CHIP_UL[0], CHIP_LR[1] - CHIP_UL[1]))
    image.paste(chip, CHIP_UL)
    image.show()


def front_page(image: Union[str, Path], face: Union[str, Path], col1: str, col2: str, col3: str, name: str):
    image = Path(image)
    face = Path(face)
    if not image.is_file():
        raise NotAFileError('Image is not a file') from None
    if not face.is_file():
        raise NotAFileError('Face is not a file') from None
    image = _paste_in_image(image, face)
    image = _add_university(image)
    image = _add_text(image, col1, col2, col3, name)
    return image


if __name__ == '__main__':
    # paste_in_image(SAMPLE, SAMPLE_FACE)
    _im = front_page(
        SAMPLE,
        SAMPLE_FACE,
        'Yo',
        'What\'s Up',
        'wrehfghjfghgf',
        'Ktos napewno'
    )
    _im.show()
