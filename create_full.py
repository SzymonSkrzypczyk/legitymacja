from typing import Union, List, Set
from pathlib import Path
from back_page import back_page
from front_page import front_page
"""
Do zrobienia
1) zmienic nazwe argumentow X
2) napisac dokumentacje X
"""


def main(front_image: Union[str, Path],
         back_image: Union[str, Path],
         face_photo: Union[str, Path],
         stickers: Union[Set[Union[str, Path]], List[Union[str, Path]]],
         col1: str,
         col2: str,
         col3: str,
         name: str):
    front = front_page(front_image, face_photo, col1, col2, col3, name)
    back = back_page(back_image, stickers)
    # dodac do siebie obrazy!


if __name__ == '__main__':
    ...
