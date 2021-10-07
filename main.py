
from madras import MadrasNFT
from palette import *


if __name__ == '__main__':
    v_bands = [(30, 5), (70, 40), (160, 10), (180, 10), (200, 10)]
    h_bands = [(40, 10), (80, 10), (160, 15), (200, 5)]
    v_lines = [12, 16, 40, 44, 120, 124, 150, 154, 212, 220, 224]
    h_lines = [100, 105, 115, 117, 140, 142, 220, 224]
    palette = [RED, BLUE]

    madras_nft = MadrasNFT(name='madrasnft',
                           square_width=240, square_height=240,
                           background=GREEN,
                           palettes=palette)

    madras_nft.create(v_bands, h_bands, v_lines, h_lines)
    madras_nft.show()
    print(madras_nft.compute_generated_shades())
