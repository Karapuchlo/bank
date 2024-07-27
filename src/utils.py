import pandas as pd

def load_transactions(file_path):
    """Загрузка данных о транзакциях из Excel-файла"""
    df = pd.read_excel(file_path)
    return df

def filter_transactions(df, **kwargs):
    """Фильтрация транзакций по различным критериям"""
    filtered_df = df.copy()
    for key, value in kwargs.items():
        filtered_df = filtered_df[filtered_df[key] == value]
    return filtered_df
