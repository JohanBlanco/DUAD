from datetime import datetime
from typing import Dict

from first_module.week_17.classes.Category import Category
from first_module.week_17.classes.FinanceManager import FinanceManager
from first_module.week_17.classes.Transaction import Transaction
import first_module.week_17.modules.persistence as persistence


'''
Recreate Object
    - Create the object based on the info from the GUI
'''
def create_category(info:Dict) -> Category:
    category = info['category'].strip()

    # The Category already exist
    category_list  = get_all_categories()

    search = [existing for existing in category_list if existing.category == category]
    if len(search) > 0:
        raise ValueError(f'Category {category} was not added it already exists')

    return Category.from_dict(info)

def create_transaction(info:Dict) -> Transaction:
    category_list = get_all_categories()

    if len(category_list) == 0:
        raise AttributeError('Add a at least 1 category before adding a transaction')

    validate_date(info['date'])
    validate_numeric_value(info['amount'])

    # info has the category id, so let's find the correct category object
    filtered = [category for category in category_list
                if info['category'].strip() == category.category]

    if len(filtered) > 0:
        category = filtered[0]
        info['category'] = category
    else:
        raise AttributeError(f'Category {info['category']} not found in the system')


    return Transaction.from_dict(info)

'''
Create/Add Methods
    - Recreate Object
    - Add the object to runtime list
    - Save the info in the file
'''

def add_transaction(info, transaction_list):
    transaction = create_transaction(info)
    transaction_list.append(transaction)
    save_transaction(transaction.to_dict())

def add_category(info, category_list):
    category = create_category(info)
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
    transactions_list =  get_all_transactions()
    categories_list = get_all_categories()

    # convert the dictionaries into objects
    finance_manager = FinanceManager(category_list=categories_list, transaction_list=transactions_list)

    return finance_manager

def get_all_transactions():
    transactions_data = persistence.load_transactions()
    finance_manager = FinanceManager.from_dict(FinanceManager(transaction_list=transactions_data))
    return finance_manager.transaction_list

def get_all_categories():
    categories_data = persistence.load_categories()
    finance_manager = FinanceManager.from_dict(FinanceManager(category_list=categories_data))
    return finance_manager.category_list

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

def export_to_csv(finance_manager: FinanceManager):
    if len(finance_manager.transaction_list) != 0:
        headers = ['date', 'title', 'amount', 'category', 'type']
        finance_manager = finance_manager.to_dict()
        transaction_dict_list = finance_manager.transaction_list
        for transaction_dict in transaction_dict_list:
            category = transaction_dict['category']
            transaction_dict['category'] = category['category']
        persistence.export_to_csv(transaction_dict_list, headers)
    else:
        raise ValueError('There are 0 transactions in the system yer')

'''
Helper Methods
'''
def validate_date(string, date_format = '%m/%d/%Y'):
    try:
        datetime.strptime(string, date_format)
    except ValueError:
        raise ValueError(f'Invalid date {string}, the date format is mm/dd/yyyy')

def validate_numeric_value(string):
    try:
        float(string)
    except ValueError:
        raise ValueError(f'Invalid value, {string} must be a numeric value')