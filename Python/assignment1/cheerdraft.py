



#e.g [4 7 8 10 12 15 21 35] would award the huskers [12 15 21] {48} and the mavericks [10 15 35] {60}



# scores = []

# n = len(sys.argv)
# for i in range(1,n):
#     scores.append(int(sys.argv[i]))

# huskerScore = 0
# maverickScore = 0

# for i in range (n - 1):
#     if scores[i] % 3 == 0:
#         huskerScore += scores[i]
#     if scores[i] % 5 == 0:
#         maverickScore += scores[i]

# print(f"Huskers: {huskerScore}")
# print(f"Mavericks: {maverickScore}")

"""
Author: Benjamin Wormsley
Date: 2023-1-27

fizzbuzz
"""
import sys
import math

def huskerMavScore(values):
    """
    Computes the Husker and Maverick Score according to the following rules:
    if integer is divisible by 3, award it to huskers
    if integer is divisible by 5, award to mavericks
    if integer is divisible by 3 and 5, award it to both teams
    ignore it other wise
    Returns a pair containing the Husker/Mav Scores respectively
    """
    n = len(values)

    for i in range(n):
        if values[i] % 3 == 0:
            huskerMavScore

def winner(values):
    """
    Calculates the winner of the game based on the rules above.  Returns
    a negative value if the Huskers win (have a greater score than the Mavericks),
	a positive value if the Mavericks win, and zero if the game is a tie.
    """
    #TODO


#ad-hoc testing:
a = [2, 9, 4, 25, 57, 45, 53]

(huskerScore,mavScore) = huskerMavScore(a)
print(f"husker score = {huskerScore}")
print(f"mav score    = {mavScore}")