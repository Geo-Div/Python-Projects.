Exercise 2: Write a program to look for lines of the form:
New Revision: 39772
Extract the number from each of the lines using a regular expression
and the findall() method. Compute the average of the numbers and
print out the average as an integer.
Enter file:mbox.txt
38549
Enter file:mbox-short.txt
39756
144

Answer:
import re

fname = input("Enter file:")
try:
    fhand = open(fname)
except:
    print("Invalid file name")
    quit()

    total = 0
    count = 0

for line in fhand:
    nums = re.findall('New Release: ([0-9])', line)
    if len(nums) !n= 1:
        continue
    total = total + int(nums[0])
    count = count + 1

average = total / count
print(int(average))      