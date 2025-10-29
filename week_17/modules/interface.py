from datetime import datetime, date
import PySimpleGUI as sg
from typing import Dict, List


def get_win_closed():
    return sg.WIN_CLOSED

def display_main_window():
    title = 'Finance Manager'

    layout = [
        [sg.Text("Menu", font=("Helvetica", 16), justification='center')],
        [sg.Column([
            [sg.Button("List Transactions", size=(15, 1))],
            [sg.Button("Add Expense", size=(15, 1))],
            [sg.Button("Add Income", size=(15, 1))],
            [sg.Button("Add Category", size=(15, 1))],
            [sg.Button("Exit", size=(15, 1))]
        ], element_justification='center')]
    ]

    window = sg.Window(title, layout, element_justification='center')

    event, values = window.read()
    window.close()
    return event, values

def display_transactions(data_table):
    title = 'Finance Manager - Transactions'

    heading = ["Date", "Tile", "Amount", 'Category', 'Type']

    layout = [
        [
            sg.Button('Back to Menu', key='back', button_color=('white', 'red'), bind_return_key=True),
            sg.Push(),
            sg.Column([
                [
                    sg.InputText('', key='from_date_input', size=(9, 1), disabled=True, enable_events=True),
                    sg.CalendarButton('From', key='from_picker', target='from_date_input', format='%m/%d/%Y'),
                    sg.InputText('', key='to_date_input', size=(9, 1), disabled=True, enable_events=True),
                    sg.CalendarButton('To', key='to_picker', target='to_date_input', format='%m/%d/%Y'),
                    sg.Button('Filter', key='filter'),
                    sg.Button('Clear Filter', key='clear_filter')
                ]
            ], element_justification='right', expand_x=True)
        ],
        [
            sg.Column([
                [sg.Table(values=data_table, headings=heading, key='table')]
            ], element_justification='center', expand_x=True)
        ]
    ]


    window = sg.Window(title, layout)

    do_filter_table_logic(data_table,window)

    window.close()

def display_add_transaction_window(category_list, transaction_type:str):
    if len(category_list) != 0:
        transaction_type = transaction_type.capitalize()

        title = f'Finance Manager - Add {transaction_type}'

        layout = [
            [sg.Text(f"Add {transaction_type}", font=("Helvetica", 16), justification='center', expand_x=True)],
            [
                sg.Column([
                    [
                        sg.Column([
                            [sg.Text('Title')],
                            [sg.Text('Category')],
                            [sg.Text('Date')],
                            [sg.Text('Amount')]
                        ], element_justification='left', pad=(0, 0)),

                        sg.Column([
                            [sg.InputText('', key='title', size=(20, 1))],
                            [sg.Combo(category_list, key='category', size=(18, 1), default_value=category_list[0], enable_events=True, readonly=True)],
                            [
                                sg.InputText('', key='date_input', size=(11, 1), disabled=True, enable_events=True),
                                sg.CalendarButton('Choose', key='picker', target='date_input', format='%m/%d/%Y')
                            ],
                            [sg.InputText('', key='amount', size=(20, 1), enable_events=True)]
                        ], element_justification='right', pad=(10, 0))
                    ],
                    [
                        sg.Button("Cancel", key='cancel', button_color=('white', 'red')),
                        sg.Button("Add", key='add', button_color=('white', 'green'))
                    ]
                ], element_justification='center')
            ]
        ]

        window = sg.Window(title, layout, element_justification='center')

        info = get_validated_transaction_info(window, category_list, transaction_type)

        window.close()

        return info
    else:
        sg.popup_error('Add a at least 1 category before adding a transaction', title='Error')

