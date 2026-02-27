class cafe:
    def __init__(self):
        self.menuPos = {}
        self.ordersPos = {}

    def add_position(self, pos, prise, category, time):
        self.menuPos[pos] = {
            "Цена": prise,
            "Категория": category,
            "Время приготовления": time}

    def addOrder(self, table, status):
        priceForOrder = 0
        userOrder = []
        print(f"Доступное меню: {list(self.menuPos.keys())}")
        
        while True:
            pos = input("Введите название блюда: ")
            if pos in self.menuPos:
                kolvo = int(input("Введите кол-во товара: "))
                for _ in range(kolvo):
                    userOrder.append(pos)
                
                priceForOrder += (self.menuPos[pos]["Цена"] * kolvo)
                
                continueOrder = input("Продолжить заказ? (1 - да; 0 - нет): ")
                if continueOrder == "0":
                    break
            else:
                print("Такого блюда нет в меню")
        self.ordersPos[table] = {
            "заказы": userOrder,
            "статус": status
        }
        return f"Итого к оплате: {priceForOrder} руб."   

    def Popular(self):
      localOrder = []
      
      for info in self.ordersPos.values():
            localOrder.extend(info["заказы"])
      if not localOrder:
          return "Заказов еще не было."

    def category(self):
        prod = {}     
        for info in self.ordersPos.values():
            for dish in info["заказы"]:
                category = self.menuPos[dish]["Категория"]
                price = self.menuPos[dish]["Цена"]
                prod[category] = prod.get(category, 0) + price
        
        if not prod:
            print("Продаж пока не было.")
        else:
            for cat, total in prod.items():
                print(f"{cat}: {total} руб.")
        return prod

myCafe = cafe()

myCafe.add_position("Латте", 200, "Напитки", "10 минут")
myCafe.add_position("Круассан", 150, "Выпечка", "3 мин")
myCafe.add_position("Чизкейк", 300, "Десерты", "2 мин")

print(myCafe.addOrder(2, "В очереди"))

print(myCafe.Popular())
myCafe.category()
