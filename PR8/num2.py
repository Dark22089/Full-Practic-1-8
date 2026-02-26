while True:
  try:
    prise = float(input())
  except ValueError:
    print("Вы ввели неверный тип данных.")
  except Exception as e:
    print("Другая ошибка")
  else:
    if prise >= 0 and prise <= 1000000:
      print("Цена указана верно")
      break
    else:
      print("Неверное число") 
