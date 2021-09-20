def printDecimal(x):
    print("   ", x, end='')
def printOctal(x):
    print("           ", oct(x), end='')
def printHexadecimal(x):
    print("           ", hex(x), end='')
def printBinario(x):
    print("             ", bin(x), end='')
def imprimirTabela():
    x = 0
    print("   Decimal      Octal       Hexadecimal           Binario")
    print("------------- --------- --------------------- -----------------")
    while x <= 255:
        printDecimal(x), printOctal(x), printHexadecimal(x), printBinario(x)
        print("\n")
        x += 1
imprimirTabela()