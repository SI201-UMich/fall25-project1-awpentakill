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


# =========================================================
# Calculations III
# =========================================================

def calculate_avg_order_value_by_segment_shipmode(data):
    total_value = {}
    count = {}

    for row in data:
        segment = row['Segment']
        ship_mode = row['Ship Mode']
        qty = float(row['Quantity'])
        sales = float(row['Sales'])
        key = (segment, ship_mode)

        if qty == 0:
            continue

        avg_value = sales / qty

        if key not in total_value:
            total_value[key] = 0
            count[key] = 0

        total_value[key] += avg_value
        count[key] += 1

    avg_order_value = {}
    for key in total_value:
        avg_order_value[key] = total_value[key] / count[key]
    print(f'Average order value by segment and ship mode: {avg_order_value}')
    return avg_order_value


def get_top3_cities_by_profit_in_category(data):
    category_city_profit = {}

    for row in data:
        category = row['Category']
        city = row['City']
        profit = float(row['Profit'])

        if category not in category_city_profit:
            category_city_profit[category] = {}

        if city not in category_city_profit[category]:
            category_city_profit[category][city] = 0

        category_city_profit[category][city] += profit

    result = {}
    for category, city_dict in category_city_profit.items():
        sorted_cities = sorted(city_dict.items(), key=lambda x: x[1], reverse=True)
        top3 = sorted_cities[:3]
        result[category] = top3
    print(f'Top 3 cities by profit in category: {result}')
    return result


# =========================================================
# Main Function
# =========================================================
def main():
    filename = "SampleSuperstore.csv"
    data = read_csv_to_dict(filename)

    avg_profit = calculate_avg_profit_by_subcategory_region(data)
    total_sales = calculate_total_sales_by_region_segment(data)
    profit_discount = calculate_profit_ratio_by_discount_region(data)
    profit_margin = calculate_profit_margin_by_shipmode_category(data)
    avg_order_value = calculate_avg_order_value_by_segment_shipmode(data)
    top3_cities = get_top3_cities_by_profit_in_category(data)

    print("Calculations complete!")
    print("Top 3 cities by profit (example):", top3_cities)

   ''' write_dict_to_csv("avg_profit_by_subcategory_region.csv", avg_profit,
                      ["Sub-Category", "Region", "Average Profit"])
    write_dict_to_csv("total_sales_by_region_segment.csv", total_sales,
                      ["Region", "Segment", "Total Sales"])
    write_dict_to_csv("profit_ratio_by_discount_region.csv", profit_discount,
                      ["Region", "Low Discount Ratio", "High Discount Ratio"])
    write_dict_to_csv("profit_margin_by_shipmode_category.csv", profit_margin,
                      ["Ship Mode", "Category", "Average Margin"])
    write_dict_to_csv("avg_order_value_by_segment_shipmode.csv", avg_order_value,
                      ["Segment", "Ship Mode", "Avg Order Value"])
    write_dict_to_csv("top3_cities_by_profit_in_category.csv", top3_cities,
                      ["Category", "City1", "Profit1", "City2", "Profit2", "City3", "Profit3"])
'''
# =========================================================
# Test Case
# =========================================================

def test_avg_profit_by_subcategory_region():
    print("\nRunning test_avg_profit_by_subcategory_region...")
    # General Case 1
    data = [
        {'Sub-Category': 'Phones', 'Region': 'East', 'Profit': '100'},
        {'Sub-Category': 'Phones', 'Region': 'East', 'Profit': '300'}
    ]
    result = calculate_avg_profit_by_subcategory_region(data)
    assert abs(result[('Phones', 'East')] - 200.0) < 0.001

    # General Case 2
    data.append({'Sub-Category': 'Chairs', 'Region': 'West', 'Profit': '400'})
    result = calculate_avg_profit_by_subcategory_region(data)
    assert ('Chairs', 'West') in result

    # Edge Case 1: Zero profit
    data = [{'Sub-Category': 'Phones', 'Region': 'East', 'Profit': '0'}]
    result = calculate_avg_profit_by_subcategory_region(data)
    assert result[('Phones', 'East')] == 0.0

    # Edge Case 2: Empty list
    data = []
    result = calculate_avg_profit_by_subcategory_region(data)
    assert result == {}
