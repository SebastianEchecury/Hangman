import random
from palabras import palabras

def obtenerPalabraValida(palabras):
    palabra = random.choice(palabras)
    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(palabras)
    return palabra

def ahorcado():
    palabra = obtenerPalabraValida(palabras).upper()
    palabraAux = []
    cantErrores = 0
    cantAciertos = 0
    letrasPalabra = list(palabra)
    letrasUsadas = []
    gano = False

    for x in range(len(palabra)):
        palabraAux.append('*')

    while (not gano and cantErrores <= 5):
        # print(palabra)
        print(palabraAux)
        if bool(letrasUsadas):
            print('Letras usadas')
            print(letrasUsadas)

        print('Escoja una letra: ', end = '')
        letra = input()
        while letra in palabra:
            print('Letra ya ingresada')
            letra = input()

        if not(letra.upper() in letrasPalabra):
            print('Letra equivocada')
            letrasUsadas.append(letra)
            cantErrores = cantErrores + 1
        else:
            print('Letra acertada')
            for x in range(len(letrasPalabra)):
                if letrasPalabra[x-1] == letra.upper():
                    cantAciertos = cantAciertos + 1
                    palabraAux[x-1] = letra.upper()
        if cantAciertos == len(letrasPalabra): gano = True

    return gano

if ahorcado(): print('Gano')
else: print('Perdio')