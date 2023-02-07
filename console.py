#!/usr/bin/python3
""" Entry point of the command interpreter """

class HBNBCommand(cmd.Cmd):
    """
    A class that implements a command interpreter for a specific task.
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        Command to exit the program when the end of file is reached.
        """
        return True

    def help_quit(self):
        """
        Help documentation for the quit command.
        """
        print("Quit the command interpreter.")

    def emptyline(self):
        """
        Action that occurs when an empty line is entered.
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
