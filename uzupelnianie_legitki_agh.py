from typing import Union
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

"""
Punkt (0, 0) Gorny Lewy Róg!!!
DO ZROBIENIA: 
    1) zmienic rozmiar V
    2) dopasowac obrazek X
    3) zrobic napisy
"""
SAMPLE = Path(__file__).parent / 'legitymacja_wzor.jpg'
SAMPLE_FACE = Path(__file__).parent / 'escobar.jpg'
FONT_FILE = Path(__file__).parent / 'ArchivoNarrow-VariableFont_wght.ttf'
HEIGHT_FACE, WIDTH_FACE = 124, 100
COLUMN1 = 79, 174
COLUMN2 = 79, 188
COLUMN3 = 79, 200
IMAGE_FIELD_UL = 281, 115
IMAGE_FIELD_LL = 281, 115 + HEIGHT_FACE
IMAGE_FIELD_UR = 281 + WIDTH_FACE, 115
IMAGE_FIELD_LR = 281 + WIDTH_FACE, 115 + HEIGHT_FACE


def get_resized_face(face: Union[str, Path]):
    face = Path(face)
    im = Image.open(face)
    return im.resize((WIDTH_FACE, HEIGHT_FACE))


def paste_in_image(image: Union[str, Path], face: Union[str, Path]):
    image1 = Path(image)
    im1 = Image.open(image1)
    im2 = get_resized_face(Path(face))
    im1.paste(im2, IMAGE_FIELD_UL)
    return im1


def add_text(image: Image, col1: str, col2: str, col3: str):
    im_draw = ImageDraw.Draw(image)
    my_font = ImageFont.truetype(str(FONT_FILE), 9)
    im_draw.text(COLUMN1, col1, fill=(0, 0, 0), font=my_font)
    im_draw.text(COLUMN2, col2, fill=(0, 0, 0), font=my_font)
    im_draw.text(COLUMN3, col3, fill=(0, 0, 0), font=my_font)
    image.show()


if __name__ == '__main__':
    # paste_in_image(SAMPLE, SAMPLE_FACE)
    add_text(
        paste_in_image(SAMPLE, SAMPLE_FACE),
        'Yo',
        'What\'s Up',
        'wrehfghjfghgf'
    )