#----------------------------------------------------------------------
def test_profit_ratio_by_discount_region():
    print("\nRunning test_profit_ratio_by_discount_region...")
    # General Case 1
    data = [
        {'Discount': '0.1', 'Profit': '100', 'Sales': '1000', 'Region': 'East'},
        {'Discount': '0.3', 'Profit': '20', 'Sales': '500', 'Region': 'East'}
    ]
    result = calculate_profit_ratio_by_discount_region(data)
    assert 'East' in result

    # General Case 2
    low_ratio, high_ratio = result['East']
    assert low_ratio >= high_ratio, f"Expected low discount ratio ≥ high discount ratio, got {low_ratio}, {high_ratio}"

    # Edge Case 1: Zero sales
    data = [{'Discount': '0.2', 'Profit': '100', 'Sales': '0', 'Region': 'West'}]
    result = calculate_profit_ratio_by_discount_region(data)
    assert result == {}

    # Edge Case 2: Empty list
    data = []
    result = calculate_profit_ratio_by_discount_region(data)
    assert result == {}
#----------------------------------------------------------------------
def test_avg_order_value_by_segment_shipmode():
    print("\nRunning test_avg_order_value_by_segment_shipmode...")
    # General Case 1
    data = [
        {'Segment': 'Consumer', 'Ship Mode': 'Standard Class', 'Sales': '200', 'Quantity': '1'},
        {'Segment': 'Consumer', 'Ship Mode': 'Standard Class', 'Sales': '100', 'Quantity': '1'}
    ]
    result = calculate_avg_order_value_by_segment_shipmode(data)
    assert ('Consumer', 'Standard Class') in result

    # General Case 2
    val = result[('Consumer', 'Standard Class')]
    assert abs(val - 150.0) < 0.001  # average order value should be 150 ✅

    # Edge Case 1: Zero quantity
    data = [{'Segment': 'Consumer', 'Ship Mode': 'Standard Class', 'Sales': '100', 'Quantity': '0'}]
    result = calculate_avg_order_value_by_segment_shipmode(data)
    assert result == {}

    # Edge Case 2: Empty data
    result = calculate_avg_order_value_by_segment_shipmode([])
    assert result == {}

#----------------------------------------------------------------------
def test_get_top3_cities_by_profit_in_category():
    print("\nRunning test_get_top3_cities_by_profit_in_category...")
    # General Case 1
    data = [
        {'City': 'New York', 'Profit': '500', 'Category': 'Furniture'},
        {'City': 'Los Angeles', 'Profit': '400', 'Category': 'Furniture'},
        {'City': 'Seattle', 'Profit': '300', 'Category': 'Furniture'}
    ]
    result = get_top3_cities_by_profit_in_category(data)
    assert 'Furniture' in result
    assert len(result['Furniture']) == 3

    # General Case 2
    top_city = result['Furniture'][0][0]
    assert top_city == 'New York'

    # Edge Case 1: Fewer than 3 cities
    data = [
        {'City': 'Detroit', 'Profit': '200', 'Category': 'Office Supplies'},
        {'City': 'Chicago', 'Profit': '100', 'Category': 'Office Supplies'}
    ]
    result = get_top3_cities_by_profit_in_category(data)
    assert len(result['Office Supplies']) <= 3

    # Edge Case 2: Empty list
    data = []
    result = get_top3_cities_by_profit_in_category(data)
    assert result == {}

# =========================================================
# Run program
# =========================================================
if __name__ == "__main__":
    main()

    print("\n====================")
    print("Running Test Cases...")
    print("====================")
    test_avg_profit_by_subcategory_region()
    test_profit_ratio_by_discount_region()
    test_avg_order_value_by_segment_shipmode()
    test_get_top3_cities_by_profit_in_category()
    print("All tests completed successfully!")