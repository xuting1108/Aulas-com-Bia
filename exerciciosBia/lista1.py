#****************
#a
#Crie uma função que recebe uma lista denúmeros ea.retorne o maior elementob.retorne a soma dos elementosc.retorneo número de ocorrências do primeiro elemento da listad.retorne a média dos elementose.retorne o valor mais próximo da média dos elementosf.retorne a soma dos elementos com valor negativog.retorne aquantidade de vizinhos iguais

n = int(input('informe quantos numeros terao na lista: '))
lista =  [] 
cont = 1
soma = 0
media = 0
	
while cont <= n:
	ns = int(input(f'informe o {cont}º numero da lista: '))
	cont += 1 
	lista.append(ns)
	soma += ns
	media = soma / n
print(max(lista))
print(soma)
print(media)
#lista = [1,1,1,0,9, 1, -10, 0] iguais = 0 for item in lista:     ult_indice = len(lista)-1     indice = lista.index(item)     if indice == ult_indice:         break     if lista[indice] == lista[indice+1]:          iguais = iguais +1  print(iguais) 
#lista = [1,7,1,0,9, 1, 1, -10] iguais = 0 for item in lista:     ult_indice = len(lista)-1     indice = lista.index(item)     if indice == ult_indice:         break     if lista[indice-1] == lista[indice+1]:          iguais = iguais +1  print(iguais) 

#a) Faça uma função que receba duas listase retorne True se são iguais ou False caso contrário. Duas listas são iguais se possuem osmesmos valores e na mesma ordem

def comparar_lista(lista1, lista2):
	if lista1 == lista2:
		return True
	else: 
		return False
print(comparar_lista([5, 4, 3], [5, 4, 3]))
