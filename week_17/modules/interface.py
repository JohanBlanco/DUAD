from datetime import datetime, date
import PySimpleGUI as sg


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
            sg.InputText('', key='from_input', size=(9, 1), disabled=True, enable_events=True), sg.CalendarButton('From',key= 'from_picker',target='from_input',format='%m/%d/%Y'),
            sg.InputText('', key='to_input', size=(9, 1), disabled= True, enable_events=True), sg.CalendarButton('To',key= 'to_picker',target='to_input',format='%m/%d/%Y'),
            sg.Button("Filter"), sg.Button("Clear Filter"),
        ],
        [
            sg.Column([ [sg.Table(values=data_table, headings=heading, key='-TABLE-')] ], element_justification='center')
        ]
    ]

    window = sg.Window(title, layout)

    while True:
        event, values = window.read()
        print(event, values)

        if event == sg.WIN_CLOSED:
            break
        elif event == 'from_input' or event == 'to_input':
            event_date = values[event]
            from_date = values['from_input']
            to_date = values['to_input']

            if not is_date_before_or_equals_today(event_date):
                sg.popup_error(f'The date can not be in the future')
                window[event].update('')
            elif not is_from_before_or_equals_to(from_date_string=from_date, to_date_string=to_date):
                sg.popup_error(f'From date {from_date} is greate than {to_date}')
                window[event].update('')

        elif event == 'Filter':
            filtered_data = data_table.copy()
            from_date = string_to_date(values['from_input'])
            to_date = string_to_date(values['to_input'])
            filtered_data = [
                row for row in filtered_data
                    if from_date <= string_to_date(row[0]) <= to_date
            ]
            window['-TABLE-'].update(values=filtered_data)

        elif event == 'Clear Filter':
            window['from_input'].update('')
            window['to_input'].update('')

            window['-TABLE-'].update(values=data_table)

    window.close()


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

