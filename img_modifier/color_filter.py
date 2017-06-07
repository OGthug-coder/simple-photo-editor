"""
Apply filters to PIL.image
"""

from PIL import ImageDraw
import logging

logger = logging.getLogger()


class ColorFilters:
    filters = {"sepia": "Sepia", "negative": "Negative", "black_white": "Black & White"}
    SEPIA, NEGATIVE, BLACK_WHITE = filters.keys()


def _sepia(img):
    pix = img.load()
    draw = ImageDraw.Draw(img)
    for i in range(img.width):
        for j in range(img.height):
            s = sum(pix[i, j]) // 3
            k = 30
            draw.point((i, j), (s+k*2, s+k, s))


def _black_white(img):
    pix = img.load()
    draw = ImageDraw.Draw(img)
    for i in range(img.width):
        for j in range(img.height):
            s = sum(pix[i, j]) // 3
            draw.point((i, j), (s, s, s))


def _negative(img):
    pix = img.load()
    draw = ImageDraw.Draw(img)
    for i in range(img.width):
        for j in range(img.height):
            draw.point((i, j), (255 - pix[i, j][0], 255 - pix[i, j][1], 255 - pix[i, j][2]))


def color_filter(img, filter_name):
    img_copy = img.copy()
    if filter_name == ColorFilters.SEPIA:
        _sepia(img_copy)
    elif filter_name == ColorFilters.NEGATIVE:
        _negative(img_copy)
    elif filter_name == ColorFilters.BLACK_WHITE:
        _black_white(img_copy)
    else:
        logger.error(f"can't find filter {filter_name}")
        raise ValueError(f"can't find filter {filter_name}")

    return img_copy
