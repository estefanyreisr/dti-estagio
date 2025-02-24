from cerberus import Validator

def book_creator_validator(request: any):
    body_validator = Validator({
        "data": {
            "type": "dict",
            "schema": {
                "titulo": {"type": "string", "required": True, "empty": False},
                "autor": {"type": "string", "required": True, "empty": False},
                "genero": {"type": "string"},
                "editora": {"type": "string"},
                "numero_paginas": {"type": "integer"},
                "data_lancamento": {"type": "string"},
            }
        }
    })
    
    response = body_validator.validate(request.json)
    
    if response is False:
        raise Exception(body_validator.errors)