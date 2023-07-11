print("Classes diferentes com o mesmo nome do método.\n")

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")

class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail!")

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly!")

car1 = Car("Ford", "Mustang") #Cria um objeto carro
boat1 = Boat("Ibiza", "Touring 20") #Cria um objeto barco
plane1 = Plane("Boeing", "747") #Cria um objeto avião

for x in (car1, boat1, plane1):
    print(x.brand, x.model)
    x.move()


print("\nPolimorfismo em herança. Criada classe Vehicle e as classes Car, Boat, Plane serão classes filhas de Vehicle\n")

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move!")

class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print("Sail!")

class Plane(Vehicle):
    def move(self):
        print("Fly!")

car1 = Car("Ford", "Mustang") #Cria um objeto carro
boat1 = Boat("Ibiza", "Touring 20") #Cria um objeto barco
plane1 = Plane("Boeing", "747") #Cria um objeto avião

for x in (car1, boat1, plane1):
    print(x.brand, x.model)
    x.move()
