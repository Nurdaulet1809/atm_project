from socket import *

host, port = '178.89.113.1', 8080
ADDR, buff_size= (host, port), 1024

tcp_connection = socket(AF_INET, SOCK_STREAM)
tcp_connection.connect(ADDR)


while True:
	data_from_server = tcp_connection.recv(buff_size)
	print(data_from_server.decode())
	data_to_server = input(">>")
	if int(data_to_server) == 0:
		print("\nCONNECTION IS CLOSED!\n")
		break
	tcp_connection.send(bytes(data_to_server, 'utf-8'))


	data_from_server = tcp_connection.recv(buff_size)
	print(data_from_server.decode())
	data_to_server = input(">>")
	tcp_connection.send(bytes(data_to_server, 'utf-8'))

	data_from_server = tcp_connection.recv(buff_size)
	print(data_from_server.decode())
	data_to_server = input(">>")
	tcp_connection.send(bytes(data_to_server, 'utf-8'))

	data_from_server = tcp_connection.recv(buff_size)
	print(data_from_server.decode())

tcp_connection.close()