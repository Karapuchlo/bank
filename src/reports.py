import pandas as pd
from openpyxl import Workbook
from src.utils import load_transactions

def generate_category_expenses_report(file_path, output_file):
    """Формирование отчета "Траты по категориям"""
    df = load_transactions(file_path)
    pivot_table = df.pivot_table(index='category', values='amount', aggfunc='sum')
    wb = Workbook()
    ws = wb.active
    ws.append(['Category', 'Total Expenses'])
    for category, total in pivot_table.items():
        ws.append([category, total])
    wb.save(output_file)

def generate_weekday_expenses_report(file_path, output_file):
    """Формирование отчета "Траты по дням недели"""
    df = load_transactions(file_path)
    df['weekday'] = df['date'].dt.day_name()
    pivot_table = df.pivot_table(index='weekday', values='amount', aggfunc='sum')
    wb = Workbook()
    ws = wb.active
    ws.append(['Weekday', 'Total Expenses'])
    for weekday, total in pivot_table.items():
        ws.append([weekday, total])
    wb.save(output_file)
