import json
import os

from week_17.classes.FinanceManager import FinanceManager

categories_json_path = '../data/categories.json'
transactions_json_path = '../data/transactions.json'

def read_json_file(path):
    if not os.path.exists(path) or os.path.getsize(path) == 0:
        return []  # File doesn’t exist or is empty

    with open(path, 'r') as file:
        try:
            json_content = json.load(file)
            return json_content
        except json.JSONDecodeError:
            raise ValueError(f'Invalid JSON file content in {path}')

def write_json_file(dict_content, path):
    try:
        json_string = json.dumps(dict_content, indent=4)
        with open(path, 'w') as file:
            file.write(json_string)
    except Exception as e:
        print(e)

def save_category(category_dict):
    categories = read_json_file(categories_json_path)
    categories.append(category_dict)
    write_json_file(categories, categories_json_path)

def save_transaction(transaction_dict):
    transactions = read_json_file(transactions_json_path)
    transactions.append(transaction_dict)
    write_json_file(transactions, transactions_json_path)


def load_data():
    categories = read_json_file(categories_json_path)
    transactions = read_json_file(transactions_json_path)
    return categories, transactions

def save_data(file_manager:FinanceManager):

    write_json_file(file_manager.category_list, categories_json_path)
    write_json_file(file_manager.transaction_list, transactions_json_path)