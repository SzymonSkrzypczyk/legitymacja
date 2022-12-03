from typing import Union, List, Set
from pathlib import Path
from PIL import Image
from back_page import back_page
from front_page import front_page
"""
Do zrobienia
1) zmienic nazwe argumentow V
2) napisac dokumentacje X
3) sprawdzenie opcji zapisu X
"""
SAMPLE_FRONT = Path(__file__).parent / 'images' / 'legitymacja_wzor.jpg'
SAMPLE_BACK = Path(__file__).parent / 'images' / 'tyl_legitka.jpeg'
SAMPLE_FACE = Path(__file__).parent / 'images' / 'escobar.jpg'
SAMPLE_STICKER = Path(__file__).parent / 'images' / 'naklejka.png'


def _resize(im1: Image, im2: Image):
    size = im1.size
    im2 = im2.resize(size)
    return im1, im2


def _merge_photos(im1: Image, im2: Image):
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
         save: Union[str, Path] = None):
    front = front_page(front_image, face_photo, released, album, pesel, name)
    back = back_page(back_image, stickers)
    image = _merge_photos(front, back)
    if save is not None:
        path = Path(save)
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
