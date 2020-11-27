"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# if score < 0 or score > 100
# error
# if input valid score
# determine score
# endif

score = float(input("Enter score: "))
if score < 0 or score > 100:
    print("Invalid score")
elif score >= 90:
    print("Excellent")
elif score >= 50:
    print("Passable")
else:
    print("Bad")
