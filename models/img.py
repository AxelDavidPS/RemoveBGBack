from flask import request

class Img_model():

    @classmethod
    def del_bg(cls):
        print(request)
        body = {
            'message':'Hello from img',
            'respuesta_modelo': 'aqui hacemos algo y retornamos el mensaje del objeto'
        }
        return body



