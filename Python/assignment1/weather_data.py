"""
Author: Benjamin Wormsley
Date(Completed): 2023-02-10

This program takes data from two weather stations and returns data on the tempature and date, as well as flagging any
missing or inconsistent data points
"""

import sys

def read_file(filename):
    """
    Given a filename, opens it and reads it into a dictionary, with the key
    as the first part, and the value as the second part. Each part is separated by a space.
    Returns the dictionary.
    """
    data = {}
    f = open(filename, "r")
    n = int(f.readline().strip())
    for i in range(n):
        line= f.readline().strip().split()
        data[line[0]] = float(line[1])
    f.close()
    return data

def temp_data(dict):
    """
    Given a dictionary with float values, return a tuple containing the minimum, maximum, and mean values.
    """
    data = list(dict.values())
    return(min(data), max(data), (sum(data) / len(data)))

def date_data(dict):
    """
    Given a dictionary with string keys, return a tuple with the earliest and most recent dates
    """
    data = list(dict.keys())
    data.sort()
    first = data[0]
    recent = data[len(data) - 1]
    return(first, recent)

def compare_data(dicta, dictb, missing, inconsistent):
    """
    Given four dictionaries, two full and two blank
    """
    for date_a in dicta:
        if date_a not in dictb:
            missing[date_a] = dicta[date_a]
        else:
            if abs(dicta[date_a] - dictb[date_a]) > 0.001:
                inconsistent[date_a] = (dicta[date_a], dictb[date_a])


  
n = len(sys.argv)
if n != 3:
    print("Error: faulty input. Please use this progream as follows:")
    print("weather_data.py [input file 1] [input file 2]")
    sys.exit(1)

data_a = read_file(sys.argv[1])
data_b = read_file(sys.argv[2])
temps = temp_data(data_a)
dates = date_data(data_a)
inconsistent = {}
missing = {}
compare_data(data_a, data_b, missing, inconsistent)

print("[#####-----=====-----=====-----=====-----#####]")
print(f"Loaded {len(data_a)} datapoints from set A")
print(f"Loaded {len(data_b)} datapoints from set B\n")
print("Temperature Reports (Set A)")
print("[#####-----=====-----=====-----=====-----#####]")
print(f"Minimum: {temps[0]:7}")
print(f"Mean: {temps[2]:10.3}")
print(f"Maximum: {temps[1]:7}\n")
print("Date Reports (Set A)")
print("[#####-----=====-----=====-----=====-----#####]")
print(f"Earliest Date:    {dates[0]} ({data_a[dates[0]]})")
print(f"Most Recent Date: {dates[1]} ({data_a[dates[1]]})\n")
print("Inconsistent and Missing Data Reports")
print("[#####-----=====-----=====-----=====-----#####]")
for date, temp in missing.items():
    print(f"Missing:      {temp} ({date})")
for date, (temp_a, temp_b) in inconsistent.items():
    print(f"Inconsistent: {temp_a} vs {temp_b} ({date})")
print("") 