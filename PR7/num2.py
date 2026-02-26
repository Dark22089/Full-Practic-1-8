import re

text = """
Посетите наши страницы:
Email: info@example.com (главный), support-team@corp.net (поддержка)
Дата: 25-05-2023, 01/01/2024, 12.02.2025.
Коды товаров: ID_PROD-1001, ITEM-20-A, ID-300-B.
Суммы: $150.50, 20 EUR, 500 RUB, £75.
"""
p = []

pattern = r'ID_PROD-\d{4}'
pattern1 = r'\d{4}'
text1 = '' 
for elem in re.findall(pattern, text): 
  text1 += elem
p.extend(re.findall(pattern1, text1))

pattern = r'ID-\d{3}'
pattern2 = r'\d{3}'
text2 = '' 
for elem in re.findall(pattern, text): 
  text2 += elem
p.extend(re.findall(pattern2, text2))

print(p)
