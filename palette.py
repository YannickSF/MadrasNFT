
# COLOR PALETTE
BLACK = [(15, 16, 32), (7, 7, 14), (14, 14, 27)]
GREY = [(98, 142, 147), (0, 0, 0), (0, 0, 0)]
WHITE = [(255, 255, 255), (244, 246, 245), (235, 235, 235)]

PRIMARY = [WHITE, GREY, BLACK]

RED = [(200, 65, 83), (164, 48, 63), (142, 41, 55)]
ORANGE = [(246, 144, 101), (244, 116, 59), (242, 89, 24)]
YELLOW = [(255, 240, 31), (240, 225, 0), (204, 190, 0)]
GREEN = [(85, 180, 139), (68, 156, 118), (56, 128, 97)]
BLUE = [(104, 120, 222), (61, 82, 213), (44, 65, 201)]
PURPLE = [(104, 30, 194), (104, 30, 194), (113, 33, 212)]

PRIMARY_1 = [RED, ORANGE]
PRIMARY_2 = [YELLOW, GREEN]
PRIMARY_3 = [BLUE, PURPLE]

PALETTE = [PRIMARY_1, PRIMARY_2, PRIMARY_3]


def select_palette(color):
    if color == WHITE:
        return 0, PRIMARY
    if color == GREY:
        return 1, PRIMARY
    if color == BLACK:
        return 2, PRIMARY

    for p in PALETTE:
        for c in p:
            try:
                return p.index(color), p
            except ValueError as v:
                pass


def select_third_palette(p1, p2):
    p3 = None
    for p in PALETTE:
        if p != p1 or p != p2:
            p3 = p
    return p3


def select_color(shade):
    if shade in WHITE:
        return 0, WHITE
    if shade in BLACK:
        return 0, BLACK

    for p in PALETTE:
        for c in p:
            try:
                return c.index(shade), c
            except ValueError as v:
                return 0, GREY


def compute_colors(shade1, shade2):
    s1, color1 = select_color(shade1)
    s2, color2 = select_color(shade2)

    if color1 == WHITE:
        return shade2
    if color1 == BLACK:
        return color2[s2 + 1 if s2 < len(color2) - 1 else len(color2) - 1]
    if color2 == WHITE:
        return color1[s1 - 1 if s1 > 0 else 0]
    if color2 == BLACK:
        return BLACK[0]

    c1, palette1 = select_palette(color1)
    c2, palette2 = select_palette(color2)

    if palette1 == palette2:
        color_return = color2[s2 + 1 if s2 < len(color2) - 1 else len(color2) - 1]

    else:
        if c1 == c2 == 0:
            color_return = palette2[c2 + 1 if c2 < len(palette2) - 1 else len(palette2) - 1]
        elif c1 == c2 == len(PRIMARY_1) - 1:
            p3 = select_third_palette(palette1, palette2)
            color_return = p3[0]
        elif c1 < c2:
            color_return = palette2[c2 + 1 if c2 < len(palette2) - 1 else len(palette2) - 1]
        elif c1 > c2:
            color_return = palette1[c1 + 1 if c1 < len(palette1) - 1 else len(palette1) - 1]
        else:
            print(c1, c2, color1, color2)
            color_return = GREY

    return color_return[0]
