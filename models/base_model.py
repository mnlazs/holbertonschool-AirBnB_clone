#!/usr/bin/python3
import uuid
import models
from datetime import datetime

"""
Este es el modulo 'base_model'\
base_model contiene una clase llamada: 'BaseModel' \
BaseModel contienene los siguientes metodos: 'init', 'save', 'to_json', 'str'.\
"""


class BaseModel:
    """This is the BaseModel class.
    """
    def __init__(self, *args, **kwargs):
        """__init__ metodo de iniciacion que asigna los siguientes atributos:\
            'id', 'created_at', 'updated_at'
        """
        if len(args) > 0:
            if type(args[0]) is dict:
                self.__dict__ = args[0]
                self.__dict__['created_at'] = datetime.strptime(
                    (self.__dict__['created_at']), "%Y-%m-%d %H:%M:%S.%f")
                self.__dict__['updated_at'] = datetime.strptime(
                    (self.__dict__['updated_at']), "%Y-%m-%d %H:%M:%S.%f")
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
