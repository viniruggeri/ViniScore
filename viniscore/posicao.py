from criterios import Criterios

class Posicao:
    def __init__(self, nome):
        # Inicializa a posição do jogador e obtém os critérios associados
        self.nome = nome
        self.criterios = Criterios(nome).obter_criterios()  # Obtendo critérios específicos para a posição

    def obter_criterios(self):
        # Retorna os critérios definidos para a posição
        return self.criterios

    def __str__(self):
        # Representação em string da posição e seus critérios
        return f"Posição: {self.nome}, Critérios: {self.criterios}"
