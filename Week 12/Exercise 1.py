class BankAccount:
    def __init__(self):
        self._balance = 0

    def add_money(self, amount):
        self._balance += amount

    def withdraw_money(self, amount):
        self._balance -= amount

class SavingsAccount(BankAccount):
    def __init__(self, min_balance):
        super().__init__()
        self._min_balance = min_balance
    
    def withdraw_money(self, amount):
        new_value = self._balance - amount
        if new_value < self._min_balance: 
            raise Exception(f'Invalid Transaction, the balance can not be less than {self._min_balance}')
        else:
            self.balance = new_value
    
if __name__ == '__main__':
    bank_account = BankAccount()
    bank_account.withdraw_money(5)

    try:
        savings_account = SavingsAccount(5)
        savings_account.add_money(7)
        savings_account.withdraw_money(5)
    except Exception as e:
        print(e)
