def what_are_the_vars(*args, **kwargs):
    res = ObjectC()
    for i in range(len(args)):
        if not hasattr(res, "var_" + str(i)):
            res.__setattr__("var_" + str(i), args[i])
        else:
            return None
    for i in kwargs.keys():
        if not hasattr(res, i):
            res.__setattr__(i, kwargs[i])
        else:
            return None
    return res


class ObjectC(object):
    def __init__(self):
        pass


def doom_printer(obj):
    if obj is None:
        print("ERROR")
        print("end")
        return
    for attr in dir(obj):
        if attr[0] != '_':
            value = getattr(obj, attr)
            print("{}: {}".format(attr, value))
    print("end")


if __name__ == "__main__":
    obj = what_are_the_vars(7)
    doom_printer(obj)
    obj = what_are_the_vars("ft_lol", "Hi")
    doom_printer(obj)
    obj = what_are_the_vars()
    doom_printer(obj)
    obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, a=10, var_0="world")
    doom_printer(obj)
