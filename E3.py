Exercise3:Writeaprogramthatreadsafileandprintstheletters indecreasing
orderof frequency.

Answer:
fname = input("Enter a file name: ")
try:
    fhand = open(fname)
except:
    print("Invalid file name")
    quit()

counts = dict()

for line in fhand:
    line = line.lower()
    for ch in line:
        if ch.isalpha() and ch in "abcdefghijklmnopqrstuvwxyz":
            counts[ch] = counts.get(ch, 0) + 1

lst = list()
for key, val in counts.items():
    lst.append((val, key))

lst.sort(reverse=True)

for val, key in lst:
    print(key, val)