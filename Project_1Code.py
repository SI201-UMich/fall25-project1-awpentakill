# =========================================================
# SI 201: Project 1 — Data Analysis (Sample Superstore)
# Name: Qingyang Lan
# Student ID: 3407 1696
# Email: qylan@umich.edu
# Collaborators: Adam Weng, Yufan Xu
# Calculation I:Qingyang Lan Calculation II: Adam Weng Calculation III: Yufan Xu
# Main coding: Qingyang Lan, Adam Weng Diagram: Yufan Xu
# GenAI Usage: Asked ChatGPT to help debug, format.
# =========================================================

import csv
import unittest


# ---------------------------------------------------------
# Part 1: Read CSV file into list of dictionaries
# ---------------------------------------------------------
def read_csv_to_dict(filename):
    data = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data


# ---------------------------------------------------------
# Part 2: Write dictionary results to a CSV file
# ---------------------------------------------------------
def write_dict_to_csv(filename, result_dict, headers):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        for key, value in result_dict.items():
            if isinstance(key, tuple):
                row = list(key)
            else:
                row = [key]

            if isinstance(value, (list, tuple)):
                for v in value:
                    row.append(v)
            else:
                row.append(value)

            writer.writerow(row)


# =========================================================
# Calculations I
# =========================================================

def calculate_avg_profit_by_subcategory_region(data):
    total_profit = {}
    count = {}

    for row in data:
        subcat = row['Sub-Category']
        region = row['Region']
        profit = float(row['Profit'])
        key = (subcat, region)

        if key not in total_profit:
            total_profit[key] = 0
            count[key] = 0
        total_profit[key] += profit
        count[key] += 1

    avg_profit = {}
    for key in total_profit:
        avg_profit[key] = total_profit[key] / count[key]
    print(f'Average profit by subcategory and region: {avg_profit}')
    return avg_profit


def calculate_total_sales_by_region_segment(data):
    sales_by_group = {}

    for row in data:
        region = row['Region']
        segment = row['Segment']
        sales = float(row['Sales'])
        key = (region, segment)

        if key not in sales_by_group:
            sales_by_group[key] = 0
        sales_by_group[key] += sales
    print(f'Total sales by region and segment: {sales_by_group}')
    return sales_by_group


# =========================================================
# Calculations II
# =========================================================

def calculate_profit_ratio_by_discount_region(data):
    ratios = {}

    for row in data:
        region = row['Region']
        discount = float(row['Discount'])
        sales = float(row['Sales'])
        profit = float(row['Profit'])

        if sales == 0:
            continue

        ratio = profit / sales

        if region not in ratios:
            ratios[region] = {'low': [], 'high': []}

        if discount > 0.2:
            ratios[region]['high'].append(ratio)
        else:
            ratios[region]['low'].append(ratio)

    result = {}
    for region in ratios:
        low_list = ratios[region]['low']
        high_list = ratios[region]['high']

        low_avg = sum(low_list) / len(low_list) if len(low_list) > 0 else 0
        high_avg = sum(high_list) / len(high_list) if len(high_list) > 0 else 0

        result[region] = (low_avg, high_avg)
    print(f'Low and high profit ratios by region: {result}')
    return result


def calculate_profit_margin_by_shipmode_category(data):
    margin_sum = {}
    count = {}

    for row in data:
        ship_mode = row['Ship Mode']
        category = row['Category']
        sales = float(row['Sales'])
        profit = float(row['Profit'])

        if sales == 0:
            continue

        margin = profit / sales
        key = (ship_mode, category)

        if key not in margin_sum:
            margin_sum[key] = 0
            count[key] = 0

        margin_sum[key] += margin
        count[key] += 1

    avg_margin = {}
    for key in margin_sum:
        avg_margin[key] = margin_sum[key] / count[key]
    print(f'Average profit margin by ship mode and category: {avg_margin}')
    return avg_margin
