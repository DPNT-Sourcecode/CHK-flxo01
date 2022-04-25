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
    'K': 70,
    'L': 90,
    'M': 15,
    'N': 40,
    'O': 10,
    'P': 50,
    'Q': 30,
    'R': 50,
    'S': 20,
    'T': 20,
    'U': 40,
    'V': 50,
    'W': 20,
    'X': 17,
    'Y': 20,
    'Z': 21
}

SPECIAL_OFFER = {
    'A': {3: 130, 5: 200},
    'B': {2: 45},
    'F': {3: 20},
    'H': {5: 45, 10: 80},
    'K': {2: 120},
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
    ('X', 'S', 'T', 'Y', 'Z'): {3: 45},
    ('A', ): {3: 130, 5: 200},
    ('B',): {2: 45},
    ('F',): {3: 20},
    ('H',): {5: 45, 10: 80},
    ('K',): {2: 120},
    ('P', ): {5: 200},
    ('Q', ): {3: 80},
    ('U', ): {4: 120},
    ('V', ): {2: 90, 3: 130}
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


def get_grouped_special_price(sku_count, group):
    group_count = dict([(i, sku_count[i]) for i in group])

    total_units = sum(group_count.values())
    total_price = 0
    special_offer = GROUP_SPECIAL_OFFER.get(group, {})
    special_numbers = sorted(special_offer.keys(), reverse=True)
    for special_number in special_numbers:
        rounded_items = floor(total_units / special_number)
        total_price += rounded_items * special_offer[special_number]
        total_units -= rounded_items * special_number
    remain_units = 0
    for i in group:
        unit_price = UNIT_PRICE[i]
        remain_units += group_count[i]
        if remain_units < total_units:
            total_price += remain_units * unit_price
            total_units -= remain_units
        else:
            total_price += total_units * unit_price
            break
    return total_price


def checkout(skus):
    sku_count = dict([(i, 0) for i in UNIT_PRICE.keys()])
    for i in skus:
        if i not in UNIT_PRICE.keys():
            return -1
        else:
            sku_count[i] += 1
    total_price = 0
    for group in GROUP_SPECIAL_OFFER:
        total_price += get_grouped_special_price(sku_count, group)
        for i in group:
            sku_count.pop(i)
    free_units_dict = get_free_items(sku_count)
    total_price += sum([get_price_no_grouped_discount(units, item, free_units_dict) for item, units in sku_count.items()])
    return total_price
