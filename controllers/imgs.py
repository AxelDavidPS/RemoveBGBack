from flask import jsonify, make_response
from models.img import Img_model

class Img_controller():

    @classmethod
    def del_bg(cls):
        response_model, status = Img_model.del_bg()
        response = make_response(jsonify(response_model),status)
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response

