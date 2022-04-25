from math import floor

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
        rounded_items = floor(units / 3)
        return rounded_items * 130 + (units - rounded_items * 3) * 50
    elif item == 'B':
        rounded_items = floor(units / 2)
        return rounded_items * 45 + (units - rounded_items * 2) * 30

def parse_sku(skus):
    'AABBCCA'
    return {}

def checkout(skus):




