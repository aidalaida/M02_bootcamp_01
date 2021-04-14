def normal(x):
    return x

def cuadrado(y):
    return y * y

def sumaTodos(limitTo, f):
    resultado = 0
    for i in range (0,limitTo+1):
        resultado += f(i)
    
    return resultado

print(sumaTodos(100, normal))
print(sumaTodos(3, cuadrado))