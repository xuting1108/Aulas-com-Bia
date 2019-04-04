p = float(input('insira seu peso: '))
a = float(input('insira sua altura:'))
def calcularIMC(p, a):
	imc =  (p / a**2)
	return imc 

imc = calcularIMC(p,a)

if imc < 20:
	print('abaixo do peso')
elif imc >=20 or imc<= 24.9:
	print('normal')
elif imc >24.9 or imc<= 29.9:
	print('sobrepeso')
else: 
	print('obesidade')