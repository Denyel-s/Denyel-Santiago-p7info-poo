# Avalição 03
A Função definida abaixo define se um número não negativo é primo.


def primo(p):
    contador = 0
    for i in range(1,p+1):
        if p%i==0:
            contador = contador+1
    if  contador==2:
        return True
    else:
        return False


Implemente uma função Python que receba um inteiro não negativo n e imprima a soma dos n primeiros números primos. 
Por exemplo: 
Para n=3, resultado 10=2+3+5. 
Para n=7, resultado 58=2+3+5+7+11+13+17. 
Para n=100, resultado 24133.