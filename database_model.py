import json


def get_register_id():
	with open("database.json", 'r') as file_out:
		py_obj = json.load(file_out)
	data = dict(py_obj)
	for key in data.keys():
		if data[key] == {}:
			return key


def clear_database():
	users = {}
	for id_line in range(1, 21):
		users[id_line] = {}
	with open("database.json", 'w') as file_in:
		json.dump(users, file_in, indent=4)


def update_account(user_id_in: int, account_in: float):
	pass
