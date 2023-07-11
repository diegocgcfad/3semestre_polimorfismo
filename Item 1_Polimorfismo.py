class Animal:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie

    def dieta(self):
        print("Carnívoro")
        
class Leao(Animal):
    pass # Palavra pass para não alterar nenhuma propriedade

class Aguia(Animal):
    pass

class Cavalo(Animal):
    def dieta(self): # Alterando a função
        print("Herbívoro")

class Tartaruga(Animal):
    def dieta(self):
        print("Onívoro")

leao1 = Leao("Simba", "Leão Africano") #Cria um objeto Leão
aguia1 = Aguia("Swoop","Águia-careca") #Cria um objeto Aguia
cavalo1 = Cavalo("Wildfire", "Appaloosa") #Cria um objeto Cavalo
tartaruga1 = Tartaruga("Crush", "Tartaruga-verde") #Cria um objeto Tartaruga

for x in (leao1, aguia1, cavalo1, tartaruga1):
    print("\n",x.nome, "-",x.especie)
    x.dieta()
