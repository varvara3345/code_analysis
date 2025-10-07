import pandas as pd
import numpy

def process_data(data_list):
    new_list = [ ]
    for item in data_list:
        if item > 10:
            new_list.append(item * 2)
    return new_list

def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)

my_numbers = [1, 5, 12, 8, 15, 3]
processed_numbers = process_data(my_numbers)
print(processed_numbers)

long_variable_name_to_demonstrate_pep8_violation_for_line_length = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 + 13 + 14 + 15 + 16 + 17 + 18 + 19 + 20 + 21 + 22 + 23 + 24 + 25 + 26 + 27 + 28 + 29 + 30

def train_model(X, y):
    from sklearn.linear_model import LogisticRegression
    model = LogisticRegression()
    model.fit(X, y)
    return model