from historico import Historico


class Calculadora:
    def __init__(self):
        self.historico = Historico()

    def calcular(self, operacao, simbolo):
        resultado = operacao.executar()
        registro = f"{operacao.primeiro} {simbolo} {operacao.segundo} = {resultado}"
        self.historico.adicionar(registro)
        return resultado

    def obter_historico(self):
        return self.historico.listar()

    def limpar_historico(self):
        self.historico.limpar()
