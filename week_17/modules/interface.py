from datetime import date
import PySimpleGUI as sg
from typing import Dict, List

'''
Layouts
These methods help to keet the methods shorted
and the code easier to read
This can simulate the html forms
'''
def get_main_menu_layout():
    return [
        [sg.Text("Menu", font=("Helvetica", 16), justification='center')],
        [sg.Column([
            [sg.Button("Add Expense", size=(15, 1))],
            [sg.Button("Add Income", size=(15, 1))],
            [sg.Button("Add Category", size=(15, 1))],
            [sg.Button("Export to CSV", size=(15, 1))],
            [sg.Button("Exit", size=(15, 1))]
        ], element_justification='center')]
    ]

def get_transaction_table_layout(data_table, category_list):
    heading = ["Date", "Tile", "Amount", 'Category', 'Type']
    row_colors = create_row_colors_list(data_table, category_list)

    layout = [
        [
            sg.InputText('', key='from_date_input', size=(9, 1), disabled=True, enable_events=True),
            sg.CalendarButton('From', key='from_picker', target='from_date_input', format='%m/%d/%Y'),
            sg.InputText('', key='to_date_input', size=(9, 1), disabled=True, enable_events=True),
            sg.CalendarButton('To', key='to_picker', target='to_date_input', format='%m/%d/%Y'),

            sg.Push(),
            sg.Column([
                [
                    sg.Button('Filter', key='filter'),
                    sg.Button('Clear Filter', key='clear_filter')
                ]
            ], element_justification='right', expand_x=True)
        ],
        [
            sg.Column([
                [sg.Table(values=data_table, headings=heading, key='table', vertical_scroll_only=False, row_colors=row_colors)]
            ], element_justification='center', expand_x=True)
        ]
    ]

    return layout

