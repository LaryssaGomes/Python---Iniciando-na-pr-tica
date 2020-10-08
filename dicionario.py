cars = {}
cars['corola'] = "red"
cars['fit'] = "green"
cars['320'] = "black"
print(cars)
cars.keys()	#  Retorna todas as chaves do dicionário
cars.values()  #  Retorna todos os valores do dicionário
cars["corola"]	 #  Retorna o valor referente a chave informada
# Declarando um dicionário usando dict
people = dict(Wesley='Father',Mariana="Mother",Sarah="baby")

# Declarando um dicionário com chaves
family = {
    'wesley' : 'Father'
}

# Verificando se existe uma chave antes de imprimir
if 'Wesley' in people:
    print(people['Wesley'])

cars = {
    "Corola" : "red",
    "Fit" : "green",
    "320" : "black"
}

for key, value in cars.items():
    print(key + " - " + value)