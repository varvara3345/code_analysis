# analyzer/code_parser.py

import astroid
import autopep8 # Добавляем для проверки PEP8

class CodeAnalyzer: # <-- Здесь начинается ОДНО определение класса
    def __init__(self):
        self.recommendations = []

    def parse_code_to_ast(self, code_content: str):
        """
        Парсит строковое представление кода в AST-дерево.
        """
        try:
            return astroid.parse(code_content)
        except Exception as e:
            self.recommendations.append(f"Ошибка парсинга кода: {e}")
            return None

    def analyze_inefficient_loops(self, ast_tree): # <-- Этот метод должен быть здесь
        """
        Анализирует AST-дерево на предмет неэффективных циклов.
        Ищет циклы 'for' с потенциально медленными операциями,
        такими как .append() внутри цикла для создания списка.
        Предлагает использовать list comprehension.
        """
        for node in ast_tree.nodes_of_class(astroid.For):  # Ищем все узлы типа For
            found_append = False
            for sub_node in node.body:  # Проходим по прямым потомкам цикла
                # Мы ищем Call узлы, где функция является атрибутом (напр. list.append)
                for call_node in sub_node.nodes_of_class(astroid.Call):
                    if isinstance(call_node.func, astroid.Attribute) and call_node.func.attrname == 'append':
                        self.recommendations.append({
                            "type": "Performance",
                            "line": node.lineno,
                            "message": (
                                f"Строка {node.lineno}: Обнаружен цикл `for` с `list.append()`. "
                                "Рассмотрите возможность использования `list comprehension` для улучшения "
                                "производительности и читаемости. Пример: `[expr for item in iterable if condition]`."
                            ),
                            "code_snippet": node.as_string(),  # Показываем сам код цикла
                        })
                        found_append = True
                        break  # Нашли append, больше в этом sub_node не ищем
                if found_append:
                    break  # Если нашли append в этом цикле, переходим к следующему For-циклу

    def analyze_pep8_compliance(self, code_content: str): # <-- Этот метод тоже должен быть здесь
        """
        Анализирует код на соответствие PEP8, используя autopep8.
        """
        fixed_code = autopep8.fix_code(code_content, options={'aggressive': 0})
        if fixed_code != code_content:
            self.recommendations.append({
                "type": "Style/Readability",
                "line": "N/A",  # autopep8 не всегда дает точную строку для всех ошибок
                "message": (
                    "Обнаружены нарушения стиля PEP8. Используйте `autopep8` или "
                    "инструменты форматирования (вроде Black) для автоматического исправления. "
                    "Это улучшит читаемость кода."
                ),
                "code_snippet": "Смотрите полный файл для деталей",
            })

    def analyze_ml_optimizations(self, ast_tree): # <-- И этот метод тоже
        """
        Анализирует AST-дерево на предмет потенциальных ML-оптимизаций.
        (Это будет зависеть от нашей LLM, пока просто заглушка)
        """
        for node in ast_tree.body:
            if isinstance(node, astroid.Import) or isinstance(node, astroid.ImportFrom):
                for name_node in node.names:
                    if name_node[0] in ['torch', 'tensorflow', 'keras', 'sklearn', 'numpy', 'pandas']:
                        self.recommendations.append({
                            "type": "ML Optimization",
                            "line": node.lineno,
                            "message": (
                                f"Строка {node.lineno}: Обнаружено использование библиотеки `{name_node[0]}`. "
                                "Для больших моделей или деплоя рассмотрите оптимизации, такие как "
                                "квантование (quantization), дистилляция (distillation) или "
                                "прунинг (pruning), чтобы улучшить производительность и уменьшить размер модели."
                            ),
                            "code_snippet": node.as_string(),
                        })

    def get_recommendations(self): # <-- И этот
        return self.recommendations

    def clear_recommendations(self): # <-- И этот
        self.recommendations = []