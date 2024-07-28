from openpyxl import Workbook
from datetime import datetime
from utils import load_transactions
import pandas as pd

def generate_weekday_expenses_report(file_path, output_file):
    """Формирование отчета "Траты по дням недели"""
    df = load_transactions(file_path)
    df['date'] = pd.to_datetime(df['date'], format='%d.%m.%Y %H:%M:%S')
    df['weekday'] = df['date'].dt.day_name()
    pivot_table = df.pivot_table(index='weekday', values=['amount', 'potential_savings'], aggfunc='sum')
    wb = Workbook()
    ws = wb.active
    ws.append(['Weekday', 'Total Expenses', 'Potential Savings'])
    for weekday, row in pivot_table.iterrows():
        ws.append([weekday, row['amount'], row['potential_savings']])
    wb.save(output_file)

def generate_category_expenses_report(file_path, output_file):
    """Формирование отчета "Траты по категориям"""
    df = load_transactions(file_path)
    pivot_table = df.pivot_table(index='category', values=['amount', 'potential_savings'], aggfunc='sum')
    wb = Workbook()
    ws = wb.active
    ws.append(['Category', 'Total Expenses', 'Potential Savings'])
    for category, row in pivot_table.iterrows():
        ws.append([category, row['amount'], row['potential_savings']])
    wb.save(output_file)
