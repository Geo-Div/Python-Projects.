Exercise 3: Use urllib to replicate the previous exercise of (1) retrieving the
document from a URL, (2) displaying up to 3000 characters, and (3) counting the
overall number of characters in the document. Don’t worry about the headers for
this exercise, simply show the first 3000 characters of the document contents.

Answer:
import urllib.request

url = input("Enter URL: ")
try:
    fhand = urlib.request.urlopen(url)
except:
    print("Improperly formatted or non-existent URL")
    quit()

total = 0
shown = 0

while True:
    data = fhand.read(512)
    if len(data) < 1:
        break
    text = data.decode(errors="ignore")
    total = total + len(text)
    if shown < 3000:
        piece = text[:3000 - shown]
        print(piece, end="")
        shown = shown + len(piece)

print()
print("Total charactera:", total)
