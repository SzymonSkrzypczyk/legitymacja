from typing import Union
from pathlib import Path
from PIL import Image

"""
Punkt (0, 0) Gorny Lewy Róg!!!
DO ZROBIENIA: 
    1) zmienic rozmiar V
    2) dopasowac obrazek X
    3) zrobic napisy
"""
SAMPLE = Path(__file__).parent / 'legitymacja_wzor.jpg'
SAMPLE_FACE = Path(__file__).parent / 'escobar.jpg'
HEIGHT_FACE, WIDTH_FACE = 124, 100
COLUMN1 = 79, 178
COLUMN2 = 79, 190
COLUMN3 = 79, 202
IMAGE_FIELD_UL = 281, 115
IMAGE_FIELD_LL = 281, 115 + HEIGHT_FACE
IMAGE_FIELD_UR = 281 + WIDTH_FACE, 115
IMAGE_FIELD_LR = 281 + WIDTH_FACE, 115 + HEIGHT_FACE


def get_resized_face(face: Union[str, Path]):
    face = Path(face)
    im = Image.open(face)
    return im.resize((WIDTH_FACE, HEIGHT_FACE))
