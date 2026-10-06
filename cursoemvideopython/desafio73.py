from cordes import desafio ,cores
desafio(73)
                # crie uma tupla com 20 colocados da tabela de um campeonado brasileiro
times = ('corinthians','santos','palmeiras',
         'flamengo','sao paulo','vasco','bota fogo',
         'fluminense','gremio','atletico mineiro',
         'portuguesa','atletico paranaese','mirasol',
         'bahia','chapecoense','sport(recife)','fortaleza',
         'cruzeior','bragantino','vitoria')

                # mostre os 5 primeiros colocados
print(f'os 5 primeiros colocados sao {times[:5]}')
print('=' * 40)
                # mostre os 4 ultimos colocados
print(f'os 4 ultimos colocados sao {times[16:]}')
print('=' * 40)
                # mostre  em ordem alfabetica
print(sorted(times))
print('=' * 40)
                # mostre em qual posição esta o time digitado
time = input('digite o time: ').lower().strip()
print(f'o time digitado esta na {times.index(time)+1}° posição')