class Pessoa:
    def __init__(self, nome = None, idade = 19):
        self.idade = idade
        self.nome = nome
    def cumprimentar (self):
        return f'Olá! {id(self)}'

if __name__ == '__main__':
    p = Pessoa('Eustáquio')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    p.nome = 'Breno'
    print(p.nome)
    print(p.idade)