import re

pattern = r"\w+@\w+.\w+"
text = """
Посетите наши страницы:
Email: info@example.com (главный), support-team@corp.net (поддержка)
Дата: 25-05-2023, 01/01/2024, 12.02.2025.
Коды товаров: ID_PROD-1001, ITEM-20-A, ID-300-B.
Суммы: $150.50, 20 EUR, 500 RUB, £75.
"""
re.findall(pattern, text)
