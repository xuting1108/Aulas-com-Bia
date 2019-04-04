#nome, peso da porcao em g, preco do kg
igredientes = [['Arroz', 100, 5.00],['Carne', 100, 16.00],['Batata Inglesa', 250, 3.50], ['Cenoura', 100, 3.00],['Queijo Minas', 150, 12.00]]
#print(igredientes)
total = []
for i in igredientes:
    n = i[0]
    x = i[2] / (i[1] / 10)
    total.append(n)
    total.append(x)
print(total)
#nome do prato, igredientes e porcoes necessarias
pratos = [['muito escodidinho', 'batata inglesa', 3, 'queijo minas', 1, 'cenoura',1],['pastelao de vento', 'batata inglesa', 4, 'carne', 1]]
#print(pratos)

#prato e a qtd semanl vendida
consumo = [['muito escondidinho', 12], ['pastelao de vento', 30]]
#print(consumo)