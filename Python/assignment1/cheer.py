"""
Author: Benjamin Wormsley
Date: 2023-1-27
e.g [4 7 8 10 12 15 21 35] would award the huskers [12 15 21] {48} and the mavericks [10 15 35] {60}
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

    e.g [4 7 8 10 12 15 21 35] would award the huskers [12 15 21] {48} and the mavericks [10 15 35] {60}

    Returns a pair containing the Husker/Mav Scores respectively
    """
    n = len(values)
    huskerScore = 0
    mavScore = 0
    for i in range(n):
        if values[i] % 3 == 0:
            huskerScore += values [i]
        if values[i] % 5 == 0:
            mavScore += values[i]
    return (huskerScore, mavScore)

def winner(values):
    """
    Calculates the winner of the game based on the rules above.  Returns
    a negative value if the Huskers win (have a greater score than the Mavericks),
	a positive value if the Mavericks win, and zero if the game is a tie.
    """
    (huskerScore, mavScore) = huskerMavScore(values)
    if huskerScore > mavScore:
        return -1
    elif mavScore > huskerScore:
        return 1
    else:
        return 0 


#ad-hoc testing:
a = [2, 9, 4, 25, 57, 45, 53, ]

(huskerScore,mavScore) = huskerMavScore(a)
print(f"Husker score = {huskerScore}")
print(f"Mav score    = {mavScore}")

final = winner(a)
if final < 0:
    print("Huskers win!")
elif final > 0:
    print("Mavericks win!")
else:
    print("Tie game!")