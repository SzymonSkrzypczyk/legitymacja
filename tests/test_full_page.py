from pathlib import Path
from PIL import Image, JpegImagePlugin
import pytest
from ..create_full import main, _merge_photos, _resize


SAMPLE_FRONT = Path(__file__).parent.parent / 'images' / 'legitymacja_wzor.jpg'
FRONT_IMG = Image.open(SAMPLE_FRONT)
SAMPLE_BACK = Path(__file__).parent.parent / 'images' / 'tyl_legitka.jpeg'
BACK_IMG = Image.open(SAMPLE_BACK)
SAMPLE_FACE = Path(__file__).parent.parent / 'images' / 'escobar.jpg'
FACE_IMG = Image.open(SAMPLE_FACE)
SAMPLE_STICKER = Path(__file__).parent.parent / 'images' / 'naklejka.png'


def test_return_merge():
    val = _merge_photos(FRONT_IMG, BACK_IMG)
    assert type(val) == Image.Image


def test_return_resize():
    val = _resize(FRONT_IMG, BACK_IMG)
    assert len(val) == 2
    assert type(val[0]) == JpegImagePlugin.JpegImageFile


def test_return_main():
    val = main(
        SAMPLE_FRONT,
        SAMPLE_BACK,
        SAMPLE_FACE,
        9 * [SAMPLE_STICKER],
        'COL1',
        'COL2',
        'COL3',
        'NAME'
    )
    assert type(val) == Image.Image


def test_size_resize():
    val = _resize(FRONT_IMG, BACK_IMG)
    assert val[0].size == val[1].size


def test_resized_wrong_types():
    with pytest.raises(AttributeError):
        _resize(FRONT_IMG, SAMPLE_BACK)
        _resize(SAMPLE_FRONT, BACK_IMG)
        assert True


'''def test_main_wrong_types():
    with pytest.raises(TypeError):
        main(
            FRONT_IMG,
            SAMPLE_BACK,
            SAMPLE_FACE,
            9 * [SAMPLE_STICKER],
            'COL1',
            'COL2',
            'COL3',
            'NAME'
        )
    assert True'''


def test_merge_wrong_front():
    with pytest.raises(AttributeError):
        _merge_photos(SAMPLE_FRONT, BACK_IMG)
        assert True


def test_merge_wrong_back():
    with pytest.raises(AttributeError):
        _merge_photos(FRONT_IMG, SAMPLE_BACK)
        assert True

