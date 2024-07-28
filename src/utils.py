import pandas as pd

def load_transactions(file_path):
    """Загружает транзакции из Excel файла"""
    df = pd.read_excel(file_path)
    df.rename(columns={
        'Дата операции': 'date',
        'Дата платежа': 'payment_date',
        'Номер карты': 'card_number',
        'Статус': 'status',
        'Сумма операции': 'amount',
        'Валюта операции': 'currency',
        'Сумма платежа': 'payment_amount',
        'Валюта платежа': 'payment_currency',
        'Кэшбэк': 'cashback',
        'Категория': 'category',
        'MCC': 'mcc',
        'Описание': 'description',
        'Бонусы (включая кэшбэк)': 'bonuses',
        'Округление на инвесткопилку': 'rounding',
        'Сумма операции с округлением': 'rounded_amount'
    }, inplace=True)

    # Вычисление potential_savings
    df['potential_savings'] = df[
                                  'amount'] * 0.05  # Предположим, что потенциальная экономия составляет 5% от суммы операции
    return df


def filter_transactions(df, **kwargs):
    """Фильтрация транзакций по различным критериям"""
    filtered_df = df.copy()
    for key, value in kwargs.items():
        filtered_df = filtered_df[filtered_df[key] == value]
    return filtered_df
