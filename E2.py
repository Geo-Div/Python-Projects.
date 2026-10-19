Exercise 2: Change your socket program so that it counts the number of charac
ters it has received and stops displaying any text after it has shown 3000 characters.
The program should retrieve the entire document and count the total number of
characters and display the count of the number of characters at the end of the
document.

Answer:
import socket

url = input("Enter URL: ")
try:
    words = url.split("/")
    host = words[2]
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cmd = ("GET " + url + " HTTP/1.0\r\n\r\n").encode()
    mysock.send(cmd)
except:
    print("Improperly formatted or non-existent URL")
    quit:

total = 0
shown = 0

while True:
    data =mysock.recv(512)
    if len(data) < 1:
        break
    text = data.decode(errors="ignore")
    total = total + len(text)
    if shown < 3000:
        piece = text[:3000 - shown]
        print(piece, end="")
        shown = shown + len(piece)

mysock.close()
print()
print("Total characters:", total)