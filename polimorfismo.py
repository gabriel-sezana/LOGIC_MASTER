class Animal:
    def emitir_som(self):
        print('algum som...')


class Cachorro(Animal):
    def emitir_som(self):
        print('auau')

cachorro = Cachorro()
cachorro.emitir_som()

class Gato(Animal):
    def emitir_som(self):
        print('miau')

gato = Gato()
gato.emitir_som()
