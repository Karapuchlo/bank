from src.utils import load_transactions, filter_transactions

def get_top_cashback_categories(file_path, top_n=5):
    """Получение top N категорий с наибольшим кешбэком"""
    df = load_transactions(file_path)
    df['cashback'] = df['amount'] * df['cashback']
    top_categories = df.groupby('category')['cashback'].sum().nlargest(top_n).index.tolist()
    return top_categories

def get_potential_savings(file_path):
    """Вычисляет потенциальную экономию"""
    df = load_transactions(file_path)
    potential_savings = df['amount'] * 0.05  # Предположим, что потенциальная экономия составляет 5% от суммы операции
    return potential_savings

