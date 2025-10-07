# main.py

import os
from analyzer.code_parser import CodeAnalyzer


# Мы пока не интегрируем LLM, но подготовим место для нее
# from llm_integration import get_llm_suggestions # Будет в следующем шаге

def read_code_from_file(filepath: str) -> str | None:
    """
    Вспомогательная функция для чтения содержимого файла.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Ошибка: Файл '{filepath}' не найден.")
        return None
    except Exception as e:
        print(f"Ошибка при чтении файла '{filepath}': {e}")
        return None


def main():
    """
    Главная функция для запуска анализатора и вывода результатов.
    """
    file_to_analyze = 'samples/bad_code.py'

    # Убедимся, что файл существует
    if not os.path.exists(file_to_analyze):
        print(f"Файл для анализа не найден: {file_to_analyze}. Пожалуйста, создайте его.")
        return

    print(f"--- Запуск AI-Powered Code Reviewer ---")
    print(f"Анализ файла: {file_to_analyze}\n")

    code_content = read_code_from_file(file_to_analyze)
    if not code_content:
        return

    analyzer = CodeAnalyzer()
    ast_tree = analyzer.parse_code_to_ast(code_content)

    if ast_tree:
        print("Проводим статический анализ кода:")
        analyzer.analyze_inefficient_loops(ast_tree)
        analyzer.analyze_ml_optimizations(ast_tree)  # Добавляем вызов нового анализатора

        # Анализ PEP8 требует строкового представления кода, а не AST
        analyzer.analyze_pep8_compliance(code_content)

        # В будущем здесь будет интеграция с LLM
    # if ast_tree:
    #     llm_suggestions = get_llm_suggestions(code_content, ast_tree)
    #     analyzer.recommendations.extend(llm_suggestions)

    all_recommendations = analyzer.get_recommendations()

    print("\n--- Отчет об анализе кода ---")
    if all_recommendations:
        # Сортируем рекомендации по типу и потом по строке
        all_recommendations.sort(key=lambda x: (x.get('type', ''), x.get('line', 0)))

        for rec in all_recommendations:
            print(f"Тип: {rec.get('type', 'Общее')}")
            print(f"Строка: {rec.get('line', 'N/A')}")
            print(f"Сообщение: {rec.get('message', 'Нет сообщения')}")
            if rec.get('code_snippet'):
                # Выводим сниппет кода, если он есть
                print("Сниппет кода:")
                for line in rec['code_snippet'].splitlines():
                    print(f"    | {line}")  # Для лучшей читаемости
            print("-" * 30)
    else:
        print("🚀 Отличная работа! Значительных проблем или предложений по оптимизации не найдено.")


if __name__ == "__main__":
    main()