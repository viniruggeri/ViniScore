class Estatisticas:
    def __init__(self):
        # Inicializa um dicionário para armazenar as estatísticas do jogador
        self.estatisticas = {
            'gols': 0,
            'assistencias': 0,
            'passes': 0,
            'dribles': 0,
            'faltas_cometidas': 0,
            'desarme': 0,  
            'interceptacao': 0,
            'faltas_sofridas': 0,
            'cartoes_amarelos': 0,
            'cartoes_vermelhos': 0,
            # Adicione outras estatísticas conforme necessário
        }

    def adicionar_estatistica(self, criterio, valor):
        # Adiciona valor à estatística correspondente, se o critério for reconhecido
        if criterio in self.estatisticas:
            self.estatisticas[criterio] += valor
        else:
            print(f"Criterio '{criterio}' não reconhecido.")

    def obter_estatisticas(self):
        # Retorna o dicionário de estatísticas
        return self.estatisticas

    def resetar_estatisticas(self):
        # Reseta todas as estatísticas para zero
        for criterio in self.estatisticas:
            self.estatisticas[criterio] = 0
