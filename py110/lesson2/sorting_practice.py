"""
Practice Problem 1
Sort the following list of numbers first in ascending numeric order, then in descending numeric order. Do not mutate the list.

lst = [10, 9, -6, 11, 7, -16, 50, 8]
Expected result
[-16, -6, 7, 8, 9, 10, 11, 50]          # Ascending sort
[50, 11, 10, 9, 8, 7, -6, -16]          # Descending sort
"""
# lst = [10, 9, -6, 11, 7, -16, 50, 8]
# print(sorted(lst))
# print(sorted(lst, reverse=True))

"""
Practice Problem 2
Repeat the previous exercise but, this time, perform the sort by mutating the original list.

lst = [10, 9, -6, 11, 7, -16, 50, 8]
Expected result
[-16, -6, 7, 8, 9, 10, 11, 50]          # Ascending sort
[50, 11, 10, 9, 8, 7, -6, -16]          # Descending sort
"""
# lst = [10, 9, -6, 11, 7, -16, 50, 8]

# lst.sort()
# print(lst)

# lst.sort(reverse=True)
# print(lst)

"""
Repeat problem 2 but, this time, sort the list as string values. Both the list passed to the sorting function and the returned list should contain numbers, not strings.

lst = [10, 9, -6, 11, 7, -16, 50, 8]

Expected result
[-16, -6, 10, 11, 50, 7, 8, 9]          # Ascending sort
[9, 8, 7, 50, 11, 10, -6, -16]          # Descending sort
"""
# lst = [10, 9, -6, 11, 7, -16, 50, 8]

# lst.sort(key=str)
# print(lst)

# lst.sort(key=str, reverse=True)
# print(lst)

"""
Practice Problem 4
How would you sort the following list of dictionaries based on the year of publication of each book, from the earliest to the most recent?

books = [
    {
        'title': 'One Hundred Years of Solitude',
        'author': 'Gabriel Garcia Marquez',
        'published': '1967',
    },
    {
        'title': 'The Book of Kells',
        'author': 'Multiple Authors',
        'published': '800',
    },
    {
        'title': 'War and Peace',
        'author': 'Leo Tolstoy',
        'published': '1869',
    },
]
Expected result
# Pretty printed for clarity
[
    {
        'title': 'The Book of Kells',
        'author': 'Multiple Authors',
        'published': '800'
    },
    {
        'title': 'War and Peace',
        'author': 'Leo Tolstoy',
        'published': '1869'
    },
    {
        'title': 'One Hundred Years of Solitude',
        'author': 'Gabriel Garcia Marquez',
        'published': '1967'
    }
]
"""
books = [
    {
        'title': 'One Hundred Years of Solitude',
        'author': 'Gabriel Garcia Marquez',
        'published': '1967',
    },
    {
        'title': 'The Book of Kells',
        'author': 'Multiple Authors',
        'published': '800',
    },
    {
        'title': 'War and Peace',
        'author': 'Leo Tolstoy',
        'published': '1869',
    },
]

def year(dict):
    return int(dict['published'])

print(sorted(books, key=year))