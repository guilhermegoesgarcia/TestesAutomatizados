

class Usuario:

    def __init__(self, nome, carteira):
        self.__nome = nome
        self.__carteira = carteira

    def propoe_lance(self, leilao,valor):
        if not self.__valor_eh_valido(valor):
            raise ValueError('O usuário não pode propor lances maior do que o valor contido na carteira ! __SALDO INSUFICIENTE__')

        lance = Lance(self, valor)
        leilao.propoe(lance)

        self.__carteira -= valor

    @property
    def nome(self):
        return self.__nome

    @property
    def carteira(self):
        return self.__carteira

    def __valor_eh_valido(self, valor):
        return valor <= self.__carteira


class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao):

        self.descricao = descricao
        self.__lances = []
        self.maior_lance = 0.0
        self.menor_lance = 0.0

    def propoe(self, lance: Lance):
        if self.lance_eh_valido(lance):
            if not self.__tem_lances():
                self.menor_lance = lance.valor
            self.maior_lance = lance.valor

            self.__lances.append(lance)
        else:
            raise ValueError('Erro ao propor lance.')

    @property
    def lances(self):
        return self.__lances[:]

    def __tem_lances(self):
        return self.__lances

    def __usuarios_diferentes(self, lance):
        return self.__lances[-1].usuario != lance.usuario

    def __valor_maior_que_lance_anterior(self, lance):
        return lance.valor > self.__lances[-1].valor

    def lance_eh_valido(self,lance):
        return not self.__tem_lances() or (self.__usuarios_diferentes(lance) and
                                           self.__valor_maior_que_lance_anterior(lance))









