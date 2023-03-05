from socket import *
from user import *
import database_model

host, port = '192.168.1.8', 8080
ADDR, buff_size = (host, port), 1024

tcp_connection = socket(AF_INET, SOCK_STREAM)
tcp_connection.bind(ADDR)
tcp_connection.listen(5)

while True:
	print('Waiting for connetcion...')
	tcp_client, client_addr = tcp_connection.accept()
	print(f"...connected from: {client_addr}")

	while True:
		tcp_client.send(bytes("PRESS [1] TO REGISTRATION\nPRESS [2] TO CLEAR\nPRESS[0] TO EXIT", 'utf-8'))
		operation = tcp_client.recv(buff_size).decode()
		if not operation:
			break
		elif int(operation) == 1:
			tcp_client.send(bytes(f"Create username: ", 'utf-8'))
			username = tcp_client.recv(buff_size).decode()
			tcp_client.send(bytes("Create secret key(only digits): ", 'utf-8'))
			password = tcp_client.recv(buff_size).decode()
			user = User(username, int(password))
			user.registration()
			tcp_client.send(bytes(f"\nYOU ARE SUCCESSFULLY REGISTERED!\n", 'utf-8'))
		elif int(operation) == 2:
			database_model.clear_database()
			tcp_client.send(bytes(f"\nDatabase cleaned!\n", 'utf-8'))
		elif int(operation) == 0:
			break
	tcp_client.close()
tcp_connection.close()