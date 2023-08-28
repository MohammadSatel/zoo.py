class Animal:
    def eat(self):
        print("eat")

    def move(self):
        print("move")

    def __str__(self) -> str:
        return __class__.__name__

class Fish(Animal):
    def move(self):
        print("Fish swim fast!")

class Zebra(Animal):
    def move(self):
        print("Zebras run fast!")

    def eat(self):
        print("Zebras eat grass!")

    def __init__(self, age, gender, name) -> None:
        self.age = age
        self.gender = gender
        self.name = name

class Lion(Animal):
    def eat(self):
        print("Lions eat meat!")
        
    def move(self):
        print("Lions run fast!")

    def __init__(self, age, gender, name) -> None:
        self.age = age
        self.gender = gender
        self.name = name

if __name__ == "__main__":
    lst = []
    lion1 = Lion(age=7,gender="male",name="Mufasa")
    lion2 = Lion(age=4,gender="female",name="Lopo")
    zebra1 = Zebra(age=11,gender="male",name="Wowo")
    zebra2 = Zebra(age=2,gender="female",name="Coa")
    fish1 = Fish()
    fish2 = Fish() 
    lst.append(lion1)
    lst.append(zebra1)
    lst.append(fish1)
    for x in lst:
        print(x)

    lion1.move()
    lion2.eat()
    zebra1.move()
    zebra2.eat()
    fish1.move()
    fish2.eat()