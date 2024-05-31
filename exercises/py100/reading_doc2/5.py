"""
Which Year is This?
The Python documentation for the datetime module provides two attributes to retrieve the year from a date or datetime object: year and isocalendar.

from datetime import date

today = date.today()

today_year = today.year
iso_year = today.isocalendar()[0]
What is the difference between the year attribute and the isocalendar method?
"""

# year attribute returns a numeric value of the year of indicated date.
# isocalendar method returns a tuple object with three components: year, week and weekday. All three are in ISO standart.