import json
import csv
import os

from week_17.classes.FinanceManager import FinanceManager

'''
Global Variables so the path is the same in every function
'''
environment = 'dev'
# environment = 'prod'

categories_json_path = f'week_17/data/{environment}/categories.json'
transactions_json_path = f'week_17/data/{environment}/transactions.json'
transactions_csv_path = f'week_17/export/{environment}/transactions.csv'

'''
Save data methods
'''
def save_category(category_dict, path = categories_json_path):
    categories = read_json_file(path)
    categories.append(category_dict)
    write_json_file(categories, path)

def save_transaction(transaction_dict, path = transactions_json_path):
    transactions = read_json_file(path)
    transactions.append(transaction_dict)
    write_json_file(transactions, path)

def save_data(file_manager:FinanceManager):

    write_json_file(file_manager.category_list, categories_json_path)
    write_json_file(file_manager.transaction_list, transactions_json_path)

'''
Load Data Methods
'''
def load_categories(path = categories_json_path):
    return read_json_file(path)

def load_transactions(path = transactions_json_path):
    return read_json_file(path)


'''
Export date to custom format Methods
'''
def export_to_csv(data, headers, path = transactions_csv_path):
    write_csv_file(path=path, data= data, headers = headers)


'''
Read/Write from/into file methods
'''
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
        os.makedirs(os.path.dirname(path), exist_ok=True)  # ✅ ensure folders exist
        json_string = json.dumps(dict_content, indent=4)
        with open(path, 'w') as file:
            file.write(json_string)
    except Exception as e:
        print(e)

def read_csv_file(path = transactions_csv_path):
    rows = []
    with open(path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
          rows.append(row)
    return rows


def write_csv_file(path, data, headers):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    print(path)
    with open(path, 'w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, headers)
        writer.writeheader()
        writer.writerows(data)