import pygame, sys
import random

class Runner(): #crear un objeto y lo utilizamos a lo largo de')
    __customes = ('turtle', 'fish', 'prawn', 'moray', 'octopus')
    
    def __init__(self, x=0, y=0):
        
        ixCustome = random.randint(0,4)
        
        self.custome = pygame.image.load("images/{}.png".format(self.__customes[ixCustome]))
        self.position = [x,y] #como lo queremos mutable es una lista no tupla
        self.name = ""
    
    def avanzar(self):
        self.position[0] += random.randint(1,6)
        
class Game():
    runners = [] #lista con instancias de tipo runner
    __posY = (160, 200, 240, 280)
    __names = ('Speedy', 'Lucero', 'Alonso', 'Torcuata')
    __startLine = -5
    __finishLine = 620
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((640, 480))
        self.__background = pygame.image.load("images/background.png")
        pygame.display.set_caption("Carrera de bichos")
        
        for i in range(4):    
            theRunner = Runner(self.__startLine,self.__posY[i])
            theRunner.name = self.__names[i]
            self.runners.append(theRunner)
    
    def close():
        pygame.quit()
        sys.exit()
        
    def competir(self):
        gameOver = False

        while not gameOver: #hasta que haya un ganador
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True
            
            for runner in self.runners: #solo en el contexto de competir. No self.runner. Pa
                runner.avanzar() #variables que solo existen en el ambito de competir
                
                if runner.position[0] >= self.__finishLine: #condición por la que se acaba la carrera
                    print("{} ha ganado".format(runner.name))
                    gameOver = True
            
            self.__screen.blit(self.__background, (0,0)) #optimizado para coger area de memoria a la coordenada. REFRESCAR LA PANTALLA
            
            for runner in self.runners:
                self.__screen.blit(runner.custome, runner.position) #solo runner en el contexto de competir y en el bucle
            
            pygame.display.flip()
        
        while True: #BUBLE infinito, para que el buffer no se llene, hacemos un bucle para recorrer todos los eventos
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: #pero util el bucle por el quit()
                    self.close()     
        
        
   
if __name__ == '__main__':
    game = Game()
    pygame.font.init()
    game.competir()