def get_add_transaction_layout(transaction_type:str, category_list):
    return [
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

def get_add_category_layout():
    return [
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

def get_main_window_layout(left_layout, right_layout):
    return [
        [
            sg.Column(left_layout, element_justification='center', background_color='#DDDDDD'),
            sg.VSeperator(),
            sg.Column(right_layout, element_justification='center')
        ]
    ]

'''
Display window methods
'''
def display_main_window(data_table, category_list):
    title = 'Finance Manager'

    # MENU
    left_layout = get_main_menu_layout()

    # TABLE
    right_layout = get_transaction_table_layout(data_table, category_list)

    layout = get_main_window_layout(left_layout, right_layout)

    window = sg.Window(title, layout)

    return window

def display_add_transaction_window(category_list, transaction_type:str):
    if len(category_list) != 0:
        transaction_type = transaction_type.capitalize()

        title = f'Finance Manager - Add {transaction_type}'

        layout = get_add_transaction_layout(transaction_type, category_list)

        window = sg.Window(title, layout, element_justification='center')

        info = get_validated_transaction_info(window, transaction_type)

        window.close()
    else:
        sg.popup_error('Add a at least 1 category before adding a transaction', title='Error')
        raise WindowsError()
    return info

def display_add_category_window():
    title = 'Finance Manager - Add Category'

    layout = get_add_category_layout()

    window = sg.Window(title, layout, element_justification='center')

    info = get_validated_category_info(window)

    window.close()

    return info

'''
Action Methods
These methods are helpful to do the actions on each window and keep a cleaner code
'''

def get_validated_category_info(window):
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'cancel':
            window.close()
            raise WindowsError(f"The window {window.Title} was closed or canceled")

        info = {
            'category': values['category'].strip(),
            "color": values['color']
        }

        if event == 'add':
            if is_there_an_empty_field(info):
                sg.popup_error('All fields are mandatory', title='Error')
            else:
                return info

def get_validated_transaction_info(window, transaction_type):
    # Validations
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'cancel':
            window.close()
            raise WindowsError(f"The window {window.Title} was closed or canceled")

        info = {
            'type': transaction_type,
            "title": values['title'],
            "category": values['category'],
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


def validate_dates(window, event, values):
    from_date_string = values['from_date_input']
    to_date_string = values['to_date_input']

    event_date = values[event]

    if not is_date_before_or_equals_today(event_date):
        sg.popup_error(f'The date can not be in the future', title='Error')
        window[event].update('')
    elif not is_from_date_before_to_date(from_date_string=from_date_string, to_date_string=to_date_string):
        sg.popup_error(f'From date {from_date_string} is greate than To date {to_date_string}', title='Error')
        window[event].update('')

def filter_table(window, values, data_table, category_list):

    from_date_string = values['from_date_input']
    to_date_string = values['to_date_input']

    if  len(from_date_string) > 0 and len(to_date_string) > 0:
        filtered_data = []

        from_date = string_to_date(values['from_date_input'])
        to_date = string_to_date(values['to_date_input'])

        for row in data_table:
            row_date = string_to_date(row[0])
            if from_date <= row_date <= to_date:
                filtered_data.append(row)

        row_colors = create_row_colors_list(filtered_data, category_list)
        window['table'].update(values=filtered_data, row_colors=row_colors)

def clear_filters(window, data_table, category_list):
    window['from_date_input'].update('')
    window['to_date_input'].update('')

    row_colors = create_row_colors_list(data_table, category_list)
    window['table'].update(values=data_table, row_colors=row_colors)

def disable_window_and_popup_another(window, func, *args, **kwargs):
    window.disable()
    try:
        result = func(*args, **kwargs)
        window.enable()
    # The window was closed or canceled
    except WindowsError as e:
        window.enable()
        raise e
    return result

def update_table(window, data, category_list):
    row_colors = create_row_colors_list(data, category_list)
    window['table'].update(values=data, row_colors=row_colors)

'''
Validation functions
Help to validate the information on each window/form
'''
def is_there_an_empty_field(fields:Dict):
    return_value = False

    for key, value in fields.items():
        if value.strip() == '':
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

def is_date_before_or_equals_today(string):
    date_in_string = string_to_date(string)
    today = date.today()

    return date_in_string <= today

def is_from_date_before_to_date(from_date_string:str, to_date_string:str):
    return_value = True

    if len(from_date_string.strip()) != 0 and len(to_date_string.strip()) != 0:
        from_date = string_to_date(from_date_string)
        to_date = string_to_date(to_date_string)

        return_value =  from_date <= to_date

    return return_value

'''
Helper functions
'''

def string_to_date(string):
    month, day, year = string.split('/')
    return date(int(year), int(month), int(day))

def get_win_closed():
    return sg.WIN_CLOSED

def read_from_window(window):
    event, values = window.read()
    return event, values

def display_notification(message):
    sg.popup_notify(message)

def display_error(error):
    sg.popup_error(error)

def close_window(window):
    window.close()

def get_text_color_based_on_row_brightness(row_color:str):

    row_color = row_color.lstrip('#')
    r, g, b = [int(row_color[i:i+2], 16) for i in (0, 2, 4)]

    # Calculate brightness (W3C formula)
    brightness = (0.299 * r + 0.587 * g + 0.114 * b)

    # Choose text color based on brightness
    text_color = '#000000' if brightness > 127 else '#FFFFFF'

    return text_color

def create_row_colors_list(data_table, category_list):
    row_colors = []

    for row_number, row in enumerate(data_table):
        if len(row) >= 3:
            row_category = row[3]
            found_colors = [category.color for category in category_list if category.category == row_category]
            if len(found_colors) > 0:
                row_color = found_colors[0]
                text_color = get_text_color_based_on_row_brightness(row_color)
                row_color_info = (row_number, text_color, row_color)
                row_colors.append(row_color_info)
        else:
            raise ValueError(f'The row {row} has less than 4 elements, the category must be in position 3')

    return row_colors