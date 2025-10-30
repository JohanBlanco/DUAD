import interface as gui
import persistance as persistance
from typing import List, Dict

from week_17.classes.Category import Category
from week_17.classes.FinanceManager import FinanceManager
from week_17.classes.Transaction import Transaction


def execute():
    # load data
    finance_manager = load_data()

    transaction_list = finance_manager.transaction_list
    category_list = finance_manager.category_list

    transaction_matrix, category_matrix = finance_manager.to_matrix()

    main_window = gui.start_main_window(transaction_matrix, category_list)
    success_massage = ''

    # all the logic
    while True:
        try:
            transaction_matrix, category_matrix = finance_manager.to_matrix()

            event, values = gui.read_from_window(main_window)

            if event == gui.get_win_closed()  or event == 'Exit':
                break

            if event == 'Add Expense':
                info = gui.disable_window_and_popup_another(main_window, gui.display_add_transaction_window, category_matrix, 'Expense')
                add_transaction(info, transaction_list, category_list)
                success_massage = 'Expense added successfully'
            elif event == 'Add Income':
                info = gui.disable_window_and_popup_another(main_window, gui.display_add_transaction_window, category_matrix,'Income')
                add_transaction(info, transaction_list, category_list)
                success_massage = 'Income added successfully'
            elif event == 'Add Category':
                info = gui.disable_window_and_popup_another(main_window, gui.display_add_category_window)
                add_category(info, category_list)
                success_massage = 'Category added successfully'
            elif event == 'Export to CSV':
                export_to_csv(finance_manager)
                success_massage = 'Data successfully exported to the export directory'
            else:
                gui.do_filter_table_logic(event, values, main_window, transaction_matrix, finance_manager.category_list)

            if success_massage != '':
                transaction_matrix, category_matrix = finance_manager.to_matrix()
                
                gui.update_table(main_window, 'table', transaction_matrix, category_list)
                gui.display_notification(success_massage)
                success_massage = ''

        # in case the window was closed or canceled
        except WindowsError as e:
            print(e)
        except ValueError as e:
            gui.display_error(e)
            print(e)
        except Exception as e:
            gui.display_error(e)
            print('Unexpected Error -> ', e)

    # save all data before close the window
    gui.close_window(main_window)
    save_data(finance_manager)

def export_to_csv(finance_manager:FinanceManager):
    headers = ['date', 'title', 'amount','category', 'type']
    finance_manager = finance_manager.to_dict()
    transaction_dict_list = finance_manager.transaction_list
    for transaction_dict in transaction_dict_list:
        category = transaction_dict['category']
        transaction_dict['category'] = category['category']
    persistance.export_to_csv(transaction_dict_list, headers)

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

def save_category(category:Dict):
    persistance.save_category(category)

def save_transaction(transaction:Dict):
    persistance.save_transaction(transaction)

def load_data() -> FinanceManager:
    # dictionaries from the persistance layer
    categories_data, transactions_data =  persistance.load_data()

    # convert the dictionaries into objects
    finance_manager = FinanceManager.from_dict(FinanceManager(category_list=categories_data, transaction_list=transactions_data))

    return finance_manager

def save_data(finance_manager: FinanceManager):
    finance_manager = finance_manager.to_dict()
    persistance.save_data(finance_manager)