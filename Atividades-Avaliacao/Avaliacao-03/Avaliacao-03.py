def primo(p):
    contador = 0
    for i in range(1,p+1):
        if p%i==0:
            contador = contador+1
    if  contador==2:
        return True
    else:
        return False
def soma_primos(n):
    i = 0
    p = 0
    soma = 0
    if n > 0:
        while i < n:
            if primo(p):
                soma += p
                i += 1
            p += 1
        return soma
    else:
        return "Número inválido"
n = int(input("diga a quantidade de números primos a serem somados: "))
somaN = soma_primos(n)
print("A soma dos {} primeiros números primos é \"{}\"!".format(n,somaN))