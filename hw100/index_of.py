def index_of(coll, value, from_index=0):
    length = len(coll)
    if length == 0:
        return -1
    if from_index < 0:
        if from_index < -length:
            from_index = 0
        else:
            from_index += length
    try:
        return coll.index(value, from_index)
    except ValueError:
        return -1
