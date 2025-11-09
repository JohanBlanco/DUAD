from first_module.week_17.classes.Transaction import Transaction
from first_module.week_17.classes.Category import Category


class FinanceManager:
    def __init__(self, transaction_list=None, category_list=None):
        if transaction_list is None:
            self.transaction_list = []
        else:
            self.transaction_list = transaction_list
        if category_list is None:
            self.category_list = []
        else:
            self.category_list = category_list

    def add_transaction(self, transaction):
        self.transaction_list.append(transaction)

    @classmethod
    def from_dict(cls, finance_manager):
        # Rebuild from a lists of dicts
        instance = cls()
        instance.transaction_list = [Transaction.from_dict(t) for t in finance_manager.transaction_list]
        instance.category_list = [Category.from_dict(t) for t in finance_manager.category_list]
        return instance

    def to_dict(self):
        transaction_list = [transaction.to_dict() for transaction in self.transaction_list]
        category_list = [category.to_dict() for category in self.category_list]
        return FinanceManager(transaction_list, category_list)

    def to_matrix(self):
        transactions = []
        categories = []

        for transaction in self.transaction_list:
            transactions.append(transaction.to_matrix())

        for category in self.category_list:
            categories.append(category.to_matrix())

        return transactions, categories