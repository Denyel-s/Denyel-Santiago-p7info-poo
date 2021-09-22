def split_word(palavra):
    palavra1 = palavra.split()
    return palavra1
def count_palavra(palavra):
    x = palavra.count('')-1
    return x
def count_word(palavra):
    split_count = []
    i=0
    for x in split_word(palavra):
        count = count_palavra(x)
        split_count.insert(i, count) 
        i += 1
    return split_count
def number_list(lista):
    n = len(lista)
    i = 0
    while i <n-1: 
        print(lista[i],end='-')
        i += 1
    print(lista[n-1])
def print_count(lista):
    print('-'*60)
    for phrase in lista:
        count_list = count_word(phrase)
        print("{:<40s} | ".format(phrase), end='')
        number_list(count_list)
def sort_list(lista):
    return len(lista)
def bigger_word(lista):
    word_list = []
    for phrase in lista:
        phrase_split = phrase.split()
        for word in phrase_split:
            word_list.append(word)
    word_list.sort(reverse=True, key=sort_list)
    return word_list[0]
i = 1
lista_de_palavras = []
print("{}\n{:<40}".format('-'*60,'Contador de caracteres em frases.'))
while (1 <= i <=100): 
    Frase = input("{}\nDigite sua frase a ser contada ou \"0\" para finalisar: \n".format('-'*60))
    i += 1
    if Frase != 0 and Frase != str(0):
        lista_de_palavras.append(Frase)
    if Frase == 0 or Frase == str(0):
        break
print_count(lista_de_palavras)
print(lista_de_palavras)
bigger_word_number = count_palavra(bigger_word(lista_de_palavras))
print('-'*60,"\nMaior palavra das frases: \"{}\"! Possuindo {} caracteres.".format(bigger_word(lista_de_palavras),bigger_word_number))