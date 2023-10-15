"""This module contains an entry point of command interpreter"""

import sys
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """class definition of the command interpreter"""

    prompt = "(hbnb) "

    __classes = {
            "BaseModel",
            "User",
            "Place",
            "State",
            "City",
            "Amenity",
            "Review"
            }

    def do_EOF(self, line):
        """Exits the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """command to do nothing when user press enter"""
        pass

    def do_create(self, cls_name):
        """ Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id.
        args: cls_name - the class name
        """
        if cls_name:
            if cls_name in HBNBCommand.__classes:
                instance = globals()[cls_name]()
                storage.new(instance)
                storage.save()
                print("{}".format(instance.id))
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, line):
        """ Prints the string representation of an instance
        based on the class name and id
        """
        args = line.split()
        objects = storage.all()
        if not args:
            print("** class name missing **")
            return
        cls_name = args[0]
        if cls_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        id_no = args[1]
        instance_key = "{}.{}".format(cls_name, id_no)
        if instance_key not in objects:
            print("** no instance found **")
        else:
            print(objects[instance_key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)"""

        args = line.split()
        objects = storage.all()

        if not args:
            print("** class name missing **")
            return
        cls_name = args[0]
        if cls_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        id_no = args[1]
        instance_key = "{}.{}".format(cls_name, id_no)
        if instance_key not in objects:
            print("no instance found")
        else:
            del objects["{}.{}".format(cls_name, id_no)]
            storage.save()

    def do_all(self, cls_name):
        """Prints all string representation of all instances
        based or not on the class name.
        args: cls_name - class name
        """

        if cls_name and cls_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            str_rep = []
            for obj in storage.all().values():
                if cls_name and cls_name == obj.__class__.__name__:
                    str_rep.append(obj.__str__())
                else:
                    str_rep.append(obj.__str__())
            print(str_rep)

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file).
        """
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        cls_name = args[0]
        if cls_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        objects = storage.all()
        key = "{}.{}".format(cls_name, obj_id)
        if key not in objects:
            print("** no instance found **")
            return
        attr_name = args[2]
        if len(args) < 3:
            print("** attribute name missing **")
            return
        attr_value = args[3]
        if len(args) < 4:
            print("** value missing **")
            return
        instance = objects[key]
        if not hasattr(instance, attr_name):

            setattr(instance, attr_name, (attr_value))
        else:
            attr_type = type(getattr(instance, attr_name))
            if attr_type == str:
                attr_value = str(attr_value)
            elif attr_type == int:
                attr_value = int(attr_value)
            elif attr_type == float:
                attr_value = float(attr_value)
            setattr(instance, attr_name, attr_value)
        storage.save()

    def postloop(self):
        """called after the loop as finished"""
        if not sys.stdin.isatty():
            print()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
