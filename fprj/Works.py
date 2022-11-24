def get_val(collection=None, key=None, default=None):
    thinks = [
        ('not isinstance(collection, dict)', "Collection is not dict"),
        ('None in [collection, key]', "Missing an argument"),
        ('not isinstance(key, str | tuple | int | float)', "The key does not fit")
    ]

    for i, p in thinks:
        if eval(i):
            print(p)
            return
    try:
        return collection[key]
    except:
        return default


def set_(coll, path, value):
    if not isinstance(coll, dict):
        print('the coll argument must be a dictionary')
        return

    if len(path) == 1:
        coll[path[0]] = value
        return

    set_(coll.setdefault(path[0], {}), path[1:], value)


print(get_val({"hello": "world"}, "hello"))
