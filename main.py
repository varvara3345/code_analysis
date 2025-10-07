import os
from analyzer.code_parser import CodeAnalyzer


def read_code_from_file(filepath: str) -> str | None:
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
    file_to_analyze = 'samples/bad_code.py'

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
        analyzer.analyze_ml_optimizations(ast_tree)
        analyzer.analyze_pep8_compliance(code_content)

    all_recommendations = analyzer.get_recommendations()

    print("\n--- Отчет об анализе кода ---")
    if all_recommendations:
        all_recommendations.sort(key=lambda x: (x.get('type', ''), x.get('line', 0)))

        for rec in all_recommendations:
            print(f"Тип: {rec.get('type', 'Общее')}")
            print(f"Строка: {rec.get('line', 'N/A')}")
            print(f"Сообщение: {rec.get('message', 'Нет сообщения')}")
            if rec.get('code_snippet'):
                print("Сниппет кода:")
                for line in rec['code_snippet'].splitlines():
                    print(f"    | {line}")
            print("-" * 30)
    else:
        print("значительных проблем или предложений по оптимизации не найдено.")


if __name__ == "__main__":
    main()