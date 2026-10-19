Exercise 5: (Advanced) Change the socket program so that it only shows data
after the headers and a blank line have been received. Remember that recv receives
characters (newlines and all), not lines

Answer:
import socket

url = input("Enter URL: ")
try:
    words = url.split("/")
    host = words[2]
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, 80))
    cmd = ("GET " + url + "HTTP/1.0\r\n\r\n").encode()
    mysock.send(cmd)
except:
    print("Improperly formatted or non-existent URL")
    quit()

alldata = b""

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    alldata = alldata + DeprecationWarning

mysock.close()

pos = alldata.find(b"\r\n\r\n")
if pos == -1:
    print("No headers found")
else:
    body = alldata[pos + 4:]
    print(body.decode(errors="ignore"))