class Criterios:
    def __init__(self, posicao):
        # Inicializa a classe com a posição do jogador e define os critérios
        self.posicao = posicao
        self.criterios = self.definir_criterios()

    def definir_criterios(self):
        # Define os critérios de pontuação para cada posição
        criterios = {
            'atacante': {
                'gols': 3,
                'assistencias': 2,
                'passes': 1,
                'dribles': 2,
                'desarme': 0,
                'interceptacao': 0,
                'faltas_cometidas': -1,
                'cartoes_amarelos': -2,
                'cartoes_vermelhos': -5,
            },
            'ponta': {
                'gols': 3,
                'assistencias': 1,
                'passes': 1,
                'dribles': 3,
                'desarme': 0,
                'interceptacao': 2,
                'faltas_cometidas': -1,
                'cartoes_amarelos': -2,
                'cartoes_vermelhos': -5,
            },
            'meia_armador': {
                'gols': 2,
                'assistencias': 2,
                'passes': 2,
                'dribles': 2,
                'desarme': 1,
                'interceptacao': 1,
                'faltas_cometidas': -1,
                'cartoes_amarelos': -2,
                'cartoes_vermelhos': -5,
            },
            'meia_central': {
                'gols': 2,
                'assistencias': 3,
                'passes': 3,
                'dribles': 1,
                'desarme': 1,
                'interceptacao': 1,
                'faltas_cometidas': -1,
                'cartoes_amarelos': -2,
                'cartoes_vermelhos': -5,
            },
            'volante': {
                'gols': 1,
                'assistencias': 2,
                'passes': 3,
                'dribles': 1,
                'desarme': 2,
                'interceptacao': 2,
                'faltas_cometidas': -1,
                'cartoes_amarelos': -2,
                'cartoes_vermelhos': -5,
            },
            'lateral': {
                'gols': 1,
                'assistencias': 2,
                'passes': 2,
                'dribles': 2,
                'desarme': 1,
                'interceptacao': 3,
                'faltas_cometidas': -1,
                'cartoes_amarelos': -2,
                'cartoes_vermelhos': -5,
            },
            'zagueiro': {
                'gols': 0,
                'assistencias': 1,
                'passes': 2,
                'dribles': 1,
                'desarme': 2,
                'interceptacao': 3,
                'faltas_cometidas': -1,
                'cartoes_amarelos': -2,
                'cartoes_vermelhos': -5,
            },
            'goleiro': {
                'gols': 0,
                'assistencias': 0,
                'passes': 2,
                'dribles': 1,
                'desarme': 0,
                'interceptacao': 0,
                'bolas defendidas': 2,
                'faltas_cometidas': -1,
                'cartoes_amarelos': -2,
                'cartoes_vermelhos': -5,
            },
        }
        return criterios.get(self.posicao, {})

    def obter_criterios(self):
        # Retorna os critérios definidos para a posição do jogador
        return self.criterios
