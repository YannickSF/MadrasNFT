import json
import os
import random
from api.db import Table, Query
from core.colors import *
from core.madras import MadrasNFT
from api.objects import MadrasRest

DB = Table('index')


def generator(**kwargs):
    kwargs['vertical_bands'] = int(kwargs['vertical_bands'])
    kwargs['horizontal_bands'] = int(kwargs['horizontal_bands'])
    kwargs['vertical_lines'] = int(kwargs['vertical_lines'])
    kwargs['horizontal_lines'] = int(kwargs['horizontal_lines'])

    def ep():
        return random.choice([i for i in range(2, 40)])

    def points(side):
        return random.choice([i for i in range(0, side - 40)])

    v_bands = [(points(kwargs['square_width']), ep()) for i in range(kwargs['vertical_bands'])]
    h_bands = [(points(kwargs['square_height']), ep()) for j in range(kwargs['horizontal_bands'])]
    v_lines = [points(kwargs['square_width']) for k in range(kwargs['vertical_lines'])]
    h_lines = [points(kwargs['square_height']) for l in range(kwargs['horizontal_lines'])]

    palette = []
    for color in kwargs['colors']:
        palette.append(select_color_by_name(color))

    filecount = len([name for name in os.listdir('static/')])
    kwargs['name'] = 'madrasnft_{}'.format(filecount)

    madras_nft = MadrasNFT(name=kwargs['name'],
                           square_width=kwargs['square_width'], square_height=kwargs['square_height'],
                           background=select_color_by_name(kwargs['background']),
                           palettes=palette)

    madras_nft.create_png(v_bands, h_bands, v_lines, h_lines)
    madras_nft.create_json()

    madras_rest = MadrasRest(name=madras_nft.name)
    DB.insert(madras_rest.__repr__())
    return madras_rest


def get_png(id=None, name=None):
    q = Query()
    if id is not None:
        robj = DB.search(q.id == id)
    elif name is not None:
        robj = DB.search(q.name == name)
    else:
        return None

    if len(robj) == 0:
        return {}
    return MadrasRest(**robj[0]).png


def get_json(id=None, name=None):
    q = Query()
    if id is not None:
        robj = DB.search(q.id == id)
    elif name is not None:
        robj = DB.search(q.name == name)
    else:
        return None
    if len(robj) == 0:
        return {}

    try:
        with open(MadrasRest(**robj[0]).json, 'r') as data:
            return json.load(data)
    except Exception as e:
        return None


def obj_pin(id, username):
    q = Query()
    robj = DB.search(q.id == id)
    if len(robj) == 0:
        return {}

    mr = MadrasRest(**robj[0])
    mr.username = username
    mr.status = 'pin'
    DB.update(mr.__repr__(), q.id == id)
    return True


def obj_upvote(id):
    q = Query()
    robj = DB.search(q.id == id)
    if len(robj) == 0:
        return {}

    mr = MadrasRest(**robj[0])
    mr.votes += 1
    DB.update(mr.__repr__(), q.id == id)
    return True


def wall_of_fame():
    q = Query()
    return DB.search(q.status == 'pin')
