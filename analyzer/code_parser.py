import astroid
import autopep8

class CodeAnalyzer:
    def __init__(self):
        self.recommendations = []

    def parse_code_to_ast(self, code_content: str):
        try:
            return astroid.parse(code_content)
        except Exception as e:
            self.recommendations.append(f"Ошибка парсинга кода: {e}")
            return None

    def analyze_inefficient_loops(self, ast_tree):
        for node in ast_tree.nodes_of_class(astroid.For):
            found_append = False
            for sub_node in node.body:
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
                            "code_snippet": node.as_string(),
                        })
                        found_append = True
                        break
                if found_append:
                    break

    def analyze_pep8_compliance(self, code_content: str):
        fixed_code = autopep8.fix_code(code_content, options={'aggressive': 0})
        if fixed_code != code_content:
            self.recommendations.append({
                "type": "Style/Readability",
                "line": "N/A",
                "message": (
                    "Обнаружены нарушения стиля PEP8. Используйте `autopep8` или "
                    "инструменты форматирования (вроде Black) для автоматического исправления. "
                    "Это улучшит читаемость кода."
                ),
                "code_snippet": "Смотрите полный файл для деталей",
            })

    def analyze_ml_optimizations(self, ast_tree):
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

    def get_recommendations(self):
        return self.recommendations

    def clear_recommendations(self):
        self.recommendations = []