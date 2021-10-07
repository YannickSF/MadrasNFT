
import random
from PIL import Image, ImageDraw

SQUARE_WIDTH = 240
SQUARE_HEIGHT = 240

# COLOR PALETTE
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 189, 0)
ORANGE = (228, 144, 37)
RED = (243, 66, 19)
GREAT_RED = (174, 45, 9)
CYAN = (157, 217, 210)
DARK_CYAN = (152, 203, 180)
GREEN = (0, 255, 0)
GREAT_GREEN = (60, 136, 126)
PINK = (245, 221, 221)
PURPLE = (158, 0, 89)
BLUE = (0, 159, 253)
GREAT_BLUE = (0, 53, 89)

PRIMARY_1 = [YELLOW, ORANGE, RED, GREAT_RED]
PRIMARY_2 = [CYAN, DARK_CYAN, GREEN, GREAT_GREEN]
PRIMARY_3 = [PINK, PURPLE, BLUE, GREAT_BLUE]

PALETTE = [PRIMARY_1, PRIMARY_2, PRIMARY_3]


def compute_colors(color1, color2):

    def select_palette(color):
        for p in PALETTE:
            try:
                return p.index(color), p
            except ValueError as v:
                pass

    if color1 == WHITE:
        return color2
    if color2 == BLACK:
        return BLACK

    else:
        current_palette = None
        i1, p1 = select_palette(color1)
        i2, p2 = select_palette(color2)

        if p1 == p2:
            current_palette = p1
            if i1 < i2:
                return current_palette[i2]
            elif i1 == i2:
                if i1 == 3:
                    return current_palette[i1]
                else:
                    return current_palette[i1 + 1]
            elif i1 > i2:
                return current_palette[i1]
        else:
            current_palette = [p for p in PALETTE if p != p1 and p != p2][0]
            if i1 < i2:
                return current_palette[i2]
            elif i1 == i2:
                if i1 == 3:
                    return current_palette[i1]
                else:
                    return current_palette[i1 + 1]
            elif i1 > i2:
                return current_palette[i1]


def madras_nft(*args, **kwargs):

    def compute_coordonates(x, y, size):
        if x is not None:
            return x, 0, x + size, kwargs['square_width']

        if y is not None:
            return 0, y, kwargs['square_height'], y + size

    def draw_band(x, y, size, color=BLACK):
        coordonates = compute_coordonates(x, y, size)
        draw.rectangle(coordonates, fill=color)
        return coordonates

    def draw_lines(x=None, y=None, color=BLACK):
        x = x if not None else kwargs['square_width']
        y = y if not None else kwargs['square_height']
        coordonates = compute_coordonates(x, y, 0)

        draw.line(coordonates, fill=color)
        return coordonates

    def initialise_img_matrix(x_size, y_size, color=WHITE):
        for i in range(x_size):
            for j in range(y_size):
                img_matrix[i, j] = color

    def update_img_matrix(coordonates, color):
        if coordonates[0] != coordonates[2]:
            if coordonates[1] == coordonates[3]:
                for i in range(coordonates[0], coordonates[2]):
                    img_matrix[i, coordonates[1]] = compute_colors(img_matrix[i, coordonates[3]], color)
            else:
                for i in range(coordonates[0], coordonates[2]):
                    for j in range(coordonates[1], coordonates[3]):
                        img_matrix[i, j] = compute_colors(img_matrix[i, j], color)
        else:
            if coordonates[0] == coordonates[2]:
                for j in range(coordonates[1], coordonates[3]):
                    img_matrix[coordonates[0], j] = compute_colors(img_matrix[coordonates[0], j], color)

    def use_img_matrix():
        for a in range(kwargs['square_width']):
            for b in range(kwargs['square_height']):
                image.putpixel((a, b), img_matrix[a, b])

    def generate_meta_datas():
        pass

    img_matrix = {}
    image = Image.new('RGB', (kwargs['square_width'], kwargs['square_height']), kwargs['background'])
    initialise_img_matrix(kwargs['square_width'], kwargs['square_height'], kwargs['background'])
    draw = ImageDraw.Draw(image)

    # v bands
    for i in args[0]:
        color = random.choice(kwargs['palette'])
        update_img_matrix(draw_band(i[0], None, i[1], color), color)
    # h bands
    for j in args[1]:
        color = random.choice(kwargs['palette'])
        update_img_matrix(draw_band(None, j[0], j[1], color), color)
    # v lines
    for k in args[2]:
        color = random.choice(kwargs['palette'])
        update_img_matrix(draw_lines(k, None, color), color)
    # h lines
    for m in args[3]:
        color = random.choice(kwargs['palette'])
        update_img_matrix(draw_lines(None, m, color), color)

    # sprint([img_matrix[i, j] for i, j in img_matrix.keys() if img_matrix[i, j] == ORANGE])
    use_img_matrix()
    image.show()
    image.save("{0}.png".format(kwargs['name']), "png")


if __name__ == '__main__':
    v_bands = [(30, 5), (70, 40), (160, 10), (180, 10), (200, 10)]
    h_bands = [(40, 10), (80, 10), (160, 15), (200, 5)]
    v_lines = [12, 16, 40, 44, 120, 124, 150, 154, 212, 220, 224]
    h_lines = [100, 105, 115, 117, 140, 142, 220, 224]
    palette = [YELLOW, CYAN]

    madras_nft(v_bands, h_bands, v_lines, h_lines,
               name='madrasnft',
               square_width=SQUARE_WIDTH,
               square_height=SQUARE_HEIGHT,
               background=WHITE,
               palette=palette)
