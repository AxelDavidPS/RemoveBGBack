from flask import Blueprint
from routes.imgs import bp_img

router = Blueprint('APIprefix',__name__,url_prefix="/api/v1")

router.register_blueprint(bp_img,url_prefix="/img")
