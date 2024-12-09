# RECURSÃO #

# ENTRADA -> FUNÇÃO -> SAÍDA (PRÓPRIA FUNÇÃO)

def fatorial(numero):
    if numero == 1:
        return 1
    return numero * fatorial(numero - 1)


print(fatorial(5))


def fibonacci(numero):
    if numero == 0:
        return 0
    elif numero == 1:
        return 1
    return fibonacci(numero - 2) + fibonacci(numero -1)


print(fibonacci(13))
