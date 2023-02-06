#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Called when an empty line is entered, does nothing"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
