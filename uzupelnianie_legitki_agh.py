from typing import Union
from pathlib import Path
from PIL import Image

"""
Punkt (0, 0) Gorny Lewy Róg!!!
DO ZROBIENIA: 
    1) zmienic rozmiar
    2)
"""
SAMPLE = Path(__file__).parent / 'legitymacja_wzor.jpg'
SAMPLE_FACE = Path(__file__).parent / 'escobar.jpg'
HEIGHT_FACE, WIDTH_FACE = 124, 100


def get_resized_face(face: Union[str, Path]):
    face = Path(face)
    im = Image.open(face)
    return im.resize((WIDTH_FACE, HEIGHT_FACE))


