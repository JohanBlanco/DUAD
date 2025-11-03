import pytest

import week_17.modules.persistence as persistence
from week_17.classes.Category import Category
from week_17.classes.FinanceManager import FinanceManager
from week_17.classes.Transaction import Transaction
from week_17.modules.logic import add_category, add_transaction, get_all_categories, get_all_transactions, export_to_csv

'''
TEST NAME CONVENTION
    - test_function_test_case

TEST STRUCTURE
    - Arrange
    - Act
    - Assert
    
TEST TYPE 
    - E2E test
    
'''

def test_add_transaction_0_categories_added_yet():
    # Arrange
    transaction_list = []
    info = {
            "title": 'New Transaction',
            "type": 'Expense',
            "date": '10/10/2025',
            "amount": '1000',
            "category": 'Not Existing Category'
        }
    persistence.write_json_file([], 'week_17/data/dev/categories.json')

    # Act & Assert
    with pytest.raises(AttributeError):
        add_transaction(info, transaction_list)

def test_add_category_successfully():
    # Arrange
    category = 'Food'
    color = '#FF7F00'
    info = {'category': category, 'color': color}

    category_list = get_all_categories()

    if len(category_list) != 0:
        last_category = category_list[-1]
        category = last_category.category + '_'
        color = last_category.color
        info = {
            'category': category,
            'color': color
        }

    expected = Category(category, color)

    # Act
    add_category(info=info, category_list=category_list)
    stored_category_list = get_all_categories()
    stored_result = stored_category_list.pop()

    runtime_result = category_list.pop()

    # Assert
    assert expected.__eq__(runtime_result) and expected.__eq__(stored_result)

def test_add_category_already_exists():
    # Arrange
    category = 'Food'
    color = '#FF7F00'
    info = {'category': category, 'color': color}

    category_list = get_all_categories()
    if len(category_list) == 0:
        add_category(info=info, category_list=category_list)
    else:
        first_category = category_list[0]
        info = {
            'category': first_category.category,
            'color': first_category.category
        }

    # Act & Assert
    with pytest.raises(ValueError):
        add_category(info=info, category_list=category_list)

def test_add_transaction_successfully():
    # Arrange
    transaction_list = []
    info = {
            "title": 'New Transaction',
            "type": 'Expense',
            "date": '12/10/2025',
            "amount": '1000',
            "category": 'Food'
        }

    # Act
    add_transaction(info, transaction_list)
    stored_transaction_list = get_all_transactions()

    expected = transaction_list.pop()
    result = stored_transaction_list.pop()

    # Assert
    assert expected.__eq__(result)

def test_add_transaction_invalid_date():
    # Arrange
    transaction_list = []
    info = {
            "title": 'New Transaction',
            "type": 'Expense',
            "date": '25/10/2025',
            "amount": '1000',
            "category": 'Food'
        }

    # Act & Assert
    with pytest.raises(ValueError):
        add_transaction(info, transaction_list)

def test_add_transaction_invalid_amount():
    # Arrange
    transaction_list = []
    info = {
            "title": 'New Transaction',
            "type": 'Expense',
            "date": '10/10/2025',
            "amount": '1000x',
            "category": 'Food'
        }

    # Act & Assert
    with pytest.raises(ValueError):
        add_transaction(info, transaction_list)

def test_add_transaction_invalid_category():
    # Arrange
    transaction_list = []
    info = {
            "title": 'New Transaction',
            "type": 'Expense',
            "date": '10/10/2025',
            "amount": '1000',
            "category": 'Not Existing Category'
        }

    # Act & Assert
    with pytest.raises(AttributeError):
        add_transaction(info, transaction_list)

def test_export_to_csv_successfully():
    # Arrange
    transaction = Transaction()
    transaction.title = 'New Transaction'
    transaction.type = 'Expense'
    transaction.date = '10/10/2025'
    transaction.amount = '1000'
    transaction.category = Category(category='Food')

    expected = [transaction]

    finance_manager = FinanceManager(transaction_list=expected)

    # Act
    export_to_csv(finance_manager)
    result = persistence.read_csv_file()
    result[0] = Transaction.from_dict(result[0])

    exp = expected[0]
    exp.category = exp.category.category
    res = result[0]

    # Assert
    assert len(expected) == 1 and len(result) == 1 and exp.__eq__(res)