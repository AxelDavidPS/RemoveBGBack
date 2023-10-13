import awsgi
from flask import Flask, jsonify, make_response
from server.server import router

app = Flask(__name__)

app.register_blueprint(router)


@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Not found!'), 404)


def handler(event, context):
    return awsgi.response(app, event, context, base64_content_types={"image/png"})

if __name__ == "__main__":
    app.run(debug=True)
