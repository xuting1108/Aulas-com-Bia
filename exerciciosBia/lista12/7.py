lista = [['Brasil', 'Italia', [10, 9]], ['Brasil', 'Espanha', [5, 7]], ['Italia', 'Espanha', [7,8]]]
faltas = 0
time = []

#print(len(lista[2][2]))
for i in lista:
    faltas += i[2][0] + i[2][1] 
    # x = i[2][0] + i[2][1]
    # time.append(x)
print(f'Numero total de faltas: {faltas}')
#sempre o i[2][0] vai pertencer ao i[0] e o i[2][1] ao i[1]
for i in lista:
    time.append(i[0])
    time.append(i[2][0])
    time.append(i[1])
    time.append(i[2][1])
print(time)


'''
import operator
 
listas = [
    ['Brasil', 'Italia', [10, 9]],
    ['Brasil', 'Espanha', [5, 7]],
    ['Italia', 'Espanha', [7,8]]
]
 
faltas = []
for lista in listas:
    jogo = {
        lista[0]: lista[2][0],
        lista[1]: lista[2][1]
    }
    faltas.append(jogo)
 
brasil = 0
italia = 0
espanha = 0
 
for falta in faltas:
    if falta.get('Brasil'):
        brasil = brasil + falta.get('Brasil')
    if falta.get('Italia'):
        italia = italia + falta.get('Italia')
    if falta.get('Espanha'):
        espanha = espanha + falta.get('Espanha')
 
 
paises = {
    'Brasil': brasil,
    'Italia': italia,
    'Espanha': espanha
}
 
min(
    paises.items(),
    key=operator.itemgetter(1)
)
'''