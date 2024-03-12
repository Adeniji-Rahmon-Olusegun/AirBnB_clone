#!/usr/bin/python3
"""This module is the console framwork of this project"""

import cmd
import shlex
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """This class is the CLI for testing and others"""

    prompt = "(hbnb) "
    acceptable_classes = ["BaseModel"]

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

        if line[0] not in self.acceptable_classes:
            print("** class doesn't exist **")
            return
        
        if len(line) < 2:
            print("** instance id missing **")
            return

        try:
            inst = storage.all()[f"{line[0]}.{line[1]}"]
            print(inst)
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        line = shlex.split(line)

        if not line:
            print("** class name missing **")
            return

        if line[0] not in self.acceptable_classes:
            print("** class doesn't exist **")
            return

        if len(line) < 2:
            print("** instance id missing **")
            return

        try:
            key = f"{line[0]}.{line[1]}"
            del storage.all()[key]
            storage.save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, line):
        """
        Prints all string representation of all instances based
        or not on the class name.
        """

        line = shlex.split(line)
        
        objs = storage.all()

        if not line:
            for value in objs.values():
                print(str(value))
        elif line[0] not in self. acceptable_classes:
            print("** class doesn't exist **")
        else:
            for key, value in objs.items():
                if key.split('.')[0] == line[0]:
                    print(str(value))

    def do_update(self, line):
        """ Updates an instance based on the class name and id
        by adding or updating attribute 
        (save the change into the JSON file)
        """

        line = shlex.split(line)

        if not line:
            print("** class name missing **")
            return

        if line[0] not in self.acceptable_classes:
            print("** class doesn't exist **")
            return

        if len(line) < 2:
            print("** instance id missing **")
            return

        objs = storage.all()
        key = f"{line[0]}.{line[1]}"

        if key not in objs:
            print("** no instance found **")
        elif len(line) < 3:
            print("** attribute name missing **")
        elif len(line) < 4:
            print("** value missing **")
        else:
            obj = objs[key]

            try:
                line[3] = eval(line[3])
            except Exception:
                pass

            setattr(obj, line[2], line[3])
            
            obj.save()

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
