# cont = 1
# while cont <= 49:
#     print(cont)
#     cont += 2

class Animal:
    # - tamanho: float
    # - tipo
    # - idade
    # - alimentação
    # + fazer barulho
    def __init__(self, tamanho, tipo, idade, alimentacao) -> None:
        self.tamanho = tamanho
        self.tipo = tipo
        self.idade = idade
        self.alimentacao = alimentacao

    def fazer_barulho(self):
        print("Esse animal não faz barulho")


class Gato(Animal):
    def __init__(self, tamanho, idade) -> None:
        super().__init__(tamanho, "Felino", idade, "onivoro")


    def fazer_barulho(self):
        print("Miau!")

animal = Animal(0, "sei lá", 0, "nao faço ideia")
animal.fazer_barulho()

gato = Gato(2.4, 1)
gato.fazer_barulho()
print(animal.alimentacao)
