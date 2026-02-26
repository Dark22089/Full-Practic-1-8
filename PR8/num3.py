while True:
  try:
    pas = input("Give your password: ")
  except ValueError:
    print("Вы ввели неверный тип данных.")
  except Exception as e:
    print("Другая ошибка")
  else:
    if len(pas) >= 8 and len(pas) <= 20:
      low = 0
      up = 0
      num = 0
      spec = 0
      
      for i in range(0, len(pas)):
        if pas[i].isdigit():
          num += 1
        elif pas[i].isupper():
          up += 1
        elif pas[i].islower():
          low += 1
        else:
          spec += 1
      if up > 0 and num > 0:
        print("Пароль принят")
        break
      else:
        print("Пароль должен содержаать хотя бы 1 цифру и заглавную букву")
    else:
      print("Пароль должен содержать от 8 до 20 символов")
