import random
from madras import MadrasNFT
from colors import *


def generator(*args, **kwargs):
    def ep():
        return random.choice([i for i in range(2, 40)])

    def points(side):
        return random.choice([i for i in range(1, side)])

    v_bands = [(points(kwargs['square_width']), ep()) for i in range(1, args[0])]
    h_bands = [(points(kwargs['square_height']), ep()) for j in range(1, args[1])]
    v_lines = [points(kwargs['square_width']) for k in range(1, args[2])]
    h_lines = [points(kwargs['square_height']) for l in range(1, args[3])]

    palette = []
    for key in kwargs.keys():
        if 'color' in key:
            palette.append(select_color_by_name(kwargs[key]))

    madras_nft = MadrasNFT(name='madrasnft',
                           square_width=kwargs['square_width'], square_height=kwargs['square_height'],
                           background=select_color_by_name(kwargs['background']),
                           palettes=palette)

    madras_nft.create(v_bands, h_bands, v_lines, h_lines)
    print(madras_nft.__repr__())


if __name__ == '__main__':
    generator(5, 4, 11, 8,
              color1='red', color2='blue', color3='yellow', color4='green',
              background='yellow',
              square_width=240,
              square_height=240)

    """
    v_bands = [(30, 5), (70, 40), (160, 10), (180, 10), (200, 10)]
    h_bands = [(40, 10), (80, 10), (160, 15), (200, 5)]
    v_lines = [12, 16, 40, 44, 120, 124, 150, 154, 212, 220, 224]
    h_lines = [100, 105, 115, 117, 140, 142, 220, 224]
    palette = [RED, RED, YELLOW, GREEN]

    madras_nft = MadrasNFT(name='madrasnft',
                           square_width=240, square_height=240,
                           background=WHITE,
                           palettes=palette)

    madras_nft.create(v_bands, h_bands, v_lines, h_lines)
    madras_nft.show()
    # print(madras_nft.compute_generated_shades())
    print(madras_nft.__repr__())
    """
