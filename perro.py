class Perro(): #siempre empieza por mayuscula
    def __init__(self, nombre, edad, peso): #instanciarlo con la funcion constructura. clase vacia self y le va añadiendo atributos. FUNCIÓN CONSTRUCTOR. Permiti crear la instancia
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
    
    def ladrar(self): #primer parametro siempre hay que introducrilo. primer parametro (instancia del objeto) de los métodos de una clase siempre es la propia clase
        if self.peso >= 8:
            print('GUAU, GUAU')
        else:
            print("guau, guau")
    
    def __str__(self): #definir una cadena: Conviene definirlo para en el momento de print la variable tener toda los atributos y así no ver la direccion de memoria
        return "Soy el perro {}".format(self.nombre)

class PerroAsistencia(Perro): #subclase de perro. llamamos a la clase perro
    trabajando = False
    
    def __init__(self, nombre, edad, peso, amo): #inicializamos con un nuevo atributo (amo), pero llamamos al constructor de la clase perro
        Perro.__init__(self, nombre, edad, peso)
        self.amo = amo
    
    def __str__(self):
        return "Perro de asistencia de {}".format(self.amo)
   
    def pasear(self):
        print("{} ayudo a mi dueño, {}".format(self.nombre, self.amo))
        
    def ladrar(self): #sobreescribir un metodo, ya que la clase perro tenía ese metodo.
        if self.trabajando:
            print("shh, no puedo ladrar")
        else:
            Perro.ladrar(self)