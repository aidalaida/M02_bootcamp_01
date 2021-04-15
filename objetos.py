import turtle # crear un objeto del modulo turte del tipo Turtle con mayusculas---- objetos SIEMPRE CON MAYUSCULAS---- son funciones de primer nivel que son capaces de invocarse y
#crearse copias de si misma, con parantesis y parametros. misma funcionalidad y atributos distintos. funciones en el objeto. help('turtle')

tortuguita = turtle.Turtle()
otraTortuguita = turtle.Turtle() #Son instancias de la clase turtle, copias del objeto de clase turtle. espacios de memoria que deja reservados para ciertas funciones. invocandose cuando quieran. 
lentorra = turtle.Turtle()

lentorra.speed(1)
tortuguita.shape('turtle') #En parentesis son los métodos de la clase (speed, color) funciones que puede realizar un objeto de clase turtle
tortuguita.color('blue') # atributos 
tortuguita.fd(50)
tortuguita.speed(5)

otraTortuguita.color('green')
otraTortuguita.left(90)
otraTortuguita.fd(50)
otraTortugita.speed(5)