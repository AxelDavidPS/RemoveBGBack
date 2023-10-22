from flask import request
from PIL import Image
from rembg import remove
import io
import base64

class Img_model():

    @classmethod
    def del_bg(cls):
        try:
            imagen = request.files['file']
            img = Image.open(imagen)
            img_without_bg = remove(img)
            buffered = io.BytesIO()
            img_without_bg.save(buffered, format='PNG')
            img_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')

            body = {
                'success':True,
                'img': img_base64
            }
            return body,200

        except Exception as e:
            body = {
                'success': False,
                "error": e.message
            }
            return body,500
