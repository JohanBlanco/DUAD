import week_17.modules.logic as logic
import week_17.modules.interface as gui

def run():
    try:
        # load data
        finance_manager = logic.load_data()

        transaction_list = finance_manager.transaction_list
        category_list = finance_manager.category_list

        transaction_matrix, category_matrix = finance_manager.to_matrix()

        main_window = gui.display_main_window(transaction_matrix, category_list)
        success_massage = ''

        # all the logic
        while True:
            try:
                transaction_matrix, category_matrix = finance_manager.to_matrix()

                event, values = gui.read_from_window(main_window)

                if event == gui.get_win_closed() or event == 'Exit':
                    break

                if event == 'Add Expense':
                    info = gui.disable_window_and_popup_another(main_window, gui.display_add_transaction_window,
                                                                category_matrix, 'Expense')
                    logic.add_transaction(info, transaction_list)
                    success_massage = 'Expense added successfully'
                elif event == 'Add Income':
                    info = gui.disable_window_and_popup_another(main_window, gui.display_add_transaction_window,
                                                                category_matrix, 'Income')
                    logic.add_transaction(info, transaction_list)
                    success_massage = 'Income added successfully'
                elif event == 'Add Category':
                    info = gui.disable_window_and_popup_another(main_window, gui.display_add_category_window)
                    logic.add_category(info, category_list)
                    success_massage = 'Category added successfully'
                elif event == 'Export to CSV':
                    logic.export_to_csv(finance_manager)
                    success_massage = 'Data successfully exported to the export directory'
                elif event == 'from_date_input' or event == 'to_date_input':
                    gui.validate_dates(main_window, event, values)
                elif event == 'filter':
                    gui.filter_table(main_window, values, transaction_matrix, category_list)
                elif event == 'clear_filter':
                    gui.clear_filters(main_window, transaction_matrix, category_list)

                if success_massage != '':
                    transaction_matrix, category_matrix = finance_manager.to_matrix()

                    gui.update_table(main_window, transaction_matrix, category_list)
                    gui.display_notification(success_massage)
                    success_massage = ''

            # in case the window was closed or canceled
            except WindowsError as e:
                print(e)
            except ValueError as e:
                gui.display_error(e)
                print(e)
            except AttributeError as e:
                gui.display_error(e)
                print(e)
            except Exception as e:
                gui.display_error(f'Unexpected Error -> {e}')
                print('Unexpected Error -> ', e)

        # save all data before close the window
        gui.close_window(main_window)
        logic.save_data(finance_manager)

    except Exception as e:
        print('Unexpected Error -> ', e)