import socket
import threading

HEADER = 64
PORT = 5050
hostname, aliaslist, ipaddrlist = socket.gethostbyname_ex(socket.gethostname())
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = 'CLOSE'


def find_server_ip(ipaddrlist):
	if len(ipaddrlist) == 1:
		return ipaddrlist[0]

	else:
		if ipaddrlist[0] == '127.0.0.1':
			return find_server_ip(ipaddrlist[1:])

		else:
			return ipaddrlist[0]


def server_bind(addr):
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind(addr)
	return server


def handle_client(conn, addr):
	print(f'[NEW CONNECTION] {addr} connected.')

	connected = True

	while connected:
		msg_length = conn.recv(HEADER).decode(FORMAT)

		if msg_length:
			msg_length = int(msg_length)
			msg = conn.recv(msg_length).decode(FORMAT)

			if msg == DISCONNECT_MESSAGE:
				connected = False

			print(f'[{addr}] {msg}')
			#conn.send('Message received'.enconde(FORMAT))

	conn.close()

def start(server):
	server.listen()
	while True:
		conn, addr = server.accept()
		thread = threading.Thread(target=handle_client, args=(conn,addr))
		thread.start()
		print(f'[ACTIVE CONNECTIONS] {threading.activeCount()-1}')

print('[STARTING] server is starting...')
server_ip = find_server_ip(ipaddrlist)
socket_addr = (server_ip, PORT)
print(f'[SERVER ADDRESS] Binding server to socket {server_ip}:{PORT}')
server = server_bind(socket_addr)
start(server)