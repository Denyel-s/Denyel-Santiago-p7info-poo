def split_word(palavra):
    palavra1 = palavra.split()
    return palavra1
def count_word(palavra):
    for x in split_word(palavra):
        print(x.count('')-1,end='-')
    print("")
teste = "I love you"
teste2 = "te t e te t e te t e te"
teste_split = teste.splitlines()
for phrase in teste_split:
    phrase_split = phrase.split()
    print(phrase_split)
print(split_word(teste))
count_word(teste)
count_word(teste2)