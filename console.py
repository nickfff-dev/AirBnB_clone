#!/usr/bin/python3
"""
Module defines HBNBCommand class that includes methods for quit, EOF, and help.
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class that includes methods for quit, EOF, and help.
    """

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program
        """
        return True

    def emptyline(self):
        """
        An empty line + ENTER shouldn’t execute anything
        """
        pass

    def help_quit(self):
        print("Quit command to exit the program")

    def help_EOF(self):
        print("EOF command to exit the program")

    def default(self, line):
        """
        Method called on an input line when the
        command prefix is not recognized.
        In this case it will be used to handle
        <class name>.all() commands.
        """
        if '.' in line:
            args = line.split('.')
            class_name = args[0]
            if class_name in ['BaseModel', 'User', 'Place', 'Amenity',
                              'City', 'State', 'Review']:
                objs = storage.all()
                class_objs = {k: v for k, v in objs.items()
                              if k.split('.')[0] == class_name}
                if 'all()' in line:
                    print("[", end="")
                    first = True
                    for v in class_objs.values():
                        if not first:
                            print(", ", end="")
                        print(v, end="")
                        first = False
                    print("]")
                elif 'count()' in line:
                    print(len(class_objs))
                elif 'show(' in line and ')' in line:
                    id = args[1].split('(')[1].strip(')"')
                    if id:
                        key = class_name + "." + id
                        if key in class_objs:
                            print(class_objs[key])
                        else:
                            print("** no instance found **")
                    else:
                        print("** no instance found **")
                elif 'destroy(' in line and ')' in line:
                    id = args[1].split('(')[1].strip(')"')
                    if id:
                        key = class_name + "." + id
                        obj_dict = storage.all()
                        try:
                            if key in obj_dict:
                                del obj_dict[key]
                                storage.save()
                            else:
                                print("** no instance found **")
                        except KeyError:
                            print("** no instance found **")
                            pass
                    else:
                        print("** no instance found **")
                elif 'update(' in line and ')' in line:
                    id = args[1].split('(')[1].split(',')[0].strip(')"')
                    if id:
                        key = class_name + "." + id
                        if key in class_objs:
                            if '{' in line:
                                dict_str = \
                                    line.split('{', 1)[1].rsplit('}', 1)[0]
                                try:
                                    dict_repr = {k.strip(' "\''):
                                                 v.strip(' "\'') for k, v in
                                                 (item.split(':') for item in
                                                  dict_str.split(','))}
                                except ValueError:
                                    print("** attribute name missing **")
                                    return
                                for attr, value in dict_repr.items():
                                    if attr:
                                        if attr not in ['id', 'created_at',
                                                        'updated_at']:
                                            if value:
                                                try:
                                                    value = int(value)
                                                except ValueError:
                                                    try:
                                                        value = float(value)
                                                    except ValueError:
                                                        value = \
                                                            value.strip(' "\'')
                                                setattr(class_objs[key],
                                                        attr, value)
                                            else:
                                                print("** value missing **")
                                                continue
                                    else:
                                        print("** attribute name missing **")
                                        continue
                                storage.save()
                            else:
                                try:
                                    attr_name = \
                                        args[1].split(',')[1].strip(' "\'')
                                except IndexError:
                                    print("** attribute name missing **")
                                    return
                                try:
                                    attr_value = \
                                        args[1].split(',')[2].strip(' "\')')
                                except IndexError:
                                    print("** value missing **")
                                    return
                                if attr_name:
                                    if attr_name not in ['id', 'created_at',
                                                         'updated_at']:
                                        if attr_value:
                                            try:
                                                attr_value = int(attr_value)
                                            except ValueError:
                                                try:
                                                    attr_value = \
                                                        float(attr_value)
                                                except ValueError:
                                                    attr_value = \
                                                        attr_value.strip('\'"')
                                            setattr(class_objs[key],
                                                    attr_name, attr_value)
                                            storage.save()
                                        else:
                                            print("** value missing **")
                                            return
                                else:
                                    print("** attribute name missing **")
                                    return
                        else:
                            print("** no instance found **")
                    else:
                        print("** instance id is missing **")
            else:
                print("** class doesn't exist **")

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it.
        """
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = globals()[arg]()
            new_instance.save()
            print(new_instance.id)
        except KeyError:
            print("** class doesn't exist **")
            pass

    def do_show(self, arg):
        """
        Prints the string rep of instance from its class name
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in ['BaseModel', 'User', 'Place',
                           'Amenity', 'City', 'State', 'Review']:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id is missing **")
            return
        try:
            obj_dict = storage.all()
            key = args[0] + "." + args[1]
            if key in obj_dict:
                print(obj_dict[key])
            else:
                print("** no instance found **")
        except KeyError:
            pass

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id save the change.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in ['BaseModel', 'User', 'Place',
                           'Amenity', 'City', 'State', 'Review']:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        try:
            obj_dict = storage.all()
            key = args[0] + "." + args[1]
            if key in obj_dict:
                del obj_dict[key]
                storage.save()
            else:
                print("** no instance found **")
        except KeyError:
            pass

    def do_all(self, arg):
        """
        Prints all string representation of all
        instances based or not on the class name.
        """
        obj_dict = storage.all()
        if not arg:
            print([str(v) for k, v in obj_dict.items()])
        elif arg not in ['BaseModel', 'User', 'Place',
                         'Amenity', 'City', 'State', 'Review']:
            print("** class doesn't exist **")
        else:
            print([str(v) for k, v in obj_dict.items()
                   if v.__class__.__name__ == arg])

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in ['BaseModel', 'User', 'Place',
                           'Amenity', 'City', 'State', 'Review']:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        try:
            obj_dict = storage.all()
            key = args[0] + "." + args[1]
            if key in obj_dict:
                if len(args) == 2:
                    print("** attribute name missing **")
                    return
                elif len(args) == 3:
                    print("** value missing **")
                    return
                else:
                    passed_value = args[3].strip(' "\'')
                    passed_attr = args[2].strip(' "\'')
                    if passed_attr:
                        if passed_attr not in ['id', 'created_at',
                                               'updated_at']:
                            if passed_value:
                                try:
                                    new_value = int(passed_value)
                                except ValueError:
                                    try:
                                        new_value = float(passed_value)
                                    except ValueError:
                                        new_value = passed_value
                                setattr(obj_dict[key], passed_attr, new_value)
                                storage.save()
                            else:
                                print("** value missing **")
                                return
                    else:
                        print("** attribute name missing **")
                        return
            else:
                print("** no instance found **")
        except Exception as e:
            pass


if __name__ == '__main__':
    from models.base_model import BaseModel
    from models import storage
    from models.user import User
    from models.place import Place
    from models.amenity import Amenity
    from models.city import City
    from models.review import Review
    from models.state import State
    HBNBCommand().cmdloop()
