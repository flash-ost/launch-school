"""
Calendar Event Checker
We have a list of events and want to check whether a specific date is available (i.e., no events planned for that date). However, the function always returns the wrong value.

events = {
    "2023-08-13": ["Python debugging exercises"],
    "2023-08-14": ["Read 'Automate the Boring Stuff'"],
    "2023-08-15": ["Webinar: Python for Data Science"],
}

def is_date_available(date):
    if date in events:
        return True

    return False

print(is_date_available("2023-08-14"))  # should return False
print(is_date_available("2023-08-16"))  # should return True
"""
# Inside a function we check whether given date is in dictionary keys and return True if it's present, 
# but False should be returned instead, since this date is taken if it's in dict.

events = {
    "2023-08-13": ["Python debugging exercises"],
    "2023-08-14": ["Read 'Automate the Boring Stuff'"],
    "2023-08-15": ["Webinar: Python for Data Science"],
}

def is_date_available(date):
    return date not in events

print(is_date_available("2023-08-14"))  # should return False
print(is_date_available("2023-08-16"))  # should return True