def retrocontador(e):
    print("{},".format(e), end="")
    if e > 0:
        retrocontador(e-1)

retrocontador(10)

def sumatorio(n):
    if n > 0:
        return n + sumatorio(n-1) #acumulamos sobre n, aunque en verdad lo hace
    else:
        return 0

sumatorio(4)

def factorial(n):
    if n > 0:
        return n * factorial(n-1)
    else:
        return 1

factorial(5)