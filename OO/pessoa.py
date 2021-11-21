class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome = None, idade = 19):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar (self):
        return f'Olá! meu nome é {self.nome}'
    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atribututos_de_classe(cls):
        return(f'{cls} - olhos {cls.olhos} ')

class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return f'{cumprimentar_da_classe}, aperto de mão.'


class Mutante(Pessoa):
    olhos = 3

if __name__ == '__main__':
    pessoa = Pessoa
    breno = Homem(nome = 'Breno')
    walter = Homem(breno, nome = 'Walter' )
    print(Pessoa.cumprimentar(breno))
    print(id(breno))
    print(breno.cumprimentar())
    print(breno.idade)
    for filho in walter.filhos:
        print(filho.nome)
    walter.sobrenome = 'Eustáquio'
    del walter.filhos
    breno.olhos = 1
    del breno.olhos
    print(breno.__dict__)
    print(walter.__dict__)
    print(Pessoa.olhos)
    print(walter.olhos)
    print(breno.olhos)
    print(id(Pessoa.olhos), id(walter.olhos), id(breno.olhos))
    print(Pessoa.metodo_estatico(), breno.metodo_estatico())
    print(Pessoa.nome_e_atribututos_de_classe(), breno.nome_e_atribututos_de_classe())
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(breno, pessoa))
    print(isinstance(breno, Homem))
    print(breno.cumprimentar())
    print(walter.cumprimentar())




