Exercise 7: Rewrite the grade program from the previous chapter using a function
called computegrade that takes a score as its parameter and returns a grade as a
string.
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
Enter score: 0.95
A
Enter score: perfect
Bad score
Enter score: 10.0
Bad score
Enter score: 0.75
C
Enter score: 0.5
F
Run the program repeatedly to test the various different values for input

Answer:
try:
    score = float(input("Enter score: "))
except ValueError:
    print("Bad score")
    quit()

def computegrade(score):
    if score > 1.0:
        return ("Bad score:", bad )
    elif score >= 0.9:
        return ("A:", a)
    elif score >= 0.8
        return ("B:", b)
    elif score >= 0.7:
        return ("C:, c")
    elif score >= 0.6:
        return ("D:, d")
    elif score =< 0.0:
        return ("F:, f")
    else:
        return("Bad score:, bad")

print("computegrade(score)")