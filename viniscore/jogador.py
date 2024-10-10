from estatisticas import Estatisticas
from posicao import Posicao

class Jogador:
    def __init__(self, nome, minutos_jogados, posicao_nome, estilo_jogo):
        self.nome = nome
        self.minutos_jogados = minutos_jogados
        self.estilo_jogo = estilo_jogo
        self.posicao = Posicao(posicao_nome)
        self.estatisticas = Estatisticas()  # Inicializando as estatísticas

    def adicionar_estatistica(self, criterio, valor):
        self.estatisticas.adicionar_estatistica(criterio, valor)

    def adicionar_minutos(self, minutos):
        self.minutos_jogados += minutos

    def calcular_nota(self):
        total_pontos = 0
        pesos = self.posicao.obter_criterios()

        for criterio, valor in self.estatisticas.obter_estatisticas().items():
            if criterio in pesos:
                total_pontos += pesos[criterio] * valor

        if self.minutos_jogados > 0:
            nota = (total_pontos / self.minutos_jogados) * self.fator_ajuste()
            return round(nota, 2)
        return 0

    def fator_ajuste(self):
        fatores = {
            "Falso 9": 1.2,
            "Matador": 1.1,
            "Completo": 1.0,
            "Pivô": 1.0,
            "Driblador": 1.1,
            "Cortador": 1.0,
            "Finalizador": 1.1,
            "Criador": 1.2,
            "Conector": 1.0,
            "Ofensivo": 1.1,
            "Motorzinho": 1.2,
            "Box to Box": 1.1,
            "Distribuidor": 1.0,
            "Equilibrador": 1.0,
            "Cão de Guarda": 1.1,
            "Construtor": 1.0,
            "Ofensivo": 1.0,
            "Defensivo": 1.0,
            "Central": 1.0,
            "Lateral": 1.0,
            "Libero": 1.1,
            "Goleiro Clássico": 1.0,
            "Goleiro Moderno": 1.1,
        }
        return fatores.get(self.estilo_jogo, 1.0)

    def __str__(self):
        return f"Jogador: {self.nome}, Estilo: {self.estilo_jogo}, Minutos: {self.minutos_jogados}, Estatísticas: {self.estatisticas.obter_estatisticas()}"
