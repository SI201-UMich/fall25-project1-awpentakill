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