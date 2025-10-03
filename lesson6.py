# class Dog:
#     def __init__(self, name, age, coat_color):
#         self.name = name
#         self.age = age
#         self.coat_color = coat_color
    
#     def description(self):
#         print(f"{self.name}'s coat is {self.coat_color}")

# my_dog = Dog("Philo", 5, "brown")
# my_dog.description()

# class Car:
#     def __init__(self, color, mileage):
#         self.color = color
#         self.mileage = mileage
    
#     def blue_car(self):
#         print(f"The {self.color} car has {self.mileage} miles.")

#     def red_car(self):
#         print(f"The {self.color} car has {self.mileage} miles.")

#     def drive(self, add_mileage):
#         self.mileage += add_mileage
#         return print(f"{self.color} car, miles: {self.mileage}")
        
# # car1 = Car("blue", 20000)
# # car1.blue_car()
# # car2 =Car("red", 30000)
# # car2.red_car()
# distance = Car("Blue", 100)
# distance.drive(0)

# class Dog:
#     species = "Canis Familiiaris"

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def __str__(self):
#         return f"{self.name} is {self.age} years old"
    
#     def  speak(self, sound):
#         return f"{self.name} says {sound}"
# class GoldenRetriever(Dog):
#     def speak(self, sound="BARK"):
#         return super().speak(sound)

class Rectangle:
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width
    
    def area(self):
        return self.lenght * self.width
    
class Square(Rectangle):
    def __init__(self, side_lenght):
        super().__init__(side_lenght, side_lenght)
        
s = Square(4)
print(s.area())