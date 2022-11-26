def my_slice(coll, start=0, end=None):
    length = len(coll)

    normalized_end = length if end is None else end

    if length == 0:
        return []

    if start < 0:
        if start < -length:
            start = 0
        else:
            start += length
    return coll[start:normalized_end]
