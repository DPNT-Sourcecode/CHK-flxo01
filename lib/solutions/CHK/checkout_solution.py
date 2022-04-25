from math import floor

# noinspection PyUnusedLocal
# skus = unicode string


def get_price_no_free(units, item):
    if not isinstance(units, int):
        raise TypeError('units must be int')
    if item == 'C':
        return units * 20
    elif item == 'D':
        return units * 15
    elif item == 'A':
        rounded_5_items = floor(units / 5)
        rounded_3_items = floor((units - rounded_5_items * 5) / 3)
        return rounded_5_items * 200 + rounded_3_items * 130 + (units - rounded_5_items * 5 - rounded_3_items * 3) * 50
    elif item == 'B':
        rounded_items = floor(units / 2)
        return rounded_items * 45 + (units - rounded_items * 2) * 30
    elif item == 'E':
        return units * 40


def get_price(units, item, free_units_dict):
    if units == 0:
        return 0
    free_units = free_units_dict.get(item, 0)
    price_no_free = get_price_no_free(units, item)
    if free_units == 0:
        return price_no_free
    price_with_free = get_price_no_free(units-free_units, item)
    return min(price_no_free, price_with_free)


def get_free_items(sku_count):
    e_count = sku_count['E']
    return {'B': floor(e_count/2)}


def checkout(skus):
    sku_count = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}
    for i in skus:
        if i not in ['A', 'B', 'C', 'D', 'E']:
            return -1
        else:
            sku_count[i] += 1
    free_units_dict = get_free_items(sku_count)
    return sum([get_price(units, item, free_units_dict) for item, units in sku_count.items()])

