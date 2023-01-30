"""
A demonstration of the usage of the "statistics library" which also
serves as an ad-hoc tester for the four functions.  Command line arguments
(CLAs) are used to read in a sequence of values and various statistics
are computed on them (min, max, sum, mean)
"""
import sys
import statistics

if len(sys.argv) <= 1:
    print("Please provide a list of numbers as command line arguments")
    exit(1)

# create a list of values from the command line arguments
# using a traditional loop:
values = []
for i in range(1, len(sys.argv)):
    values.append(float(sys.argv[i]))

# the more "pythonic way" using a list comprehension:
values = [ float(x) for x in sys.argv[1:] ]

print("values: " + str(values))
min = statistics.minimum(values)
max = statistics.maximum(values)
sum = statistics.sumVals(values)
mean = statistics.mean(values)

print(f"Minimum: {min}")
print(f"Maximum: {max}")
print(f"Sum:     {sum}")
print(f"Mean:    {mean}")
