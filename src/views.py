import json
from src.utils import load_transactions, filter_transactions

def generate_main_page(file_path):
    """Формирование данных для главной страницы"""
    df = load_transactions(file_path)
    data = df.to_dict('records')
    return json.dumps(data)

def generate_events_page(file_path, **filters):
    """Формирование данных для страницы "События"""
    df = load_transactions(file_path)
    if filters:
        df = filter_transactions(df, **filters)
    data = df.to_dict('records')
    return json.dumps(data)
