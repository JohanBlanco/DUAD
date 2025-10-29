import interface as display
from typing import List
from week_17.classes.Transaction import Transaction


def execute():
    transaction_list = [['12/10/2024','Transaction', '$20', 'Food', 'Expense'],
                        ['12/10/2023','Transaction', '$20', 'Transportation', 'Expense']]
    category_list = [['Food'], ['Transportation']]
    info = {}

    while True:
        try:
            event, values = display.display_main_window()
            if event == display.get_win_closed() or event == 'Exit':
                break
            elif event == 'List Transactions':
                display.display_transactions(transaction_list)
            elif event == 'Add Expense':
                info = display.display_add_transaction_window(category_list, 'Expense')
            elif event == 'Add Income':
                info = display.display_add_transaction_window(category_list, 'Income')
            elif event == 'Add Category':
                info = display.display_add_category_window()

            print(info)
        except WindowsError as e:
            print(e)
        except Exception as e:
            print('Unexpected Error -> ', e)