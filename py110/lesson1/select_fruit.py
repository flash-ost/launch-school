def select_fruit(produce_dict):
    fruits = { key: produce_dict[key] for key in produce_dict if produce_dict[key] == 'Fruit' }
    return fruits

produce = {
    'apple': 'Fruit',
    'carrot': 'Vegetable',
    'pear': 'Fruit',
    'broccoli': 'Vegetable',
}

print(select_fruit(produce))  # { apple: 'Fruit', pear: 'Fruit' }

