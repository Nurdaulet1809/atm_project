import database_model, json


class User:
	def __init__(self, username: str, secret: int, account: float = 0):
		self.username = username
		self.account = account
		self.secret = secret

	def registration(self):
		register_id = int(database_model.get_register_id())
		user_data = {"fst_name": self.username, "secret": self.secret, "account": self.account}
		with open("database.json", 'r') as file_out:
			data = json.load(file_out)
			data = dict(data)
		data[str(register_id)] = user_data

		with open("database.json", 'w') as file_in:
			json.dump(data, file_in, indent=4)


