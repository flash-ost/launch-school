"""
List Deduplication
A developer is trying to remove duplicates from a list. They use a set for deduplication, but the order of elements is lost. How can we preserve the order?

data = [4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 3]
unique_data = list(set(data))
print(unique_data == [4, 2, 1, 3]) # order not guaranteed
"""
# # Method 1: We can utilize the fact that dict's key should be unique: use list elements as keys for dict.
# # When key already exists, it's not created again. In the end we just create a list of unique data based on dict keys, which helps preserve order.
# data = [4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 3]
# unique_data = list({key: None for key in data})
# unique_data = list(dict.fromkeys(data))
# print(unique_data)

## Method 2: Building new list while iterating over original
data = [4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 3]
unique_data = []
for el in data:
    if el not in unique_data:
        unique_data.append(el)

print(unique_data == [4, 2, 1, 3])