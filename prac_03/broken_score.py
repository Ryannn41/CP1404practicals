"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


# if score < 0 or score > 100
# error
# if input valid score
# determine score
# endif

def main():
    score = float(input("Enter score: "))
    print(user_input(score))


def user_input(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
