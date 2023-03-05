import atm_operations
import database_model


def atm(user_id, account):
	while True:
		print("""Введите цифру операции\n1-снятие денег, 2-пополнение счета, 
				3-перевод в депозит, 0-для выхода""", end='\n')
		operation_id = int(input(">>"))

		if operation_id == 1:
			print("Введите сумму для снятие:", end='\n')
			withdraw_money = float(input('>>'))
			account = atm_operations.withdraw(account, withdraw_money)
			database_model.update_account(user_id, account)

		elif operation_id == 2:
			print("Введите сумму для пополнение:", end='\n')
			recharge_money = float(input('>>'))
			account = atm_operations.recharge(account, recharge_money)
			database_model.update_account(user_id, account)

		elif operation_id == 3:
			atm_operations.show_info(account)

		elif operation_id == 4:
			print("Введите сумме для депозита:")
			deposit_money = float(input(">>"))
			local_list = atm_operations.deposit(account, deposit_money)
			account = local_list[0]
			deposit = local_list[1]

		elif operation_id == 0:
			break
