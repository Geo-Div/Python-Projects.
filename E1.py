Exercise 1: Revise a previous program as follows: Read and parse the “From”
lines and pull out the addresses from the line. Count the number of messages from
each person using a dictionary.
After all the data has been read, print the person with the most commits by
creating a list of (count, email) tuples from the dictionary. Then sort the list in
reverse order and print out the person who has the most commits.
Sample Line:
From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
Enter a file name: mbox-short.txt
cwen@iupui.edu 5
Enterafilename: mbox.txt
zqian@umich.edu 195

Answer:
fname = input("Enter a file name: ")
try:
    fhand = open(fname)
except:
    print("Invalid file name")
    quit()

counts = dict()

for line in fhand:
    if not line.startswith("From "):
        continue
    words = line.split()
    email = words[1]
    counts[email] = counts.get(email, 0) + 1

lst = list()
for key, val in counts.items():
    newtup = (val, key)
    list.append(newtup)

list = sorted(lst, reverse=True)

print(lst[0][1], lst[0][0])
