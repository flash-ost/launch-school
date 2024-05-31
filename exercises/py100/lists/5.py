"""
Filter
Count the number of elements in scores that are 100 or above.

scores = [96, 47, 113, 89, 100, 102]
"""
scores = [96, 47, 113, 89, 100, 102]
# print(len([score for score in scores if score >= 100]))
num = 0
for score in scores:
    if score >= 100:
        num += 1
print(num)        