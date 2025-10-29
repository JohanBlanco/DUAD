import interface as gui
import persistance as db
from typing import List, Dict

from week_17.classes.Category import Category
from week_17.classes.FinanceManager import FinanceManager
from week_17.classes.Transaction import Transaction


def execute():
    # load data
    finance_manager = load_data()
    info = {}

    # all the logic
    while True:
        try:
            event, values = gui.display_main_window()

            transaction_matrix, category_matrix = finance_manager.to_matrix()

            if event == gui.get_win_closed() or event == 'Exit':
                break
            elif event == 'List Transactions':
                gui.display_transactions(transaction_matrix, finance_manager.transaction_list)
            elif event == 'Add Expense':
                info = gui.display_add_transaction_window(category_matrix, 'Expense')
                add_transaction(info, finance_manager)
            elif event == 'Add Income':
                info = gui.display_add_transaction_window(category_matrix, 'Income')
                add_transaction(info, finance_manager)
            elif event == 'Add Category':
                info = gui.display_add_category_window()
                add_category(info, finance_manager)

        # in case the window was closed or canceled
        except WindowsError as e:
            print(e)
        except Exception as e:
            print('Unexpected Error -> ', e)

    # save all data before close the window
    save_data(finance_manager)

def add_transaction(info, finance_manager):
    transaction = create_transaction(info, finance_manager.category_list)
    finance_manager.transaction_list.append(transaction)
    save_transaction(transaction.to_dict())

def add_category(info, finance_manager):
    category = create_category(info)
    finance_manager.category_list.append(category)
    save_category(category.to_dict())

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

def create_row_colors_list(data_table, category_list):
    text_color = '#FFFFFF'

    row_colors = []

    for index, row in enumerate(data_table):
        if len(row) >= 4:
            row_category = row[4]
            found_colors = [category.color for category in category_list if category.category == row_category]
            if len(found_colors) > 0:
                color = found_colors[0]
                row_color = (index, text_color, color)
                row_colors.append(row_color)
        else:
            raise ValueError(f'The row {row} has less than 4 elements, the category must be in position 4')

    return row_colors

def save_category(category:Dict):
    db.save_category(category)

def save_transaction(transaction:Dict):
    db.save_transaction(transaction)

def load_data() -> FinanceManager:
    # dictionaries from the db
    categories_data, transactions_data =  db.load_data()

    # convert the dictionaries into objects
    finance_manager = FinanceManager.from_dict(FinanceManager(category_list=categories_data, transaction_list=transactions_data))

    return finance_manager

def save_data(finance_manager: FinanceManager):
    try:
        finance_manager = finance_manager.to_dict()
        db.save_data(finance_manager)
    except Exception as e:
        print('An error occurred while saving data -> ', e)