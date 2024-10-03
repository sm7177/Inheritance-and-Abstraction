# Activity-1
# class Parent:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id
#     def display(self):
#         print(self.name)
#         print(self.id)

# class Child(Parent):
#     def __init__(self,name, id, salary, post):
#         self.salary = salary
#         self.post = post
        
#         Parent.__init__(self, name, id)
        
#     def deatils(self):
#         print(self.name, self.id, self.salary, self.post)
        
# a=Child("Sasha", 7177, 10000, "Manager"  )
# a.display()
# a.deatils()



#Activity-2---------------------------------------------------------------------------------
# class Parent:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id
#     def display(self):
#         print(self.name)
#         print(self.id)

# class Child(Parent):
#     def __init__(self,name, id, salary, post):
#         super().__init__(name, id)
#         self.salary = salary
#         self.post = post
        
        
        
#     def deatils(self):
#         print(self.name, self.id, self.salary, self.post)
        
# a=Child("Sasha", 7177, 10000, "Manager"  )
# a.deatils()




#Activity-3--------------------------------------------------------------------------------------
from abc import ABC, abstractmethod
class Animal(ABC):
    def move(self):
        pass

class Human(Animal):
    def move(self):
        print("I can walk and run")

class Snakes(Animal):
    def move(self):
        print("I can slither and crawl")
    
class Dog(Animal):
    def move(self):
        print("I can bark and run")
        
class Lion(Animal):
    def move(self):
        print("I can roar")

H=Human()
H.move()

S=Snakes()
S.move()

D=Dog()
D.move()

L=Lion()
L.move()
