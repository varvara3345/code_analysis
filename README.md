# AI-Powered Code Reviewer (ML Focus)

![Python Logo](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)

## Описание

Инструмент для статического анализа Python-кода, ориентированный на ML-приложения. Автоматически выявляет потенциальные проблемы в коде и предлагает улучшения по:
*   **Производительности:** Оптимизация циклов (`list comprehension`).
*   **Читаемости/Стилю:** Соответствие стандартам PEP8.
*   **ML-оптимизациям:** Общие рекомендации для ML-библиотек (квантование, дистилляция).

## Основные Возможности

*   Разбор кода в Абстрактное Синтаксическое Дерево (AST).
*   Поиск неэффективных `for`-циклов с `list.append()`.
*   Проверка базовых нарушений стиля PEP8.
*   Идентификация ML-библиотек (`pandas`, `numpy`, `scikit-learn` и др.) с предложениями по оптимизации.
*   Детальный вывод рекомендаций с номером строки и фрагментом кода.

## Установка и Запуск

```bash
# 1. Клонировать репозиторий
git clone https://github.com/varvara3345/code_analysis.git
cd code_analysis

# 2. Создать и активировать виртуальное окружение
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate

# 3. Установить зависимости
pip install astroid autopep8 transformers torch pandas numpy

# 4. Запустить анализатор
python main.py