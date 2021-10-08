

class Color:
    def __init__(self, *args):
        self.name = args[0]
        self.shades = [args[i] for i in range(1, len(args))]

    def __repr__(self):
        return {'name': self.name,
                'shades': self.shades}

    def __str__(self):
        return self.__repr__().__str__()


WHITE = Color('white', (255, 255, 255), (244, 246, 245), (235, 235, 235))
RED = Color('red', (200, 65, 83), (164, 48, 63), (142, 41, 55))
ORANGE = Color('orange', (246, 144, 101), (244, 116, 59), (242, 89, 24))
YELLOW = Color('yellow', (255, 240, 31), (240, 225, 0), (204, 190, 0))
GREEN = Color('green', (85, 180, 139), (68, 156, 118), (56, 128, 97))
BLUE = Color('blue', (104, 120, 222), (61, 82, 213), (44, 65, 201))
PURPLE = Color('purple', (104, 30, 194), (104, 30, 194), (113, 33, 212))
BLACK = Color('black', (15, 16, 32), (7, 7, 14), (14, 14, 27))

GREY = Color('grey', (98, 142, 147))
PALETTE = [WHITE, RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE, BLACK]


def select_color(shade):
    si, color = -1, None
    for p in PALETTE:
        try:
            si, color = p.shades.index(shade), p
        except ValueError as v:
            pass
    return si if si != -1 else 0, color if si != -1 else GREY


def compute_shades(shade1, shade2):
    s1, color1 = select_color(shade1)
    s2, color2 = select_color(shade2)

    if color1 == color2:
        s = s2 if s1 <= s2 else s1
        color = color2 if s2 == s else color1
        return color.shades[s + 1 if s2 < len(color.shades) - 1 else len(color.shades) - 1]
    else:
        if color1 == RED and color2 == YELLOW or color2 == RED and color1 == YELLOW:
            return ORANGE.shades[0]
        elif color1 == RED and color2 == BLUE or color2 == RED and color1 == BLUE:
            return PURPLE.shades[0]
        elif color1 == BLUE and color2 == YELLOW or color2 == BLUE and color1 == YELLOW:
            return GREEN.shades[0]
        elif color1 == PURPLE and color2 == ORANGE or color2 == PURPLE and color1 == ORANGE:
            return RED.shades[0]
        elif color1 == PURPLE and color2 == GREEN or color2 == PURPLE and color1 == GREEN:
            return BLUE.shades[0]
        elif color1 == GREEN and color2 == ORANGE or color2 == GREEN and color1 == ORANGE:
            return YELLOW.shades[0]
        else:
            return color2.shades[s2 + 1 if s2 < len(color2.shades) - 1 else len(color2.shades) - 1]

