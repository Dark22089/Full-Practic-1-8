class cafe:   # Доделать
    def __init__(self):
        self.menuPos = {}
        self.ordersPos = {}
    def add_position(self, pos, prise, category, time):
        self.menuPos[pos] = {
            "Цена": prise,
            "Категория": category,
            "Время приготовления": time}
    def addOrder(self, table, status):
        priseForOrder = 0
        userOrder = []
        print(self.menuPos.keys())
        while True:
            pos = input("Введите название блюда: ")
            if pos in self.menuPos:
              userOrder.append(pos)
              
              kolvo = int(input("Введите кол-во товара: "))

              priseForOrder += (self.menuPos[pos]["Цена"] * kolvo)
              self.ordersPos[table] = {
                  "заказы": userOrder,
                  "статус": status
              }

              continueOrder = int(input("Продолжить заказ? (1 - да; 0 - нет)"))
              while continueOrder != 0 and continueOrder != 1:
                  continueOrder = int(input("Продолжить заказ? (1 - да; 0 - нет)"))
              
              if continueOrder == 0:
                  break
            else:
              print("Такого блюда нет в меню")
        return priseForOrder
    def Popular(self):
      localOrder = []
      
      for info in self.ordersPos.values():
            localOrder.extend(info["заказы"])

      if not localOrder:
          return "Заказов еще не было."

      print(localOrder)
    def category(self):
       Prod = {}     
       for info in self.ordersPos.values():
            for newKey in info["заказы"]:
                category = self.menuPos[newKey]["Категория"]
                price = self.menuPos[newKey]["Цена"]
                Prod[cat] = Prod.get(cat, 0) + price
                
                if category in Prod:
                    Prod[category] += price
                else:
                    Prod[category] = price
       if not Prod:
            print("Продаж пока не было.")
       else:
            for cat, total in Prod.items():
                print(f"{cat}: {total} руб.")
        
       return Prod

myCafe = cafe()

myCafe.add_position("Латте", 200, "Напитки", "10 минут")
myCafe.add_position("Круассан", 150, "Выпечка", "3 мин")
myCafe.add_position("Чизкейк", 300, "Десерты", "2 мин")

print(myCafe.addOrder(2, "В очереди"))

print(myCafe.Popular())
