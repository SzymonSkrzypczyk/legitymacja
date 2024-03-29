from typing import Union, List, Set, Tuple
from pathlib import Path
from PIL import Image
from back_page import back_page
from front_page import front_page, DEFAULT_UNIVERSITY

__all__ = ['main']
"""
Do zrobienia
1) zmienic nazwe argumentow V
2) napisac dokumentacje V
3) sprawdzenie opcji zapisu V
"""
SAMPLE_FRONT = Path(__file__).parent / 'images' / 'legitymacja_wzor.jpg'
SAMPLE_BACK = Path(__file__).parent / 'images' / 'tyl_legitka.jpeg'
SAMPLE_FACE = Path(__file__).parent / 'images' / 'escobar.jpg'
SAMPLE_STICKER = Path(__file__).parent / 'images' / 'naklejka.png'


def _resize(im1: Image, im2: Image) -> Tuple:
    """Resizes images to a common size(size of the first image)

    Args:
        im1 (Image.Image): The First Image
        im2 (Image.Image): The Second Image
    Returns:
        Tuple: The Resized Images
    """
    size = im1.size
    im2 = im2.resize(size)
    return im1, im2


def _merge_photos(im1: Image, im2: Image) -> Image.Image:
    """Merges Two Given Images Next To Each Other

    Args:
        im1 (Image.Image): The First Image
        im2 (Image.Image): The Second Image
    Returns:
        Image.Image: A Combined Image
    """
    im1, im2 = _resize(im1, im2)
    new_img = Image.new('RGBA', (im1.size[0] * 2, im1.size[1]))
    width, _ = im1.size
    new_img.paste(im1, (0, 0))
    new_img.paste(im2, (width, 0))
    return new_img


def main(front_image: Union[str, Path],
         back_image: Union[str, Path],
         face_photo: Union[str, Path],
         stickers: Union[Set[Union[str, Path]], List[Union[str, Path]]],
         released: str,
         album: str,
         pesel: str,
         name: str,
         university: str = DEFAULT_UNIVERSITY,
         save: Union[str, Path] = None) -> Image.Image:
    """Generates A Student's ID Using Given Params

    Args:
        front_image (Image.Image): Front Page Of The ID
        back_image: (Image.Image): Back Page Of The ID
        face_photo: (Image.Image): Face To Be Pasted In
        stickers:  (Union[Set[Union[str, Path]], List[Union[str, Path]]]): An Either Set Or List Of Stickers
        released: (str): Date Of Releasing The ID
        album: (str): ID Number Of The Student
        pesel: (str): Polish Pesel Number
        name: (str): Student's Name
        university (str): Student's University
        save: (Union[str, Path]): If Given A Path Saves The Generated ID To The Given Location
    Returns:
        Image.Image: The Final Student's ID
    """
    front = front_page(front_image, face_photo, released, album, pesel, name)
    back = back_page(back_image, stickers)
    image = _merge_photos(front, back)
    if save is not None:
        path = Path(save)
        if path.suffix != '.png':
            path = str(path).replace(path.suffix, '.png')
        image.save(path)
    return image


if __name__ == '__main__':
    _im = main(
        SAMPLE_FRONT,
        SAMPLE_BACK,
        SAMPLE_FACE,
        9 * [SAMPLE_STICKER],
        'col1',
        'col2',
        'col3',
        'Sample Name'
    )
    _im.show()
