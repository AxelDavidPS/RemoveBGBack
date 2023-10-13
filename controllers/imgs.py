from flask import jsonify, make_response
from models.img import Img_model

class Img_controller():

    @classmethod
    def del_bg(cls):
        response_model = Img_model.del_bg()
        return make_response(jsonify(response_model),200)

