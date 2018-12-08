import socket
req = [str(x)+'abc' for x in range(10)] 
# req = 'Hello tcp!'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 1234))
for request in req:
    # request = str(request)
    print('request= ', request)
    s.send(request.encode())
    rsp = s.recv(1024)
    print('responce=', rsp)
s.close()
