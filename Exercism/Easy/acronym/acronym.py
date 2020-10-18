# coding: utf-8
import string
import re


# Usando regex
def abbreviate(words):
    lista = []
    alfabeto = list(string.ascii_uppercase) + list(string.ascii_lowercase)
    unir = ''
    words_limpando = words.replace("'", '').replace('_', '')
    recebendo_apenas_alfa_numerico = re.sub(r"\W+", ' ', words_limpando)
    recebendo_fatiado = recebendo_apenas_alfa_numerico.split(' ')
    for i in recebendo_fatiado:
        lista.append(i[0])
    retorna = unir.join(lista).upper()
    return retorna


print(abbreviate("Casa's -  Blanca-Club unir _Not_"))


# import string
#
#
# # Sem regex
# def abbreviate(words):
#     lista = []
#     unir = ''
#     recebe_limpando = words.replace('_', '').replace(' - ', ' ').replace('-', ' ')
#     recebe_fatiado = recebe_limpando.split(' ')
#     letras = list(string.ascii_uppercase) + list(string.ascii_lowercase)
#     for i in recebe_fatiado:
#         if i[0] in letras:
#             lista.append(i[0])
#     retorna = unir.join(lista).upper()
#     return retorna


print(abbreviate("Casa's - Blanca-Club unir _Not_"))
