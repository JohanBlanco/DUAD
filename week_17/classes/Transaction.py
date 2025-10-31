from week_17.classes.Category import Category


class Transaction:
    def __init__(self,title = '', type='', date='',  amount='', category=Category()):
        self.amount = amount
        self.title = title
        self.type = type
        self.date = date
        self.category = category

    def to_dict(self):
        return {
            "title": self.title,
            "type": self.type,
            "date": self.date,
            "amount": self.amount,
            "category": self.category.to_dict() if hasattr(self.category, "to_dict") else self.category
        }

    @classmethod
    def from_dict(cls, data):
        # make a shallow copy so we can modify it safely
        data = data.copy()

        # if category is a dict, convert it first
        if isinstance(data.get("category"), dict):
            data["category"] = Category.from_dict(data["category"])

        # now unpack safely
        return cls(**data)

    def to_matrix(self):
        transaction_dict =  self.to_dict()
        transaction_dict['category'] = self.category.to_matrix()

        return [
            transaction_dict['date'],
            transaction_dict['title'],
            transaction_dict['amount'],
            transaction_dict['category'],
            transaction_dict['type'],
        ]

