class User:
	def __init__(self, login, password):
		self.login = login
		self.password = password

	def show_info(self):
		return str(self.login) + " " + str(self.password)


class SuperUser(User):
	def __init__(self, admin, login, password):
		self.admin = admin
		super(SuperUser, self).__init__(login, password)

	def show_info_admin(self):
		if self.admin == True:
			print(str(self.admin) + " " + super(SuperUser, self).show_info())
		else:
			print(super(SuperUser, self).show_info())


class ProUser(User):
	def __init__(self, billing, login, password):
		self.billing = billing
		super(ProUser, self).__init__(login,password)

	def show_info_pro_user(self):
		if self.billing == True:
			print(f"Your billing is {self.billing} " + super(ProUser, self).show_info())
		else:
			print(super(ProUser, self).show_info())


super_user = SuperUser(False, "admin", 1234)
simple_user = SuperUser(False, "user1", 1222)
pro_user = ProUser(True, "proUser1", 4455)

super_user.show_info_admin()
print(simple_user.show_info())
pro_user.show_info_pro_user()
