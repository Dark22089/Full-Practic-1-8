import re

text = """
Посетите наши страницы:
Email: info@example.com (главный), support-team@corp.net (поддержка)
Дата: 25-05-2023, 01/01/2024, 12.02.2025.
Коды товаров: ID_PROD-1001, ITEM-20-A, ID-300-B.
Суммы: $150.50, 20 EUR, 500 RUB, £75.
"""
spec = [r"\.", r"\-", r"\/"]
p = []
for i in range(0, 3):
    pattern = rf'\b\d{{2}}{spec[i]}\d{{2}}{spec[i]}\d{{4}}\b'
    p.extend(re.findall(pattern, text))
end = []
for elem in p:
  elem = str(elem[6] + elem[7] + elem[8] + elem[9] + "-" + elem[3] + elem[4] + "-" + elem[0] + elem[1])
  end.append(elem)
print(end)
