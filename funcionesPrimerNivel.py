def normal(x):
    return x

#normal = lambda x: x #Cuando la funcion sea utilizable hay que usar def
#Lambda solo en un momento, para algo muy simple.

def cuadrado(y):
    return y * y

def cubo(x):
    return x**3

def sumaTodos(limitTo, f):
    resultado = 0
    for i in range (0,limitTo+1):
        resultado += f(i)
    
    return resultado

if __name__ == '__main__':
    print(sumaTodos(100, normal))
    print(sumaTodos(3, cubo))
