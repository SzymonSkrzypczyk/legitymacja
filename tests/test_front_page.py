import pytest
from PIL import Image, JpegImagePlugin
from front_page import (_get_resized_face, _paste_in_image, front_page, _add_university, _add_chip,
                        _add_text, SAMPLE_FACE, SAMPLE, HEIGHT_FACE, WIDTH_FACE)


def test_return_front():
    val = front_page(SAMPLE, SAMPLE_FACE, 'col1', 'col2', 'col3', 'name')
    assert type(val) == JpegImagePlugin.JpegImageFile


def test_return_resized():
    val = _get_resized_face(SAMPLE_FACE)
    assert type(val) == Image.Image
    assert val.size == (WIDTH_FACE, HEIGHT_FACE)


def test_return_paste_in():
    val = _paste_in_image(SAMPLE, SAMPLE_FACE)
    assert type(val) == Image.Image


def test_return_university():
    with pytest.raises(AttributeError):
        _add_university(SAMPLE)
        assert True
    val = _add_university(Image.open(SAMPLE))
    assert type(val) == JpegImagePlugin.JpegImageFile


def test_return_chip():
    with pytest.raises(AttributeError):
        _add_chip(SAMPLE)
        assert True
    val = _add_chip(Image.open(SAMPLE))
    assert type(val) == JpegImagePlugin.JpegImageFile


def test_return_text():
    with pytest.raises(AttributeError):
        _add_text(SAMPLE, 'col1', 'col2', 'col3', 'name')
        assert True
    val = _add_text(Image.open(SAMPLE), 'col1', 'col2', 'col3', 'name')
    assert type(val) == JpegImagePlugin.JpegImageFile
