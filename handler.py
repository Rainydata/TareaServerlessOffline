import json


def hello(event, context):
    body = {
        "Nombre": "Bryan Alejandro",
        "Apellido": "Benavides Gallego",
        "Cedula": "1004701942",
        "Direccion": "Calle 123 num 24-11",
        "Telefono": "3104365446",
        "Correo": "benavides.bryan.0194@eam.edu.co",
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
