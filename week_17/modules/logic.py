import persistence as persistence
from typing import List, Dict

from week_17.classes.Category import Category
from week_17.classes.FinanceManager import FinanceManager
from week_17.classes.Transaction import Transaction


'''
Recreate Object
    - Create the object based on the info from the GUI
'''
def create_category(info:Dict) -> Category:
    return Category.from_dict(info)

def create_transaction(info:Dict, category_list:List[Category]) -> Transaction:
    info = info.copy()

    # info has the category id, so let's find the correct category object
    filter = [category for category in category_list
                if info['category'] == category.category]

    if len(filter) > 0:
        category = filter[0]
        info['category'] = category
    else:
        raise AttributeError(f'Category {info['category']} not found')

    return Transaction.from_dict(info)

'''
Create/Add Methods
    - Recreate Object
    - Add the object to runtime list
    - Save the info in the file
'''

def add_transaction(info, transaction_list, category_list):
    transaction = create_transaction(info, category_list)
    transaction_list.append(transaction)
    save_transaction(transaction.to_dict())

def add_category(info, category_list):
    category = create_category(info)

    # The Category already exist
    search = [existing for existing in  category_list if existing.category == category.category]
    if len(search) > 0:
        raise ValueError(f'Category {category.category} was not added it already exists')

    category_list.append(category)
    save_category(category.to_dict())

'''
Persistence Data Methods: communicate to persistence layer to load/store data
'''

'''
Load Data Method
    - Loads the data from the files used as db
'''
def load_data() -> FinanceManager:
    # dictionaries from the persistence layer
    transactions_data =  load_transactions()
    categories_data = load_categories()

    # convert the dictionaries into objects
    finance_manager = FinanceManager.from_dict(FinanceManager(category_list=categories_data, transaction_list=transactions_data))

    return finance_manager

def load_transactions():
    return persistence.load_transactions()

def load_categories():
    return persistence.load_categories()

'''
Save Methods: communicates to persistence layer to load/store data
    - save_category
    - save_transaction
    - save_data: Saves all the data in file_manager_object
    - export_to_csv: exports the transactions to a csv file
'''

def save_category(category:Dict):
    persistence.save_category(category)

def save_transaction(transaction:Dict):
    persistence.save_transaction(transaction)


def save_data(finance_manager: FinanceManager):
    finance_manager = finance_manager.to_dict()
    persistence.save_data(finance_manager)

def export_to_csv(finance_manager:FinanceManager):
    headers = ['date', 'title', 'amount','category', 'type']
    finance_manager = finance_manager.to_dict()
    transaction_dict_list = finance_manager.transaction_list
    for transaction_dict in transaction_dict_list:
        category = transaction_dict['category']
        transaction_dict['category'] = category['category']
    persistence.export_to_csv(transaction_dict_list, headers)