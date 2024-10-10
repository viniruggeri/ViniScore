from partida import Partida
from jogador import Jogador

# Criar dois jogadores com todas as estatísticas
jogador1 = Jogador("Jogador 1", 90, "atacante", "Falso 9")
jogador1.adicionar_estatistica('gols', 2)
jogador1.adicionar_estatistica('assistencias', 1)
jogador1.adicionar_estatistica('passes', 5)
jogador1.adicionar_estatistica('dribles', 3)
jogador1.adicionar_estatistica('desarme', 1)
jogador1.adicionar_estatistica('interceptacao', 0)
jogador1.adicionar_estatistica('faltas_cometidas', 2)
jogador1.adicionar_estatistica('faltas_sofridas', 1)
jogador1.adicionar_estatistica('cartoes_amarelos', 0)
jogador1.adicionar_estatistica('cartoes_vermelhos', 0)

jogador2 = Jogador("Jogador 2", 85, "meia_armador", "Criador")
jogador2.adicionar_estatistica('gols', 1)
jogador2.adicionar_estatistica('assistencias', 2)
jogador2.adicionar_estatistica('passes', 8)
jogador2.adicionar_estatistica('dribles', 4)
jogador2.adicionar_estatistica('desarme', 2)
jogador2.adicionar_estatistica('interceptacao', 1)
jogador2.adicionar_estatistica('faltas_cometidas', 1)
jogador2.adicionar_estatistica('faltas_sofridas', 0)
jogador2.adicionar_estatistica('cartoes_amarelos', 1)
jogador2.adicionar_estatistica('cartoes_vermelhos', 0)

# Criar partida
partida = Partida("Time A", "Time B")
partida.adicionar_jogador(jogador1)
partida.adicionar_jogador(jogador2)

# Calcular notas
notas = partida.calcular_notas()
print("Notas da Partida:", notas)
