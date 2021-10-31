
from api.methods import generator


if __name__ == '__main__':

    def get_background(i):
        if i < 20:
            return 'white'
        if (i >= 20) and (i < 40):
            return 'yellow'
        if (i >= 40) and (i < 60):
            return 'red'
        if (i >= 60) and (i < 80):
            return 'blue'
        if i >= 80:
            return 'black'

    print('start factoring')
    for i in range(101):
        payload = {'background': get_background(i),
                   'square_width': 480,
                   'square_height': 480,
                   'vertical_bands': 6,
                   'horizontal_bands': 6,
                   'vertical_lines': 12,
                   'horizontal_lines': 12,
                   'colors': ['yellow', 'yellow', 'yellow', 'yellow',  'yellow', 'blue', 'blue', 'blue', 'red', 'red']}

        obj_rest = generator(**payload)

    print('end factoring')
