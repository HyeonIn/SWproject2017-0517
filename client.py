import sys, socket

IP = "127.0.0.1"
PORT = 8888

print("start client")
s = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)

saddress = (IP, PORT)
s.connect(saddress)

msg = input("원하는 문장을 입력해 : ")

s.sendall(msg.encode())

s.close()