def add(x, y):
    if type(x) not in [int, float] or type(y) not in [int, float]:
        raise TypeError("Invalid type")
    return x + y