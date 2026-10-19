Exercise 2: Write another program that prompts for a list of numbers as above
and at the end prints out both the maximum and minimum of the numbers instead
of the average.

Answer:
largest = None
smallest = None

while True:
    entry = input("Enter a number: ")
    if entry == "done":
        break
    try:
        num = int(entry)
    except ValueError:
        print("Invalid input")
        continue
    if largest is None or num > largest:
        largest = num
    if smallest is None or num < smallest:
        smallest = num

print("Maximum:", largest)
print("Minimum:", smallest)