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
    'F': {3: 20},
    'H': {5: 45, 10: 80},
    'K': {2: 150},
    'P': {5: 200},
    'Q': {3: 80},
    'U': {4: 120},
    'V': {2: 90, 3: 130}
}

SPECIAL_OFFER_DIFF_ITEMS = {
    'E': {2: 'B'},
    'N': {3: 'M'},
    'R': {3: 'Q'}
}

GROUP_SPECIAL_OFFER = {
    ('Z', 'S', 'T', 'Y', 'X'): {3: 45}
}


def get_free_items(sku_count):
    free_units_dict = dict([(i, 0) for i in UNIT_PRICE.keys()])
    for item, offer in SPECIAL_OFFER_DIFF_ITEMS.items():
        item_count = sku_count.get(item, 0)
        for required_item, free_diff_item in offer.items():
            free_units_dict[free_diff_item] += floor(item_count/required_item)
    return free_units_dict


def get_price_no_free(units, item):
    if not isinstance(units, int):
        raise TypeError('units must be int')

    unit_price = UNIT_PRICE[item]
    special_offer = SPECIAL_OFFER.get(item, {})
    special_numbers = sorted(special_offer.keys(), reverse=True)
    total_price = 0
    total_units = units
    for special_number in special_numbers:
        rounded_items = floor(total_units / special_number)
        total_price += rounded_items * special_offer[special_number]
        total_units -= rounded_items * special_number
    total_price += total_units*unit_price
    return total_price


def get_price_no_grouped_discount(units, item, free_units_dict):
    if units == 0:
        return 0
    free_units = free_units_dict.get(item, 0)
    price_no_free = get_price_no_free(units, item)
    if free_units == 0:
        return price_no_free
    price_with_free = get_price_no_free(units-free_units, item)
    return min(price_no_free, price_with_free)


def get_grouped_special_count(sku_count):
    grouped_special_count = {}
    for special_group in GROUP_SPECIAL_OFFER:
        # ('Z', 'S', 'T', 'Y', 'X')
        for item in special_group:




get_price_grouped_discount({'X': 10, 'T': 5})


def checkout(skus):
    sku_count = dict([(i, 0) for i in UNIT_PRICE.keys()])
    for i in skus:
        if i not in UNIT_PRICE.keys():
            return -1
        else:
            sku_count[i] += 1
    free_units_dict = get_free_items(sku_count)
    return sum([get_price_no_grouped_discount(units, item, free_units_dict) for item, units in sku_count.items()])



