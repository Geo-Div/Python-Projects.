Exercise2:Thisprogramcountsthedistributionofthehourofthedayforeach
of themessages.Youcanpull thehour fromthe“From”linebyfindingthetime
stringandthensplittingthat string intopartsusingthecoloncharacter. Once
youhaveaccumulatedthecountsforeachhour,printoutthecounts,oneperline,
sortedbyhourasshownbelow.
pythontimeofday.py
Enterafilename: mbox-short.txt
043
061
071
092
103
116
141
152
164
172
181
191

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
    time = words[5]
    hour = time.split(":")[0]
    counts[hour] = counts.get(hour, 0) + 1

lst = list()
for key, val in counts.items():
    lst.append((key, val))

lst.sort()

for key, val in lst:
    print(key. val)