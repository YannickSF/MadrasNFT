
from flask import Flask, request, send_file
from api.methods import generator, get_json, get_png, obj_pin, obj_upvote, wall_of_fame

app = Flask(__name__)


@app.route("/")
def index():
    return {'madras-api': 'live'}


@app.route("/generate", methods=['GET'])
def generate():
    payload = request.get_json()
    payload['square_width'] = 240
    payload['square_height'] = 240

    obj_rest = None
    try:
        obj_rest = generator(**payload)
    except Exception as e:
        return {'error': e.__str__()}

    return {'id': obj_rest.id}


@app.route("/png/<string:id>", methods=['GET'])
def png(id):
    return send_file(get_png(id), mimetype='image/png')


@app.route("/json/<string:id>", methods=['GET'])
def json(id):
    return get_json(id)


@app.route("/pin/<string:id>", methods=['GET'])
def pin(id):
    payload = request.get_json()
    return {'state': obj_pin(id, payload['username'])}


@app.route("/upvote/<string:id>", methods=['GET'])
def upvote(id):
    return {'state': obj_upvote(id)}


@app.route("/wall", methods=['GET'])
def wall():
    return {'wall': wall_of_fame()}


if __name__ == '__main__':
    app.run(host='0.0.0.0')