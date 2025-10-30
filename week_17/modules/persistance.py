import json
import csv
import os

from week_17.classes.FinanceManager import FinanceManager


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

def write_csv_file(data, headers, path):
    with open(path, 'w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, headers, delimiter="\t")
        writer.writeheader()
        writer.writerows(data)

def export_to_csv(data, headers, path = '../export/transactions.csv'):
    write_csv_file(data, headers, path)

def save_category(category_dict, path = '../data/categories.json'):
    categories = read_json_file(path)
    categories.append(category_dict)
    write_json_file(categories, path)

def save_transaction(transaction_dict, path = '../data/transactions.json'):
    transactions = read_json_file(path)
    transactions.append(transaction_dict)
    write_json_file(transactions, path)

def load_categories(path = '../data/categories.json'):
    return read_json_file(path)

def load_transactions(path = '../data/transactions.json'):
    return read_json_file(path)

def load_data():
    categories = load_categories()
    transactions = load_transactions()

    return categories, transactions

def save_data(file_manager:FinanceManager):

    write_json_file(file_manager.category_list, '../data/categories.json')
    write_json_file(file_manager.transaction_list, '../data/transactions.json')