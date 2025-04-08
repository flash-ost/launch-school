"""
Merge Sorted Lists
Write a function that takes two sorted lists as arguments and returns a new list that contains all the elements from both input lists in ascending sorted order. You may assume that the lists contain either all integer values or all string values.

You may not provide any solution that requires you to sort the result list. You must build the result list one element at a time in the proper order.

Your solution should not mutate the input lists.

Examples
# All of these examples should print True
print(merge([1, 5, 9], [2, 6, 8]) == [1, 2, 5, 6, 8, 9])
print(merge([1, 1, 3], [2, 2]) == [1, 1, 2, 2, 3])
print(merge([], [1, 4, 5]) == [1, 4, 5])
print(merge([1, 4, 5], []) == [1, 4, 5])

names1 = ['Alice', 'Kim', 'Pete', 'Sue']
names2 = ['Bonnie', 'Rachel', 'Tyler']
names_expected = ['Alice', 'Bonnie', 'Kim', 'Pete',
                  'Rachel', 'Sue', 'Tyler']
print(merge(names1, names2) == names_expected)
"""
## Understanding
# Input: 2 sorted lists
# Output: single sorted lists containing 2 original lists merged

# Solution should not sort the merged list, but create the merged sorted list 1 element at a time
# Solution should not mutate original lists
# Input lists will both consist either of integers only or strings only

## Algorithm 1
# Create empty list merged
# Create copy1 of the list1
# Create copy2 of the list2
# Iterate while idx1 for list1 is less than its length and idx for list2 is less than its length:
#   If idx1 for list1 is equal to its length:
#       append idx2 element of list2 to merged
#       increment idx2 by 1
#       continue
#   elif idx2 for list2 is equal ot its length:
#       append idx1 element of list1 to merged
#       increment idx1 by 1
#       continue

#   if idx1 el of list1 is less than or equal to idx2 el of list2:
#       append idx1 el of list1 to merged
#       increment idx1 by 1
#   else:
#       append idx2 el of list2 to merged
#       increment idx2 by 1
# Return merged

# Solution 1
# def merge(list1, list2):
    # merged = []
    # idx1 = idx2 = 0
    # length1 = len(list1)
    # length2 = len(list2)
    # while idx1 < length1 or idx2 < length2:
    #     if idx1 == length1:
    #         merged.append(list2[idx2])
    #         idx2 += 1
    #         continue
    #     elif idx2 == length2:
    #         merged.append(list1[idx1])
    #         idx1 += 1
    #         continue

    #     if list1[idx1] <= list2[idx2]:
    #         merged.append(list1[idx1])
    #         idx1 += 1
    #     else:
    #         merged.append(list2[idx2])
    #         idx2 += 1
    # return merged

## Algorithm 2
# Create an empty list merged
# Create copy1 of list1
# Create copy2 of list2
# While both copies have elements:
#   if 0th element of copy1 if less than or equal to 0th element of copy2:
#       pop 0th element of copy1 and append it to merged
#   else:
#       pop 0th element of copy2 and append it to merged
# return merged concatenated to copy1 and copy2 (this ensures we add elements that may remain in copy1 or copy2)

# Solution 2
def merge(list1, list2):
    merged = []
    copy1 = list1[:]  
    copy2 = list2[:]

    while copy1 and copy2:
        if copy1[0] <= copy2[0]:
            merged.append(copy1.pop(0))
        else:
            merged.append(copy2.pop(0))
    return merged + copy1 + copy2        

print(merge([1, 5, 9], [2, 6, 8]) == [1, 2, 5, 6, 8, 9])
print(merge([1, 1, 3], [2, 2]) == [1, 1, 2, 2, 3])
print(merge([], [1, 4, 5]) == [1, 4, 5])
print(merge([1, 4, 5], []) == [1, 4, 5])

names1 = ['Alice', 'Kim', 'Pete', 'Sue']
names2 = ['Bonnie', 'Rachel', 'Tyler']
names_expected = ['Alice', 'Bonnie', 'Kim', 'Pete',
                  'Rachel', 'Sue', 'Tyler']
print(merge(names1, names2) == names_expected)
