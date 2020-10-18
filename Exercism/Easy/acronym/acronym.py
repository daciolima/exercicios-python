# import string
#
#
# def abbreviate(words):
#     lista1 = []
#     unir = ''
#     recebe = words.replace('_', '')
#     recebe1 = recebe.replace(' - ', ' ').replace('-', ' ')
#     recebe3 = recebe1.split(' ')
#     letras = list(string.ascii_uppercase) + list(string.ascii_lowercase)
#     for i in recebe3:
#         if i[0] in letras:
#             lista1.append(i[0])
#     retorna = unir.join(lista1).upper()
#     print(recebe)
#     return retorna


import string
import re


def abbreviate(words):
    lista1 = []
    unir = ''
    words_total = words.replace("'", '')
    recebe = re.sub(r"\W+", ' ', words_total).replace('_', '').replace("'", '')
    recebe_total = recebe.split(' ')
    letras = list(string.ascii_uppercase) + list(string.ascii_lowercase)
    for i in recebe_total:
        if i[0] in letras:
            lista1.append(i[0])
    retorna = unir.join(lista1).upper()
    print(recebe)
    return retorna


print(abbreviate("Casa's - Blanca-Club unir _Not_"))
