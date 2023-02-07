#!/usr/bin/python3
"""
Custom command line for AirBnB project
This module contains the entry point of the command interpreter
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Command Line Interpreter Class
    This module contains one class: `HBNBCommand()`
    """

    prompt = "(hbnb) "

    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Place": Place,
        "Amenity": Amenity,
        "Review": Review}

    def do_EOF(self, line):
        """Exit the program when user types EOF
        """
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def emptyline(self):
        """  """
        return False

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel
        saves it to the JSON file and prints id.
        If the class name doesn't exist, print ** class doesn't exist **
        If the class name is missing, print ** class name missing **
        """
        args = arg.split()
        if len(args) == 0 or arg is None:
            print("** class name missing **")
        else:
            if len(args) == 1 and args[0] in self.classes:
                new_instance = self.classes.get(args[0])()
                print(new_instance.id)
            else:
                print("** class doesn't exist **")
        storage.save()

    def do_show(self, arg):
        """
        Prints string representation of an instance
        based on the class name and id.
        If the instance doesn't exist for the id, print ** no instance found **
        If the id is missing, print ** instance id missing **
        If the class name doesn't exist, print ** class doesn't exist **
        If the class name is missing, print ** class name missing **
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1 and args[0] in self.classes:
            print("** instance id missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            instances = storage.all()
            instance_id = "{}.{}".format(args[0], args[1])
            try:
                print(instances[instance_id])
            except:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        save the change into the JSON file.
        If the instance doesn't exist for the id, print ** no instance found **
        If the id is missing, print ** instance id missing **
        If the class name doesn't exist, print ** class doesn't exist **
        If the class name is missing, print ** class name missing **
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1 and args[0] in self.classes:
            print("** instance id missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            instances = storage.all()
            instance_id = "{}.{}".format(args[0], args[1])
            try:
                del(instances[instance_id])
                storage.save()
            except:
                print("** no instance found **")

    def do_all(self, arg=""):
        """
        Prints all string representation of all instances
        based or not on the class name.
        If the class name doesn't exist, print ** class doesn't exist **
        """
        instances = storage.all()
        just_class = "empty list"
        if arg:
            # print specified instance
            if arg in self.classes:
                for key, value in instances.items():
                    if arg in key:
                        print(value)
                        just_class = "instances have been created!"
                if just_class == "empty list":
                    print("[]")
            else:
                print("** class doesn't exist **")
        else:
            # all with no argument, print all
            for value in instances.values():
                print(value)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute then save the change into the JSON file
        If the instance doesn't exist for the id, print ** no instance found **
        If the id is missing, print ** instance id missing **
        If the class name doesn't exist, print ** class doesn't exist **
        If the class name is missing, print ** class name missing **
        If the attribute name is missing, print ** attribute name missing **
        If the value for the attribute name doesn't exist,
           print ** value missing **
        """
        args = arg.split()
        instance_check = False
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            instances = storage.all()
            for key, value in instances.items():
                print("This is the key {}".format(key))
                if args[3][0] == "" and args[3][-1] == "":
                    args[3] = args[3][1:-1]
                instance_id = "{0}.{1}".format(args[0], args[1])
                if key == instance_id:
                    setattr(value, args[2], args[3])
                    storage.save()
                    instance_check = True
        if instance_check is False:
            print("** no instance found **")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
