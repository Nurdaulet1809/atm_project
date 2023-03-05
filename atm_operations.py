def show_info(account_in: float) -> None:
	print(f"\n'Остаток на счете {account_in}KZT'\n")


def withdraw(account_in: float, money: float) -> float:
	account_in = account_in - money
	print(f"\n'Снято сумма денег {money}KZT.\nОстаток на счете {account_in}KZT'\n")
	return account_in


def recharge(account_in: float, money: float) -> float:
	account_in = account_in + money
	print(f"\n'Внесено денег в сумме {money}KZT.\nОстаток на счете {account_in}KZT'\n")
	return account_in


def deposit(account_in: float, money_for_deposit: float) -> list:
	deposit_percent = 13.5
	account_in = account_in - money_for_deposit
	changed_deposit = money_for_deposit + (money_for_deposit*deposit_percent)/100
	print(f"\n'Сумма в депозите {changed_deposit}KZT'\n")
	return [account_in, changed_deposit]

