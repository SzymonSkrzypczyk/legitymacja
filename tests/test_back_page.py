from pathlib import Path
import pytest
from PIL import Image, JpegImagePlugin
from ..back_page import _resize_sticker, _place_sticker, back_page, STICKER_SIZE

SAMPLE = Path(__file__).parent.parent / 'images' / 'tyl_legitka.jpeg'
SAMPLE_IMG = Image.open(SAMPLE)
SAMPLE_STICKER = Path(__file__).parent.parent / 'images' / 'naklejka.png'


def test_return_resize_sticker():
    val = _resize_sticker(SAMPLE_STICKER)
    assert val.size == STICKER_SIZE
    assert type(val) == Image.Image


def test_return_place_sticker():
    with pytest.raises(AttributeError):
        _place_sticker(SAMPLE_IMG, SAMPLE_STICKER)
        assert True
    val = _place_sticker(SAMPLE_IMG, SAMPLE_STICKER)
    assert type(val) == JpegImagePlugin.JpegImageFile


def test_return_back_page():
    val = back_page(SAMPLE, 2 * [SAMPLE_STICKER])
    return type(val) == Image.Image
