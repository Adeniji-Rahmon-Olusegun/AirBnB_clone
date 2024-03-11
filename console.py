#!/usr/bin/python3
"""This module is the console framwork of this project"""

import cmd
import shlex
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """This class is the CLI for testing and others"""

    prompt = "(hbnb) "

    def do_create(self, line):
        """Creates new instance of BaseModel, saves and prints id"""
        
        line = shlex.split(line)
        
        if not line:
            print("** class name missing **")
            return
        
        class_ = line[0]

        try:
            instance = eval(class_)()
            instance.save()
            print(instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Prints string repr of instance based on class name & id"""
        line = shlex.split(line)

        if not line:
            print("** class name missing **")
            return
        
        if len(line) < 2:
            print("** instance id missing **")
            return

        class_, inst_id = line[0], line[1]
        
        if class_ not in globals():
            print("** class doesn't exist **")
            return

        try:
            inst = storage.all()[f"{class_}.{inst_id}"]
            print(inst)
        except KeyError:
            print("** no instance found **")

    def destroy(self, line):
        """Deletes an instance based on the class name and id"""
        line = shlex.split(line)

        if not line:
            print("** class name missing **")
            return

        if len(line) < 2:
            print("** instance id missing **")
            return
        class_, inst_id = line[0], line[1]

        if class_ not in globals():
            print("** class doesn't exist **")
            return

        try:
            inst = storage.all()[f"{class_}.{inst_id}"]
            del inst
        except KeyError:
            print("** no instance found **")

    def do_all(self, line):
        """
        Prints all string representation of all instances based
        or not on the class name.
        """

        line = shlex.split(line)

        if line:
            class_ = line[0]
            if class_ not in globals():
                print("** class doesn't exist **")
                return
            
        inst_list = [
            str(inst) for inst in storage.all().values()
            if not class_ or isinstance(inst, eval(class_))
        ]
        print(inst_list)

    def do_update(self, line):
        """ Updates an instance based on the class name and id
        by adding or updating attribute 
        (save the change into the JSON file)
        """

        line = shlex.split(line)

        if not line:
            print("** class name missing **")
            return

        if line:
            if class_ not in globals():
                print("** class doesn't exist **")
                return

        if len(line) < 2:
            print("** instance id missing **")
            

    def emptyline(self):
        """Emptyline shouldn't execute anything"""
        pass

    def do_quit(self, line):
        """Quit command to exit the program\n\n"""
        return True

    def do_EOF(self, line):
        """Exits the program"""
        return True


if __name__ == "__main__":

    import sys

    if len(sys.argv) > 1:
        HBNBCommand().onecmd(' '.join(sys.argv[1:]))
    else:
        HBNBCommand().cmdloop()