def display_add_category_window():
    title = 'Finance Manager - Add Category'

    layout = [
        [sg.Text(f"Add Category", font=("Helvetica", 16), justification='center', expand_x=True)],
        [
            sg.Column([
                [
                    sg.Column([
                        [sg.Text('Category')],
                        [sg.Text('Color')],
                    ], element_justification='left', pad=(0, 0)),

                    sg.Column([
                        [sg.InputText('', key='category', size=(31, 1), enable_events=True)],
                        [sg.InputText(key='color', size=(20, 1), readonly=True, enable_events=True),
                         sg.ColorChooserButton('Pick Color', target='color')]
                    ], element_justification='right', pad=(10, 0))
                ],
                [
                    sg.Button("Cancel", key='cancel', button_color=('white', 'red')),
                    sg.Button("Add", key='add', button_color=('white', 'green'))
                ]
            ], element_justification='center')
        ]
    ]

    window = sg.Window(title, layout, element_justification='center')

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'cancel':
            window.close()
            raise WindowsError(f"The window {window.Title} was closed or canceled")

        info = {
            'category': values['category'],
            "color": values['color']
        }

        if event == 'add':
            if is_there_an_empty_field(info):
                sg.popup_error('All fields are mandatory', title='Error')
            else:
                window.close()
                return info

def get_validated_transaction_info(window, category_list, transaction_type):
    # Validations
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'cancel':
            window.close()
            raise WindowsError(f"The window {window.Title} was closed or canceled")

        info = {
            'type': transaction_type,
            "title": values['title'],
            "category": values['category'][0],
            "date": values['date_input'],
            "amount": values['amount']
        }


        if event == 'amount':
            numeric_list = [info[event]]
            if not are_all_elements_numeric(numeric_list):
                sg.popup_error('The amount must be a numeric value, for decimals use the dot symbol', title='Error')
                window[event].update('')
        if event == 'date_input':
            if not is_date_before_or_equals_today(info['date']):
                sg.popup_error(f'The date can not be in the future', title='Error')
                window[event].update('')
        elif event == 'add':
            if is_there_an_empty_field(info):
                sg.popup_error('All fields are mandatory', title='Error')
            else:
                return info


def is_there_an_empty_field(fields:Dict):
    return_value = False

    for key, value in fields.items():
        if value == '':
            return_value =  True
            break

    return return_value


def are_all_elements_numeric(numeric_list:List):
    return_value = True

    for number in numeric_list:
        try:
            float(number)
        except ValueError:
            print(f'{number} is not a numeric value')
            return_value =  False
            break

    return return_value

def do_filter_table_logic(data_table, window):

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'back':
            break

        from_date_string = values['from_date_input']
        to_date_string = values['to_date_input']

        # Validates the dates are the correct values in order to filter
        if event == 'from_date_input' or event == 'to_date_input':
            event_date = values[event]

            if not is_date_before_or_equals_today(event_date):
                sg.popup_error(f'The date can not be in the future', title='Error')
                window[event].update('')
            elif not is_from_before_or_equals_to(from_date_string=from_date_string, to_date_string=to_date_string):
                sg.popup_error(f'From date {from_date_string} is greate than To date {to_date_string}', title='Error')
                window[event].update('')

        elif event == 'filter' and len(from_date_string) > 0 and len(to_date_string) > 0:
            filtered_data = data_table.copy()
            from_date = string_to_date(from_date_string)
            to_date = string_to_date(to_date_string)
            filtered_data = [
                row for row in filtered_data
                if from_date <= string_to_date(row[0]) <= to_date
            ]
            window['table'].update(values=filtered_data)

        elif event == 'clear_filter':
            window['from_date_input'].update('')
            window['to_date_input'].update('')

            window['table'].update(values=data_table)

def is_date_before_or_equals_today(string):
    date_in_string = string_to_date(string)
    today = date.today()

    return date_in_string <= today

def is_from_before_or_equals_to(from_date_string:str, to_date_string:str):
    return_value = True

    if len(from_date_string.strip()) != 0 and len(to_date_string.strip()) != 0:
        from_date = string_to_date(from_date_string)
        to_date = string_to_date(to_date_string)

        return_value =  from_date <= to_date

    return return_value

def string_to_date(string):
    month, day, year = string.split('/')
    return date(int(year), int(month), int(day))

