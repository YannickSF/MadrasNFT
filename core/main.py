
import os
from api.methods import generator


if __name__ == '__main__':
    for i in range(2):
        filecount = len([name for name in os.listdir('_collections/')])
        generator(name='_collections/madrasnft_{}'.format(filecount),
                  vertical_bands=5,
                  horizontal_bands=4,
                  vertical_lines=11,
                  horizontal_lines=8,
                  color1='red', color2='blue', color3='yellow', color4='green',
                  background='yellow',
                  square_width=240,
                  square_height=240)
