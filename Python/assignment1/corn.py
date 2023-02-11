"""
Author: Benjamin Wormsley
Date: 2023-1-26
Takes a radius, a height, and a percentage as command line arguments and returns a weight
"""
import sys
import math

n = len(sys.argv)

if n != 4:
    print("Please input data as following:")
    print("corn.py [radius] [height] [percentage full]")
    exit(1)
radius = float(sys.argv[1])
height = float(sys.argv[2])
percnt = float(sys.argv[3])

if radius <= 0 or height <= 0 or percnt < 0 or percnt > 1:
    print("Error! Invalid Input(s)")
    exit(2)

volume = height * radius * radius * math.pi * percnt
weight = volume * 720.83 
percnt = percnt * 100

print(f"Radius: {radius:.2f} m")
print(f"Height: {height:.2f} m")
print(f"Percent: {percnt:.2f} %")
print("\n")
print(f"Total Volume: {volume:.2f} m^3")
print(f"Total Weight: {weight:.2f} kg")

