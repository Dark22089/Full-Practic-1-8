def num1(a, b, oper):
  if oper == "+":
    return(a + b)
  elif oper == "-":
    return(a - b)
  elif oper == "*":
    return(a * b)
  elif oper == "/":
    return(a / b)
  elif oper == "//":
    return(a // b)
  elif oper == "**":
    return(a ** b)
  else:
    return "Неверныё оператор"
a = int(input())
b = int(input())
oper = input()

print(num1(a, b, oper))
