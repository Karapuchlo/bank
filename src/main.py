from src.views import generate_main_page, generate_events_page
from src.services import get_top_cashback_categories, get_potential_savings
from src.reports import generate_category_expenses_report, generate_weekday_expenses_report
import os

if __name__ == '__main__':
    file_path = '../data/operations.xlsx'

    # Использование функций
    os.makedirs('reports', exist_ok=True)
    main_page_data = generate_main_page(file_path)
    events_page_data = generate_events_page(file_path, category='groceries')

    top_cashback_categories = get_top_cashback_categories(file_path)
    potential_savings = get_potential_savings(file_path)

    generate_category_expenses_report(file_path, '../reports/category_expenses.xlsx')
    generate_weekday_expenses_report(file_path, '../reports/weekday_expenses.xlsx')
