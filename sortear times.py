import random
players = list()
time = list()

times = int(input('Quantidade de times: '))
jtime = int(input('Jogadores por time: '))

jogadores = times * jtime #quant de jogadores

for c in range(1,jogadores+1):          #lista do 
    p = str(input(f'Jogador {c}: '))      #nome dos jogadores
    players.append(p) 

print('-='*15)

for t in range(1,times+1):
    print(f'Time {t}: ')
    time_atual = []

    while len(time_atual) < jtime:
        jog = random.choice(players)
        players.remove(jog)
        time_atual.append(jog)
    for b,m in enumerate(time_atual):
        print(m)
        time.append(time_atual)







