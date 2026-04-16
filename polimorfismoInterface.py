# 1. Criamos a classe "Forma" — ela funciona como uma INTERFACE (um contrato).
#    Toda classe que herdar de "Forma" DEVE implementar o método "area()".
class Forma():

    # 2. O método "area" aqui não faz nada (por isso o "pass").
    #    Ele existe apenas para dizer: "quem herdar de mim precisa ter um método area()".
    def area(self):
        pass


# 3. Criamos a classe "Quadrado" que HERDA de "Forma" (isso é o polimorfismo via interface).
#    Ao colocar "Forma" entre parênteses, estamos dizendo que Quadrado é um tipo de Forma.
class Quadrado(Forma):

    # 4. O "__init__" é o CONSTRUTOR — ele roda automaticamente quando criamos um Quadrado.
    #    Recebe o valor do "lado" e guarda dentro do objeto com "self.lado".
    def __init__(self, lado):
        self.lado = lado

    # 5. Aqui estamos SOBRESCREVENDO o método "area()" que veio da classe Forma.
    #    Agora ele realmente calcula algo: lado elevado ao quadrado (lado ** 2).
    def area(self):
        return self.lado ** 2


# 6. Criamos um objeto "quadrado" a partir da classe Quadrado, passando lado = 5.
#    Isso chama o __init__ automaticamente e armazena self.lado = 5.
#    Se chamarmos quadrado.area(), o resultado será 5 ** 2 = 25.
quadrado = Quadrado(5)
area_quadrado = quadrado.area()
print(area_quadrado)


class Circulo(Forma):
    def __init__(self,raio):
        self.raio = raio

    def area(self):
        return 3.14 * self.raio **2
    
circulo = Circulo(4)
area_circulo = circulo.area()
print(area_circulo)

        