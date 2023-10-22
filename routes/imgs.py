from flask import Blueprint
from controllers.imgs import Img_controller

bp_img = Blueprint('img', __name__)


@bp_img.route("/", methods=['POST'])
@bp_img.route("", methods=['POST'])
def img_post():
    return Img_controller.del_bg()
