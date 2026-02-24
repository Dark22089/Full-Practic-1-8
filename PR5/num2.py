import random

def newPas(useNum, useLow, useHigh, useSpec):
    pull = ""

    if useNum == 1: pull = pull + "0123456789"
    if useLow == 1: pull = pull + "abcdefghijklmnopqrstuvwxyz"
    if useHigh == 1: pull = pull + "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if useSpec == 1: pull = pull +"!@#$%^&}*()-_=+[];:,.<>/?|{~`"
    lenPull = len(pull)
    Pasword = ""

    if lenPull != 0:
        for i in range(1, lenPas + 1):
            Pasword = Pasword + pull[random.randint(0, lenPull - 1)]
        return Pasword
    else:
        return "Возможные символы генерации отсутствуют"

# pull

lenPas = int(input("Введите кол-во символов"))

useNum = int(input("В пароле нужны цифры? (1 - да, 0 - нет)"))
while useNum != 0 and useNum != 1:
  useNum = int(input("В пароле нужны цифры? (1 - да, 0 - нет)"))

useLow = int(input("В пароле нужны строчные буквы? (1 - да, 0 - нет)"))
while useLow != 0 and useLow != 1:
  useLow = int(input("В пароле нужны строчные буквы? (1 - да, 0 - нет)"))

useHigh = int(input("В пароле нужны заглавные буквы? (1 - да, 0 - нет)"))
while useHigh != 0 and useHigh != 1:
  useHigh = int(input("В пароле нужны заглавные буквы? (1 - да, 0 - нет)"))

useSpec = int(input("В пароле нужны спецсимволы? (1 - да, 0 - нет)"))
while useSpec != 0 and useSpec != 1:
  useSpec = int(input("В пароле нужны спецсимволы? (1 - да, 0 - нет)"))

# generate

kolvo = int(input("Выберите количество генераций"))
while kolvo <= 0:
    kolvo = int(input("Выберите количество генераций"))

for i in range(1, kolvo + 1):
    print(newPas(useNum, useLow, useHigh, useSpec))
