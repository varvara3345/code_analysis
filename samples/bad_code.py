# samples/bad_code.py

import pandas as pd
import numpy # для теста ML Optimization

def process_data(data_list):
    """
    Пример функции с неэффективным циклом.
    Нарушение PEP8: Слишком много пробелов после скобки.
    """
    new_list = [ ] # Нарушение PEP8 здесь
    for item in data_list:
        if item > 10:
            new_list.append(item * 2) # Неэффективный append
    return new_list

def calculate_average(numbers):
    total = 0
    # Этот цикл тоже может быть оптимизирован sum()
    for num in numbers:
        total += num
    return total / len(numbers)

# Еще один пример для анализа
my_numbers = [1, 5, 12, 8, 15, 3]
processed_numbers = process_data(my_numbers)
print(processed_numbers)

# Длинная строка, которая может нарушать PEP8
long_variable_name_to_demonstrate_pep8_violation_for_line_length = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 + 13 + 14 + 15 + 16 + 17 + 18 + 19 + 20 + 21 + 22 + 23 + 24 + 25 + 26 + 27 + 28 + 29 + 30

# Пример использования ML-фреймворка
def train_model(X, y):
    from sklearn.linear_model import LogisticRegression
    model = LogisticRegression()
    model.fit(X, y)
    return model