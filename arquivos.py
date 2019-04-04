import csv
with open('pessoas.csv', 'w', newline='') as csvfile:
	colunas = ['nome', 'peso', 'altura']
	writer = csv.DictWriter(csvfile, fieldnames=colunas)
	writer.writeheader()
	writer.writerow({'nome': 'Annie', 'peso': 35.5, 'altura': 1.30,})
	writer.writerow({'nome': 'Claire', 'peso': 39.5, 'altura': 1.35,})