# with open('test.txt', 'w') as f:
#     list_ = [str(i) + '\n' for i in range(5)]
#     f.writelines(list_)
#     with open('test.txt', 'r') as f2:
#         f.seek(1)
#         print(f2.readlines())

# процедурное програмирование
# функциональное програмированние
# ООП

# Полиморфизм
# Инкапсуляция - инкапсуляция данных, защита данных
# Наследование
# Агрегация
# Композиция
# Абстракция

class Animal:
    # атрибуты класса
    eyes = 2 

    # атрибуты экземпляра класса
    def __init__(self, name, feet):
        self.name = name
        self.feet = feet

    # instance method
    def sound(self, noise):
        return noise
    
    # class method
    @classmethod
    def change_eyes(cls, new_q):
        cls.eyes=new_q

    # static method
    @staticmethod
    def say():
        print("I'm not an animal")

# dog = Animal(name='Tuzik', feet=4)
# cat = Animal('Barsik', 3)
# bird = Animal('Kesha', 2)

# print(dog.sound('Woof woof'))

# dog.change_eyes(3)
# print(dog.eyes)

# dog.say()

# class FlyMixin:
#     def fly(self):
#         return 'I fly'

# class SwimMixin:
#     def swim(self):
#         return 'I swim'

# class Dog(Animal):
#     def sound(self):
#         return 'Woof'

# class Bird(Animal):
#     def sound(self):
#         return 'Chik-chirik'

# dog = Dog('Bobik', 4)
# bird = Bird('Popka', 2)
# print(dog.sound())
# print(bird.sound())

# git - инструмент для работы с версиями кода (система управления версиями)
# github -  




