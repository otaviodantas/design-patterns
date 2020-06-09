from impostos import calcular_ISS, calcular_ICMS


class calculador_impostos(object):

    def realiza_calculo(self, orcamento, imposto):
        imposto_calculado = imposto(orcamento)
        print(imposto_calculado)


if __name__ == "__main__":
    from orcamento import orcamento

    calculador = calculador_impostos()
    orcamento = orcamento(500)

    calculador.realiza_calculo(orcamento, calcular_ISS)
    calculador.realiza_calculo(orcamento, calcular_ICMS)
