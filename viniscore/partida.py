from jogador import Jogador
from calcularNota import CalculadoraNota

class Partida:
    def __init__(self, time_a, time_b):
        self.time_a = time_a
        self.time_b = time_b
        self.jogadores = []

    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)

    def registrar_estatisticas(self, nome_jogador, criterio, valor):
        for jogador in self.jogadores:
            if jogador.nome == nome_jogador:
                jogador.adicionar_estatistica(criterio, valor)
                print(f"Estatística {criterio} registrada para {nome_jogador} com valor {valor}.")
                break

    def calcular_notas(self):
        notas = {}
        for jogador in self.jogadores:
            calculadora = CalculadoraNota(jogador)
            notas[jogador.nome] = calculadora.calcular_nota()
        return notas
