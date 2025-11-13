class Animal:
    def speak(self):
        return "Animal Speaks"
class Dog(Animal):
    def bark(self):
        return "Dog barks"
    def speak(self):
        return "Dog Speaks"

class Cat(Animal):
   def meow(self):
       return "Cat meows"
   def speak(self):
       return "Cat Speaks" 
   
class Pets(Dog,Cat):
# class Pets(Animal):
    def __init__(self):
        super().__init__()
    def pet_info(self): 
        return "This is a pet"
    
obj1 = Pets()
print(obj1.speak())
