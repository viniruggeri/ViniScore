from jogador import Jogador
from posicao import Posicao

class CalculadoraNota:
    def __init__(self, jogador):
        self.jogador = jogador

    def calcular_nota(self):
        total_pontos = 0
        pesos = self.definir_pesos()

        for criterio, valor in self.jogador.estatisticas.obter_estatisticas().items():
            if criterio in pesos:
                total_pontos += pesos[criterio] * valor

        if self.jogador.minutos_jogados > 0:
            nota = (total_pontos / (self.jogador.minutos_jogados / 90)) * self.fator_ajuste()
            # Limitar a nota ao valor máximo de 10
            nota = min(nota, 10)  # Garante que a nota não ultrapasse 10
            return round(nota, 2)
        return 0

        return 0

    def definir_pesos(self):
        posicao = Posicao(self.jogador.posicao.nome)  # Instanciando Posicao com o nome do jogador
        return posicao.criterios

    def fator_ajuste(self):
        fatores = {
            "Falso 9": 1.1,
            "Matador": 1.2,
            "Completo": 1.0,
            "Pivô": 1.2,
            "Driblador": 1.2,
            "Cortador": 1.0,
            "Finalizador": 1.0,
            "Criador": 1.2,
            "Conector": 1.1,
            "Ofensivo": 1.2,
            "Box to Box": 1.1,
            "Motorzinho": 1.1,
            "Distribuidor": 1.1,
            "Equilibrador": 1.0,
            "Cão de Guarda": 1.1,
            "Construtor": 1.0,
            "Defensivo": 1.0,
            "Central": 1.0,
            "Lateral": 1.0,
            "Libero": 1.1,
            "Goleiro Clássico": 1.0,
            "Goleiro Moderno": 1.1,
        }
        return fatores.get(self.jogador.estilo_jogo, 1.0)
