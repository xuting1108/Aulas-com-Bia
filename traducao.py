traducao_gato = {'ingles': 'cat', 'espanhol': 'gato', 'frances': 'chat', 'alemao': 'Katze', 'italiano': 'gatto'}

#print(traducao_gato.get('ingles'))
#print(traducao_gato.get('espanhol'))
#print(traducao_gato.get('frances'))
#print(traducao_gato.get('japones'))

#for gatos in traducao_gato.items():
	#print(f'{gatos[0]}: {gatos[1]}')
print('****ordem crescente****')
for gatos in sorted(traducao_gato.items()):
	print(gatos)
print('**** reverse ***')
print(sorted(traducao_gato.values(), reverse=True))
print('**** contem es no final ****')
for gatos in sorted(traducao_gato.keys()):
	if gatos.endswith('ês'):
print(gatos)