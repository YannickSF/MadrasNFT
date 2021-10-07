
import random
from PIL import Image, ImageDraw
from palette import *


class MadrasNFT:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.palettes = kwargs['palettes']
        self.square_width = kwargs['square_width']
        self.square_height = kwargs['square_height']
        self.background = kwargs['background']

        self.img_matrix = {}
        self.image = Image.new('RGB', (kwargs['square_width'], kwargs['square_height']), kwargs['background'][0])
        self.initialise_img_matrix(kwargs['square_width'], kwargs['square_height'], kwargs['background'][0])
        self.draw = ImageDraw.Draw(self.image)

    def compute_coordonates(self, x, y, size):
        if x is not None:
            return x, 0, x + size, self.square_width

        if y is not None:
            return 0, y, self.square_height, y + size

    def draw_band(self, x, y, size, b_shade=None):
        b_coordonates = self.compute_coordonates(x, y, size)
        self.draw.rectangle(b_coordonates, fill=b_shade)
        return b_coordonates

    def draw_lines(self, x=None, y=None, l_shade=None):
        x = x if not None else self.square_width
        y = y if not None else self.square_height
        l_coordonates = self.compute_coordonates(x, y, 0)

        self.draw.line(l_coordonates, fill=l_shade)
        return l_coordonates

    def initialise_img_matrix(self, x_size, y_size, shade):
        for g in range(x_size):
            for h in range(y_size):
                self.img_matrix[g, h] = shade

    def update_img_matrix(self, coordonates, u_shade):
        if coordonates[0] != coordonates[2]:
            if coordonates[1] == coordonates[3]:
                for i in range(coordonates[0], coordonates[2]):
                    self.img_matrix[i, coordonates[1]] = compute_colors(self.img_matrix[i, coordonates[3]], u_shade)
            else:
                for k in range(coordonates[0], coordonates[2]):
                    for j in range(coordonates[1], coordonates[3]):
                        self.img_matrix[k, j] = compute_colors(self.img_matrix[k, j], u_shade)
        else:
            if coordonates[0] == coordonates[2]:
                for t in range(coordonates[1], coordonates[3]):
                    self.img_matrix[coordonates[0], t] = compute_colors(self.img_matrix[coordonates[0], t], u_shade)

    def use_img_matrix(self):
        for a in range(self.square_width):
            for b in range(self.square_height):
                self.image.putpixel((a, b), self.img_matrix[a, b])

    def create(self, *args):
        # v bands
        for m in args[0]:
            color = random.choice(self.palettes)
            self.update_img_matrix(self.draw_band(m[0], None, m[1], color[0]), color[0])

        # h bands
        for n in args[1]:
            color = random.choice(self.palettes)
            self.update_img_matrix(self.draw_band(None, n[0], n[1], color[0]), color[0])

        # v lines
        for o in args[2]:
            color = random.choice(self.palettes)
            self.update_img_matrix(self.draw_lines(o, None, color[0]), color[0])

        # h lines
        for p in args[3]:
            color = random.choice(self.palettes)
            self.update_img_matrix(self.draw_lines(None, p, color[0]), color[0])

        self.use_img_matrix()
        self.image.save("{0}.png".format(self.name), "png")

    def show(self):
        self.image.show()

    def compute_generated_shades(self):
        computed = {}
        full_palette = PRIMARY + PRIMARY_1 + PRIMARY_2 + PRIMARY_3
        for color in full_palette:
            found = [self.img_matrix[i, j] for i, j in self.img_matrix.keys() if self.img_matrix[i, j] in color]
            if len(found) > 0:
                computed[color[0]] = len(found)

        return computed

    def __repr__(self):
        return {'name': self.name,
                'width': self.square_width,
                'height': self.square_height,
                'background': self.background,
                'palette': self.palettes}

    def __str__(self):
        return self.__repr__().__str__()
