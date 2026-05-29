#Создайте базовый класс "Животное" со свойствами "вид", "количество лап", "цвет
#шерсти". От этого класса унаследуйте класс "Собака" и добавьте в него свойства
#"кличка" и "порода".

class Animal:
    def __init__(self, species, legs, color):
        self.species = species
        self.legs = legs
        self.color = color

    def show_info(self):
        print(f"Вид: {self.species}")
        print(f"Лап: {self.legs}")
        print(f"Цвет: {self.color}")


class Dog(Animal):
    def __init__(self, species, legs, color, name, breed):
        super().__init__(species, legs, color)
        self.name = name
        self.breed = breed

    def show_info(self):
        super().show_info()
        print(f"Кличка: {self.name}")
        print(f"Порода: {self.breed}")


# тест
dog = Dog("Собака", 4, "Черный", "Шарик", "Овчарка")
dog.show_info()