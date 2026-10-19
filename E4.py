Exercise 4: Add code to the above program to figure out who has sent the most
messages in the file. After all the data has been read and the dictionary has
been created, look through the dictionary using a maximum loop (see Chapter 5:
Maximum and minimum loops) to find who has the most messages and print how
many messages the person has.
Enter a file name: mbox-short.txt
cwen@iupui.edu 5
Enter a file name: mbox.txt
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

bestcount = None
bestemail = None

for email, count in counts.items():
    if bestcount is None or count > bestcount:
        bestcount = count
        bestemail = email

print(bestemail, bestcount)