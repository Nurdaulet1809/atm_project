from user import *


def main():
	while True:
		print("PRESS [1] TO REGISTRATION\nPRESS [2] TO LOGIN\nPRESS[0] TO EXIT")
		operation = int(input(">>"))
		if operation == 1:
			print("Enter username: ")
			username = input(">>")
			print("Enter secret key: ")
			password = int(input(">>"))
			user = User(username, password)
			user.registration()
		elif operation == 0:
			break


if __name__ == '__main__':
	main()





