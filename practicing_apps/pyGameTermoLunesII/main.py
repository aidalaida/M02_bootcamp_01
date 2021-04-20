import pygame, sys
from pygame.locals import *

class Termometro(): #la clase cuando la mencione si esta debajo de la llamada a la clase, va a decir que no existe
    def __init__(self):
        self.custome = pygame.image.load("images/termo1.png")
        
    def convertir(self, grados, toUnidad):
        resultado = 0
        if toUnidad == 'F':
            resultado = grados * 9/5 + 32
        elif toUnidad == 'C':
            resultado = (grados -32) * 5/9
        else:
            resultado = grados
            
        return "{:10.2f}".format(resultado)

class Selector():
    __tipoUnidad = None
    
    def __init__(self, unidad = 'C'):
        self.__customes = []
        self.__customes.append(pygame.image.load("images/posiF.png"))
        self.__customes.append(pygame.image.load("images/posiC.png"))
        
        self.__tipoUnidad = unidad
    
    def custome(self): #nos devuelva
        if self.__tipoUnidad == 'F':
            return self.__customes[0]
        else:
            return self.__customes[1]
    
    def unidad(self): #Función getter porque hemos creado un atributo privado
        return self.__tipoUnidad
    
    def change(self):
        
        if self.__tipoUnidad == 'F':
            self.__tipoUnidad = 'C'
        else:
            self.__tipoUnidad = 'F'
        
class NumberInput():
    __value = 0 
    __strValue = ''
    __position = [0,0] #x,y
    __size = [0,0] #ancho por alto
    __pointCount = 0
    
    def __init__(self, value= 0):
        self.__font = pygame.font.SysFont("Arial", 24) #Para poner una fuente
        self.value(value)
    
    def on_event(self, event):
        if event.type == KEYDOWN:
            if event.unicode.isdigit() and len(self.__strValue) < 10 or (event.unicode == '.' and self.__pointCount == 0):
                self.__strValue += event.unicode
                self.value(self.__strValue)
                if event.unicode == '.':
                    self.__pointCount += 1
              
            elif event.key == K_BACKSPACE: #Para quitar las la ultima 
                if self.__strValue[-1] == '.': #posicion penultima, paa borrarla
                    self.__pointCount -= 1
                self.__strValue = self.__strValue[:-1] #Con [:-1] lo que haces con el array es que la posicion la deja fuera 
                self.value(self.__strValue)
               
                  

    def render(self): #para renderizarlo
        textBlock = self.__font.render(self.__strValue, True, (74, 74, 74)) #Para renderizar, con un color. consulta fuente y tamaño y hace una foto. DISFRAZ
        rect = textBlock.get_rect() #rectangulo pequeño
        rect.left = self.__position[0]
        rect.top = self.__position[1]
        rect.size = self.__size #rectangulo
        
        return (rect, textBlock)
        
#         #return {
#                 'fondo': rect,            #se puede hacer con un tupla o un diccionario
#                 'texto': textBlock
#             }

#setter para el value

    def value(self, val = None):
        if val == None:
            return self.__value
        else:
            val = str(val)
            try:
                self.__value = float(val)
                self.__strValue = val
                if '.' in self.__strValue:
                    self.__pointCount = 1
                else:
                    self.__pointCount = 0
            except:
                pass
                
          
#GETTER Y SETTER DE LA VARIABLE SIZE
            
    def width(self, val = None):
        if val == None:
            return self.__size[0]
        else:
            try: #para validar la entrada
                self.__size[0] = int(val)
            except:
                pass
    
    def height(self, val = None):
        if val == None:
            return self.__size[1]
        else:
            try:
                self.__size[1] = int(val)
            except:
                pass
    
    def size(self, val= None):
        if val == None:
            return self.__size
        else:
            try:
                self.__size = [int(val[0]), int(val[1])]
            except:
                pass
            
#GETTER Y SETTER DE LA VARIABLE POSICIÓN  
    
    def posX(self, val = None):
        if val == None:
            return self.__position[0]
        else:
            try: #para validar la entrada
                self.__position[0] = int(val)
            except:
                pass
    
    def posY(self, val = None):
        if val == None:
            return self.__position[1]
        else:
            try:
                self.__position[1] = int(val)
            except:
                pass
    
    def pos(self, val= None):
        if val == None:
            return self.__position
        else:
            try:
                self.__position = [int(val[0]), int(val[1])]
            except:
                pass
            
            
class mainApp():
    termometro = None
    entrada = None
    selector = None
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((290, 415))
        pygame.display.set_caption("Termometro")
        self.__screen.fill((244, 236,203)) #para solo poner color. Creo tupla de conlores con RGB 
        
        
        self.termometro = Termometro() #clase termometro lo asigno al atributo de la clase main
        self.entrada = NumberInput()
        self.entrada.pos((106,58))
        self.entrada.size((133,28))
        self.selector = Selector()
        
        
    def __on_close(self):
        pygame.quit()
        sys.exit()
    
    def start(self):
        
        while True:
            for event in pygame.event.get(): #capturar los eventos
                if event.type == QUIT:
                    self.__on_close() #llamas a la funcion on_close (privada)
                    
                self.entrada.on_event(event)
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.selector.change()
                    grados = self.entrada.value()
                    nuevaUnidad = self.selector.unidad()
                    print(nuevaUnidad)
                    temperatura = self.termometro.convertir(grados, nuevaUnidad)
                    print(temperatura)
                    self.entrada.value(temperatura)
                
            #Pintamos el fondo de pantalla y volvemos a pintar cada vez que se mueve el selector
                
            self.__screen.fill((244, 236,203))
            
            #Pintamos el termómetro en su posición
            
            self.__screen.blit(self.termometro.custome, (50, 34)) #foto fija del termometro en su posición
            
            #Pintamos el cuadro de texto            
            
            text = self.entrada.render() #Obtenemos rectángulo blanco y foto de texto lo asignamos a text
            pygame.draw.rect(self.__screen, (255 ,255 , 255), text[0]) #Creamos el rectangulo blanco con sus datos (posicion, tamaño) text [0]
            self.__screen.blit(text[1], self.entrada.pos()) #pintamos la foto del texto (text[1])
            
            #Pintamos el selector
            self.__screen.blit(self.selector.custome(), (112, 153))
            
        
            pygame.display.flip()
                    
if __name__ == '__main__':
    
    pygame.init()
    app = mainApp()
    app.start() #lanzo la instancia