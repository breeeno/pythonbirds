class Pessoa:
    def __init__(self, *filhos, nome = None, idade = 19):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar (self):
        return f'Olá! {id(self)}'

if __name__ == '__main__':
    breno = Pessoa(nome = 'Breno')
    walter = Pessoa(breno, nome = 'Walter' )
    print(Pessoa.cumprimentar(breno))
    print(id(breno))
    print(breno.cumprimentar())
    print(breno.idade)
    for filho in walter.filhos:
        print(filho.nome)
    walter.sobrenome = 'Eustáquio'
    del walter.filhos
    print(breno.__dict__)
    print(walter.__dict__)