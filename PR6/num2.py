class Student:
    def __init__(self):
        self.students = {}
        self.grades = {}

    def add(self, id, name, group, contact):
        self.students[id] = {
            "ФИО": name,
            "Группа": group,
            "Контакты": contact
        }
        self.grades[id] = [] 
        print(f"Студент {name} успешно добавлен.")

    def grade(self, id, subject, grade, date):
        if id in self.students:
            new_grade = {
                "Предмет": subject,
                "Оценка": grade,
                "Дата": date
            }
            self.grades[id].append(new_grade)
            print(f"Оценка {grade} по предмету '{subject}' добавлена студенту {self.students[id]['ФИО']}.")
        else:
            print("Ошибка: Студент с таким ID не найден.")

    def store(self, id):
        if id not in self.grades or not self.grades[id]:
            return 0.0
        
        allScores = [item["Оценка"] for item in self.grades[id]]
        return sum(allScores) / len(allScores)

    def find(self, threshold):
        print(f"Студенты с оценками ниже {threshold}")
        found = False
        for id, gratlist in self.grades.items():
            low = [g["Оценка"] for g in gratlist if g["Оценка"] < threshold]
            if low:
                name = self.students[id]["ФИО"]
                print(f"Студент: {name} (ID: {id}) имеет оценки: {low}")
                found = True
        if not found:
            print("Таких студентов нет.")

    def rait(self):
        rlist = []
        for id in self.students:
            avg = self.store(id)
            rlist.append({
                "Имя": self.students[id]["ФИО"],
                "Средний балл": avg
            })
        
        rlist.sort(key=lambda x: x["Средний балл"], reverse=True)
        
        print("\nРейтинг студентов")
        for i, student in enumerate(rlist, 1):
            print(f"{i}. {student['Имя']} — {student['Средний балл']:.2f}")


st = Student()

# 1
st.add(101, "Иван Иванов", "БПИ-23", "ivan@mail.ru")
st.add(102, "Анна Петрова", "БПИ-23", "anna@mail.ru")
st.add(103, "Сергей Сидоров", "ЭКО-22", "serg@mail.ru")

# 2
st.grade(101, "Программирование", 5, "20.10.2023")
st.grade(101, "Математика", 4, "21.10.2023")
st.grade(102, "Программирование", 5, "20.10.2023")
st.grade(102, "Математика", 5, "21.10.2023")
st.grade(103, "Математика", 3, "21.10.2023")

# 3
print(f"\nСредний балл Ивана: {st.store(101)}")

# 4
st.find(4)

# 5
st.rait()
