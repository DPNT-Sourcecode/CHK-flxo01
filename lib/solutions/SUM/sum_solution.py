# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):
    if x < 0 or y < 0:
        raise ValueError("Expect positive values")
    if x > 100 or y > 100:
        raise ValueError("inputs cannot be more than 100")
    if not (isinstance(x, int) and isinstance(y, int)):
        raise ValueError('inputs must be integer')
    return sum((x, y))


