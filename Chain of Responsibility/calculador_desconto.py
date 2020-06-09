from descontos import desconto_itens, desconto_valor, sem_desconto


class Calculador_desconto(object):

    def calculador(self, orcamento):
        desconto = desconto_itens(desconto_valor(
            sem_desconto)).calcula(orcamento)

        return desconto


if __name__ == "__main__":
    from orcamento2 import orcamento, Item

    orcamento = orcamento()
    orcamento.add_item(Item('ITEM - 1', 100))
    orcamento.add_item(Item('ITEM - 2', 400))
    orcamento.add_item(Item('ITEM - 3', 70))

    calculador = Calculador_desconto()
    desconto = calculador.calculador(orcamento)

    print(desconto)
