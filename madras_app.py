
from flask import Flask, request, send_file
from flask_cors import CORS
from api.methods import generator, item_by_id, get_png, obj_pin, wall_of_fame

app = Flask(__name__)
cors = CORS(app)


@app.route("/")
def index():
    return {'madras-api': 'live'}


@app.route("/generate", methods=['GET'])
def generate():

    payload = {k: request.values[k] for k in request.values.keys() if 'responseType' not in k}
    payload['colors'] = payload['colors'].split(',')

    payload['square_width'] = 480
    payload['square_height'] = 480

    obj_rest = None
    try:
        obj_rest = generator(**payload)
    except Exception as e:
        return {'error': e.__str__()}

    return {'id': obj_rest.id}


@app.route("/images/<string:id>", methods=['GET'])
def image_by_id(id):
    return send_file(get_png(id))


@app.route("/item/<string:id>", methods=['GET'])
def item(id):
    return {'item': item_by_id(id).__repr__()}


@app.route("/pin/<string:id>", methods=['GET'])
def pin(id):
    payload = {k: request.values[k] for k in request.values.keys()}
    return {'state': obj_pin(id, payload['username'])}


@app.route("/wall", methods=['GET'])
def wall():
    return {'wall': wall_of_fame()}


if __name__ == '__main__':
    app.run(host='0.0.0.0')
