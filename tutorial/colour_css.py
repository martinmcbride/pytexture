# Author:  Martin McBride
# Created: 2021-04-19
# Copyright (C) 2021, Martin McBride
# License: MIT

from generativepy.drawing import make_image, setup
from generativepy.color import Color
from generativepy.geometry import Rectangle


def draw_css(ctx, pixel_width, pixel_height, frame_no, frame_count):
    setup(ctx, pixel_width, pixel_height, background=Color('cornflowerblue'))

    pos = [10, 10]
    w = 100
    h = 100

    Rectangle(ctx).of_corner_size(pos, w, h).fill(Color("salmon"))
    pos[0] += w
    Rectangle(ctx).of_corner_size(pos, w, h).fill(Color("gold"))
    pos[0] += w
    Rectangle(ctx).of_corner_size(pos, w, h).fill(Color("seagreen"))
    pos[0] += w
    Rectangle(ctx).of_corner_size(pos, w, h).fill(Color("cadetblue"))
    pos[0] += w
    Rectangle(ctx).of_corner_size(pos, w, h).fill(Color("slateblue"))
    pos[0] += w
    Rectangle(ctx).of_corner_size(pos, w, h).fill(Color("darkorchid"))
    pos[0] += w
    Rectangle(ctx).of_corner_size(pos, w, h).fill(Color("hotpink"))
    pos[0] += w


make_image("colour-css.png", draw_css, 720, 120)
