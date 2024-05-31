my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}

odd_dict = { string: len(string) 
             for string in my_set 
             if len(string) % 2 != 0 }

print(odd_dict)