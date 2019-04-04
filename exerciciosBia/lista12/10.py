def mostrar_signos(lista):
    signos = ['Macaco', 'Galo', 'Cão', 'Porco', 'Rato', 'Boi', 'Tigre', 'Coelho', 'Dragão', 'Serpente', 'Cavalo', 'Carneiro']
    #faz o split dadata de aniversario
    data = [i.split('/') for i in aniversarios]
    #print(data) 

    anos = []
    #vai pegar o indice 2 (que é o ano) de cada item
    for item in data:
        anos.append(item[2])
    #print(ano)
    #transformo os itens en inteiros para poder fazer as comparacoes
    for ano in anos: 
        ano = int(ano) 
        if ano % 12 == 0:
            print(ano,signos[0])

        elif ano % 12 == 1:
            print(signos[1])

        elif ano % 12 == 2:
            print(signos[2])

        elif ano % 12 == 3:
            print(signos[3])

        elif ano % 12 == 4:
            print(signos[4])

        elif ano % 12 == 5:
            print(signos[5])

        elif ano % 12 == 6:
            print(signos[6])

        elif ano % 12 == 7:
            print(signos[7])

        elif ano % 12 == 8:
            print(signos[8])

        elif ano % 12 == 9:
            print(signos[9])

        elif ano % 12 == 10:
            print(signos[10])

        elif ano % 12 == 11:
            print(signos[11])
aniversarios = ['27/03/2000','11/08/1992', '23/09/2003', '15/07/2013', '18/09/1997']
mostrar_signos(aniversarios)