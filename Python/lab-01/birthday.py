"""
Interactively prompts the user for their bithdate
and computes how old they are.
"""
import sys
import math
from datetime import date

# A "dictionary" that maps months (as strings) to their ordinal (integers)
monthMap = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

# An alternative way of creating the dictionary/map using a list
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
# and a dictionary comprehension:
monthMap = { month:months.index(month)+1 for month in months }

today = date.today()

year = int(sys.argv[1])
month = monthMap[sys.argv[2]]
day = int(sys.argv[3])



birthdate = date(year, month, day)

diff = today - birthdate
years = math.floor(diff.days / 365.25)
remain = diff.days - 365.25 * years
weeks = int(remain // 7)
remain = remain - 7 * weeks
days = int(remain)

print(f"You are {years} years, {weeks} weeks and {days} days old")

