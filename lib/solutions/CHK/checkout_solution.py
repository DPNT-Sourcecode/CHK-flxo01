from math import floor

# noinspection PyUnusedLocal
# skus = unicode string


def get_price(units, item):
    if not isinstance(units, int):
        raise TypeError('units must be int')
    if item == 'C':
        return units * 20
    elif item == 'D':
        return units * 15
    elif item == 'A':
        rounded_items = floor(units / 3)
        return rounded_items * 130 + (units - rounded_items * 3) * 50
    elif item == 'B':
        rounded_items = floor(units / 2)
        return rounded_items * 45 + (units - rounded_items * 2) * 30


def checkout(skus):
    sku_count = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
    for i in skus:
        if i not in ['A', 'B', 'C', 'D']:
            return -1
        else:
            sku_count[i] += 1
    return sum([get_price(units, item) for item, units in sku_count.items()])



