import re

pattern = r'^\d{12}$'

while True:
  try:
    inn = int(input())
  except ValueError:
    print("Вы ввели неверный тип данных.")
  except Exception as e:
    print("Другая ошибка")
  else:
    innStr = str(inn)
    if len(innStr) == 12:

      print("ИНН принят: ", inn)
      break
    else:
      print("Необходимо 12 чисел")
  finally:
    pass
