import interface as display

def execute():
    transaction_list = [['10/12/2024','Transaction', '$20', 'Birthdays', 'Expense'],
                        ['10/12/2023','Transaction', '$20', 'Birthdays', 'Expense']]
    while True:
        event, values = display.display_main_window()
        if event == display.get_win_closed() or event == 'Exit':
            break
        elif event == 'List Transactions':
            display.display_transactions(transaction_list)