# AirBnB Clone Command Interpreter

## Description of the project

This project is part of the AirBnB clone series and aims to create a command-line interface (CLI) for managing AirBnB objects. The command interpreter allows users to perform various operations such as creating, retrieving, updating, and deleting objects like User, State, City, Place, etc., which are essential for the functionality of the AirBnB clone.

## Description of the command interpreter

The command interpreter provides a shell-like interface where users can interact with the AirBnB objects using various commands. These commands allow users to manipulate objects, query data, and perform other operations related to the AirBnB application.

### How to start it

To start the command interpreter, simply run the `console.py` script. This will launch the CLI and provide a prompt where commands can be entered.

```bash
$ python console.py
```

### How to use it

Once the command interpreter is running, users can enter commands to interact with AirBnB objects. The commands follow a specific syntax and allow users to perform various operations like creating, retrieving, updating, and deleting objects.

#### Command syntax

The general syntax for commands is as follows:

```
command_name [options] [arguments]
```

#### Available commands

- **create**: Create a new object of a specified type.
- **show**: Display details of a specific object.
- **destroy**: Delete a specified object.
- **update**: Update attributes of a specified object.
- **all**: Retrieve all objects of a specified type or all objects if no type is specified.
- **quit/EOF**: Exit the command interpreter.

### Examples

#### Creating a new user

```
(hbnb) create User
```

#### Showing details of a user

```
(hbnb) show User 12345
```

#### Updating attributes of a user

```
(hbnb) update User 12345 email "example@example.com"
```

#### Deleting a user

```
(hbnb) destroy User 12345
```

#### Retrieving all users

```
(hbnb) all User
```
