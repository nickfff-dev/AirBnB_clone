# AirBnB Clone

## Project Description
This project is a simple clone of the AirBnB website and functionality.
This command-line console is designed for managing and persisting objects with an abstraction layer for storage. It enables you to create, update, destroy, and interact with objects in your data model via a command interpreter. The key features of this program include:

Creating your data model
Managing (create, update, destroy, etc.) objects via a console/command interpreter
Storing and persisting objects to a file (JSON file)
This repo will focus on the first stage. In this stage We implement a command line interface in the
file console.py to manipulate data.

## console.py
It works just like the shell but for specific AirBnB data maniuplation needs.
From the console you should be able to:
1. Create a new object (ex: a new User or a new Place).
2. Retrieve an object from a file, a database etc.
3. Do operations on objects (count, compute stats, etc).
4. Update attributes of an object.
5. Destroy an object.
6. view list of available commands with `help`

## Usage

### Interactive Mode
```
$ ./console.py
```

In interactive mode, you can use the help command to see a list of documented commands and quit to exit the console.
#### Example
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
### Non-Interactive Mode
You can also use the console in non-interactive mode by piping commands into the script or by providing a file containing commands.
#### Example
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```
