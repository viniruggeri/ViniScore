from jogador import Jogador


class Equipe:
    def __init__(self, nome):
        # Inicializa a equipe com um nome e uma lista vazia de jogadores
        self.nome = nome
        self.jogadores = []

    def adicionar_jogador(self, jogador):
        # Adiciona um jogador à lista de jogadores da equipe
        self.jogadores.append(jogador)

    def calcular_nota_media(self):
        # Calcula a média das notas dos jogadores da equipe
        total_nota = 0
        for jogador in self.jogadores:
            total_nota += jogador.obter_nota()  # Usa o método obter_nota para calcular a nota do jogador
        
        if len(self.jogadores) > 0:
            return round(total_nota / len(self.jogadores), 2)
        return 0

    def listar_jogadores(self):
        # Lista os jogadores da equipe
        for jogador in self.jogadores:
            print(jogador)

    def __str__(self):
        # Retorna uma representação da equipe, incluindo o nome e o número de jogadores
        return f"Equipe: {self.nome}, Jogadores: {len(self.jogadores)}"
    
    def registrar_estatisticas(self, jogador, tipo, valor):
        # Verifica se o jogador já existe na lista de jogadores da partida
        if jogador not in self.jogadores:
            raise ValueError(f"Jogador {jogador.nome} não está registrado na partida.")

        # Verifica se o tipo de estatística já existe para o jogador, caso contrário, inicializa
        if tipo not in jogador.estatisticas:
            jogador.estatisticas[tipo] = 0
    
        # Atualiza o valor da estatística
        jogador.estatisticas[tipo] += valor

    # Exibe uma confirmação para facilitar o rastreamento
    print(f"Estatística registrada: {jogador.nome} - {tipo} = {jogador.estatisticas[tipo]}")
