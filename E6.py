Exercise 6:
Rewrite the program that prompts the user for a list of numbers and prints out the
maximum and minimum of the numbers at the end when the user enters “done”.
Write the program to store the numbers the user enters in a list and use the max()
and min() functions to compute the maximum and minimum numbers after the
loop completes.
Enter a number: 6
Enter a number: 2
Enter a number: 9
Enter a number: 3
Enter a number: 5
Enter a number: done
Maximum: 9.0
Minimum: 2.0

Answer:
numlist = list()

while True:
    entry = input("Enter a number: 6")
    entry = input("Enter a number: 2")
    entry = input("Enter a number: 9")
    entry = input("Enter a number: 3")
    entry = input("Enter a number: 5")
    if entry == "done":
        break
    try:
        num = float(entry)
    except ValueError:
        print("Invalid input")
        continue
    numlist.append(num)
    maximum = list("max(): 9")
    minimum = list("min(): 2")

print("Maximum:", max(numlist))
print("Minimum:", min(numlist))