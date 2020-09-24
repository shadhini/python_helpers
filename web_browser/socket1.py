import socket

# socket is the endpoint from where you gonna send and receive messages

# open the socket
# 2 step process
# 1. create the socet and then socket lives in your computer as an endpoint
# it's the endpoint you gonna receive and send data to, from your computer
# 2. then make the phone call

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # make a phone
mysock.connect(('data.pr4e.org', 80)) # dial phone, domain name and port
# if there's no such domain, then codde gonna blow up here
cmd = 'GE http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode()
# \r return and \n new line: twice there as we have to keep a blank line
# then unicode string in python is converted into a UTF8 by encode function
mysock.send(cmd) # talk first, send the request

while True:
    data = mysock.recv(512) # receive upto 512 characters
    if len(data) < 1:
        break
    print(data.decode(), end='')
    # decode, bcs python itself doesn't use UTF inside it, it used unicode

# protocol tells us we are supposed to receive data until the socket is closed

mysock.close()