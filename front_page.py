from typing import Union
from pathlib import Path
from tomli import load
from PIL import Image, ImageDraw, ImageFont
__all__ = ['front_page']
"""
Punkt (0, 0) Gorny Lewy Róg!!!
DO ZROBIENIA: !
    1) zmienic rozmiar V
    2) dopasowac obrazek V
    3) zrobic napisy V
    4) ustawic imie i nazwisko V
    5) dopracowac obraz V
    6) dodac AGH V
    7) stale do TOML V
    8) chip V
    9) druga strona V
    10) poprawienie chipu V
    11) Dokumentacja V
"""
SAMPLE = Path(__file__).parent / 'images' / 'legitymacja_wzor.jpg'
SAMPLE_FACE = Path(__file__).parent / 'images' / 'escobar.jpg'
CHIP_IMAGE = Path(__file__).parent / 'images' / 'chip.png'
FONT_FILE = Path(__file__).parent / 'ArchivoNarrow-VariableFont_wght.ttf'
BOLD_FONT_FILE = Path(__file__).parent / 'ArchivoNarrow-Bold.ttf'
with (Path(__file__).parent / 'constants.toml').open(mode='rb') as f:
    CONSTANTS = load(f)
HEIGHT_FACE, WIDTH_FACE = CONSTANTS['other']['height_face'], CONSTANTS['other']['width_face']
COLUMN1 = CONSTANTS['columns']['column1']['x'], CONSTANTS['columns']['column1']['y']
COLUMN2 = CONSTANTS['columns']['column2']['x'], CONSTANTS['columns']['column2']['y']
COLUMN3 = CONSTANTS['columns']['column3']['x'], CONSTANTS['columns']['column3']['y']
IMAGE_FIELD_UL = CONSTANTS['image_field']['image_field_ul']['x'], CONSTANTS['image_field']['image_field_ul']['y']
IMAGE_FIELD_LL = CONSTANTS['image_field']['image_field_ll']['x'], CONSTANTS['image_field']['image_field_ll']['y']
IMAGE_FIELD_UR = CONSTANTS['image_field']['image_field_ur']['x'], CONSTANTS['image_field']['image_field_ur']['y']
IMAGE_FIELD_LR = CONSTANTS['image_field']['image_field_lr']['x'], CONSTANTS['image_field']['image_field_lr']['y']
OFFSET = CONSTANTS['other']['offset']
DEFAULT_UNIVERSITY = CONSTANTS['other']['default_university']
UNIVERSITY = CONSTANTS['other']['university']['x'], CONSTANTS['other']['university']['y']
CHIP_UL = CONSTANTS['chip']['chip_ul']['x'], CONSTANTS['chip']['chip_ul']['y']
CHIP_LR = CONSTANTS['chip']['chip_lr']['x'], CONSTANTS['chip']['chip_lr']['y']


class NotAFileError(FileExistsError):
    ...


def _get_resized_face(face: Union[str, Path]) -> Image.Image:
    """Resizes The Face Image To The Default Size(100x124)

    Args:
        face (Union[str, Path]): The Face
    Returns:
        Image.Image: A Resized Face
    """
    face = Path(face)
    im = Image.open(face)
    return im.resize((WIDTH_FACE, HEIGHT_FACE))


def _paste_in_image(image: Union[str, Path], face: Union[str, Path]) -> Image.Image:
    """Pastes In An Image Of A Face

    Args:
        image (Union[str, Path]): The ID's Front Page
        face (Union[str, Path]): The Face
    Returns:
        Image.Image: The ID With A Pasted Face
    """
    image1 = Path(image)
    im1 = Image.open(image1)
    im2 = _get_resized_face(Path(face))
    im1.paste(im2, IMAGE_FIELD_UL)
    return im1


def _add_text(image: Image, released: str, album: str, pesel: str, name: str) -> Image.Image:
    """Adds Text To The ID Image

    Args:
        image (Image.Image): The ID's Front Page
        released: (str): Date Of Releasing The ID
        album: (str): ID Number Of The Student
        pesel: (str): Polish Pesel Number
        name: (str): Student's Name
    Returns:
        Image.Image: The ID's Front Page With Text
    """
    im_draw = ImageDraw.Draw(image)
    my_font = ImageFont.truetype(str(FONT_FILE), 9)
    second_font = ImageFont.truetype(str(FONT_FILE), 12)
    im_draw.text(COLUMN1, released, fill=(0, 0, 0), font=my_font)
    im_draw.text(COLUMN2, album, fill=(0, 0, 0), font=my_font)
    im_draw.text(COLUMN3, pesel, fill=(0, 0, 0), font=my_font)
    im_draw.text((image.size[0] // 2 - len(name) * OFFSET,
                  image.size[1] // 2 - len(name) * OFFSET),
                 '\n'.join(name.split(' ')),
                 fill=(0, 0, 0),
                 font=second_font,
                 align='center')
    # image.show()
    return image


def _add_university(image: Image, university: str = DEFAULT_UNIVERSITY) -> Image.Image:
    """Adds An University To The ID
    Args:
        image (Image.Image): The ID's Front Page
    Returns:
        Image.Image: The ID's Front Page With An University
    """
    im_draw = ImageDraw.Draw(image)
    my_font = ImageFont.truetype(str(BOLD_FONT_FILE), 9)
    im_draw.text((UNIVERSITY[0] - len(university), UNIVERSITY[1]),
                 university,
                 fill=(0, 0, 0),
                 font=my_font,
                 align='right')
    return image


def _add_chip(image: Image):
    """Adds A Chip To The ID
    Args:
        image (Image.Image): The ID's Front Page
    Returns:
        Image.Image: The ID With A Chip
    """
    chip = Image.open(CHIP_IMAGE)
    chip = chip.resize((CHIP_LR[0] - CHIP_UL[0], CHIP_LR[1] - CHIP_UL[1]))
    image.paste(chip, CHIP_UL)
    return image


def front_page(image: Union[str, Path],
               face: Union[str, Path],
               released: str, album: str,
               pesel: str, name: str) -> Image.Image:
    """Generates The Front Page Of The ID

    Args:
        image (Union[str, Path]): The Front Page OF The ID
        face (Union[str, Path]): A Face To Be Used In The ID
        released: (str): Date Of Releasing The ID
        album: (str): ID Number Of The Student
        pesel: (str): Polish Pesel Number
        name: (str): Student's Name
    Returns:
        Image.Image: The Complete Front Page Of The ID
    """
    image = Path(image)
    face = Path(face)
    if not image.is_file():
        raise NotAFileError('Image is not a file') from None
    if not face.is_file():
        raise NotAFileError('Face is not a file') from None
    image = _paste_in_image(image, face)
    image = _add_university(image)
    image = _add_chip(image)
    image = _add_text(image, released, album, pesel, name)
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
