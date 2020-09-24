from socket import *

def createServer():
    serversocket = socket(AF_INET, SOCK_STREAM)
    try:
        # server need to already awake and litening to incoming requests
        serversocket.bind(('localhost', 9000))
        serversocket.listen(5) # Dear operating system, if I'm busy handling one phone call,
        # you can hold on to four more and queue them and then
        # I'll come back and get them for you.
        while(1):
            (clientsocket, address) = serversocket.accept() # this accept is blocking.
            # It stops and it just sits there. And it can sit there forever.
            # And if nobody calls it, nothing happens.
            # The next line never runs until you blow it up or the server goes down
            # HTTP protocol says, client should speak first, so server keeps listening

            rd = clientsocket.recv(5000).decode()
            pieces = rd.split("\n")
            if (len(pieces) > 0): print(pieces[0])

            data = "HTTP/1.1 200 OK\r\\n"
            data += "Content-Type: text/html; charset=utf-8\r\n"
            data += "\r\n"
            data += "<html><body>Hello World</body></html>\r\n\r\n"
            clientsocket.sendall(data.encode())
            clientsocket.shutdown(SHUT_WR)
    except KeyboardInterrupt:
        print("\nShutting down...\n")
    except Exception as exc:
        print("Error:\n")
        print(exc)
    serversocket.close()

print("Access http://localhost:9000")
createServer()