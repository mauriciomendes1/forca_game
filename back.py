from random import randint

#lista de temas

temas = {1:'animais',
         2:'carros',
         3:'cidades'}

dict1 = {'animais': ['cachorro', 'gato', 'urubu', 'rato', 'lagartixa', 'camaleao', 'galinha', 'camarao'],
         'carros' : ['gol', 'palio', 'celta', 'corolla', 'strada', 'toro'],
         'cidades': ['teresina', 'timon', 'altos', 'alto longa', 'sao paulo', 'fortaleza', 'sao luiz']
         }


def sortear_tema():
    tema = randint(1, 3)

    temas[tema]

    tamanho = len(dict1[temas[tema]])
    position = randint(0, tamanho - 1)

    palavra = dict1[temas[tema]][position]

    return palavra, temas[tema]

letras_acertadas = ''
def formando_palavra(letra_informada, palavra_secreta):
    global letras_acertadas

    if letra_informada in palavra_secreta:
        letras_acertadas += letra_informada

    palavra_formada = ''
    for letra in palavra_secreta:
        if letra in letras_acertadas:
            palavra_formada += letra
        else:
            palavra_formada += '*'
    
    return palavra_formada


def consultar_letra(letra, palavra_secreta):
    if letra in palavra_secreta:
        return True
    else:
        return False
