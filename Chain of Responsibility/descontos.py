class desconto_itens(object):

    def __init__(self, prox_desconto):
        self.__proximo_desconto = prox_desconto

    def calcula(self, orcamento):
        if orcamento.total_itens > 5:
            return orcamento.valor * 0.
        else:
            return self.__proximo_desconto.calcula(orcamento)


class desconto_valor(object):

    def __init__(self, prox_desconto):
        self.__proximo_desconto = prox_desconto

    def calcula(self, orcamento):
        if orcamento.valor > 500:
            return orcamento.valor * 0.07
        else:
            return self.__proximo_desconto.calcula(sem_desconto)


class sem_desconto(object):
    def calcula(self):
        return 0
