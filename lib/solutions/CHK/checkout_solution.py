from math import floor

# noinspection PyUnusedLocal
# skus = unicode string

UNIT_PRICE = {
    'A': 50,
    "B": 30,
    'C': 20,
    'D': 15,
    'E': 40,
    'F': 10,
    'G': 20,
    'H': 10,
    'I': 35,
    'J': 60,
    'K': 80,
    'L': 90,
    'M': 15,
    'N': 40,
    'O': 10,
    'P': 50,
    'Q': 30,
    'R': 50,
    'S': 30,
    'T': 20,
    'U': 40,
    'V': 50,
    'W': 20,
    'X': 90,
    'Y': 10,
    'Z': 50
}

SPECIAL_OFFER = {
    'A': {3: 130, 5: 200},
    'B': {2: 45},
    'F': {3: 20}
}


def get_price_no_free(units, item):
    if not isinstance(units, int):
        raise TypeError('units must be int')
    unit_price = UNIT_PRICE[item]
    special_offer = SPECIAL_OFFER.get(item, {})
    if item in ['C', 'D', 'E']:
        return unit_price * units
    elif item in ['A', 'B', 'F']:
        special_numbers = sorted(special_offer.keys(), reverse=True)
        total_price = 0
        total_units = units
        for special_number in special_numbers:
            rounded_items = floor(units / special_number)
            total_price += rounded_items * special_offer[special_number]
            total_units -= rounded_items * special_number
        total_price += total_units*unit_price
        return total_price
        # rounded_5_items = floor(units / 5)
        # rounded_3_items = floor((units - rounded_5_items * 5) / 3)
        # return rounded_5_items * 200 + rounded_3_items * 130 + \
        #        (units - rounded_5_items * 5 - rounded_3_items * 3) * unit_price
    # elif item == 'B':
    #     rounded_items = floor(units / 2)
    #     return rounded_items * 45 + (units - rounded_items * 2) * unit_price
    # elif item == 'F':
    #     rounded_items = floor(units / 3)
    #     return rounded_items * 20 + (units - rounded_items * 3) * unit_price


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
    sku_count = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0}
    for i in skus:
        if i not in ['A', 'B', 'C', 'D', 'E', 'F']:
            return -1
        else:
            sku_count[i] += 1
    free_units_dict = get_free_items(sku_count)
    return sum([get_price(units, item, free_units_dict) for item, units in sku_count.items()])


