Exercise 1: Write a simple program to simulate the operation of the grep com
mand on Unix. Ask the user to enter a regular expression and count the number
of lines that matched the regular expression:
$ python grep.py
Enter a regular expression: ^Author
mbox.txt had 1798 lines that matched ^Author
$ python grep.py
Enter a regular expression: ^X
mbox.txt had 14368 lines that matched ^X
$ python grep.py
Enter a regular expression: java$
mbox.txt had 4175 lines that matched java$

Answer:
import re

fname = input("Enter a file name: ")
try:
    fhand = open(fname)
except:
    print("Invalid file name")
    quit()

pattern = input("Enter a regular expressio: ")
count = 0

for line in fhand:
    line = line.rstrip()
    if re.search(patter, line):
        count = count + 1

print(fname, "had", count, "lines that matched", pattern)
