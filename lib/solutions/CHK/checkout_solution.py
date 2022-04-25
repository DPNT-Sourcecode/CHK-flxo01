

# noinspection PyUnusedLocal
# skus = unicode string

def get_price(units, item):
    if item not in ['A', 'B', 'C', 'D']:
        return -1
    if not isinstance(units, int):
        raise TypeError('units must be int')
    if item == 'C':
        return units * 20
    elif item == 'D':
        return units * 15
    elif item == 'A':
        rounded_items = units / 3
        return rounded_items * 130 + (units - rounded_items*3)*50

def checkout(skus):



