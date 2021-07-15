import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = 'CLOSE'
SERVER = '10.108.153.183'
ADDR = (SERVER, PORT)
BUF_SZ = 2048

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
	message = msg.encode(FORMAT)
	msg_length = len(message)
	send_length = str(msg_length).encode(FORMAT)
	send_length += b' '*(HEADER-len(send_length))
	client.send(send_length)
	client.send(message)
	#print(client.recv(BUF_SZ))

connected = True

while connected:

	msg = input('Message: ')

	if msg == DISCONNECT_MESSAGE:
		send(DISCONNECT_MESSAGE)
		break
	else:
		send(msg)
	