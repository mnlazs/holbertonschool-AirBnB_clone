#!/usr/bin/python3
import json
import os
import models
'''
This is the file_storage module.
file_storage contains one class: FileStorage; two private attributes:
file_path, objects; and four instances: all, new, save, reload.
'''


class FileStorage:
    """Esta clase llamada FileStorage \
        incluida la ruta del archivo-objeto \ 
        y la lista _objects donde se almacenan \ 
        """
    __file_path = 'hbnb.json'
    __objects = {}

    def all(self):
        """Estos son todos los metodos de instancia publica
        """
        return FileStorage.__objects

    def new(self, obj):
        """Esta es la instancia 'new'.
        Sets __object as @obj with key obj.id
        @obj: object
        """
        FileStorage.__objects[obj.id] = obj

    def save(self):
        """Esta es la instancia 'save'.\
        Serializa el __objeto a un archivo JSON\
        Return: JSON file\
        """
        new_dict = {}
        for key in FileStorage.__objects.keys():
            new_dict[key] = FileStorage.__objects[key].to_json()
        with open(FileStorage.__file_path, 'w+', encoding='utf-8') as fn:
            json.dump(new_dict, fn)

    def reload(self):
        """Instancia 'reload'.
        Deserializes the JSON file to __objects.
        If JSON file does not exist, do nothing.
        Return: __object or nothing
        """
        if os.path.isfile(FileStorage.__file_path) is True:
            with open(FileStorage.__file_path, 'r+', encoding='utf-8') as fn:
                obj = json.load(fn)
                for key in obj.keys():
                    is_dict = obj[key]
                    is_class = is_dict['__class__']
                    if 'BaseModel' in is_class:
                        FileStorage.__objects[key] = models.BaseModel(obj[key])
                    if 'Amenity' in is_class:
                        FileStorage.__objects[key] = models.Amenity(obj[key])
                    if 'City' in is_class:
                        FileStorage.__objects[key] = models.City(obj[key])
                    if 'Place' in is_class:
                        FileStorage.__objects[key] = models.Place(obj[key])
                    if 'Review' in is_class:
                        FileStorage.__objects[key] = models.Review(obj[key])
                    if 'State' in is_class:
                        FileStorage.__objects[key] = models.State(obj[key])
                    if 'User' in is_class:
                        FileStorage.__objects[key] = models.User(obj[key])
