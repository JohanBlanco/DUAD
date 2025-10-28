from week_17.classes.Transaction import Transaction


class FinanceManager:
    def __init__(self):
        self.transaction_list = []

    def add_transaction(self, transaction):
        self.transaction_list.append(transaction)

    @classmethod
    def from_dict(cls, data):
        # Rebuild from a list of transaction dicts
        instance = cls()
        instance.transaction_list = [Transaction.from_dict(t) for t in data]
        return instance

    def to_dict(self):
        return [t.to_dict() for t in self.transaction_list]