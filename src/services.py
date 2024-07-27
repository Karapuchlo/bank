from .utils import load_transactions, filter_transactions

def get_top_cashback_categories(file_path, top_n=5):
    """Получение top N категорий с наибольшим кешбэком"""
    df = load_transactions(file_path)
    df['cashback'] = df['amount'] * df['cashback_rate']
    top_categories = df.groupby('category')['cashback'].sum().nlargest(top_n).index.tolist()
    return top_categories

def get_potential_savings(file_path):
    """Анализ транзакций для выявления возможных сбережений"""
    df = load_transactions(file_path)
    # Логика для выявления потенциальных сбережений
    return potential_savings
