#!/usr/bin/python3
"""This module is the console framwork of this project"""

import cmd


class HBNBCommand(cmd.Cmd):
    """This class is the CLI for testing and others"""

    prompt = "(hbnb) "

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
