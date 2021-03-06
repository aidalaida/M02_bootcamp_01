import pygame, sys
from pygame.locals import * #para importa las eventos de pygame
import random

class Runner(): #crear un objeto y lo utilizamos a lo largo de')
    __customes = ('turtle', 'fish', 'prawn', 'moray', 'octopus')
    
    def __init__(self, x=0, y=0):
        
        ixCustome = random.randint(0,4)
        
        self.custome = pygame.image.load("images/{}.png".format(self.__customes[ixCustome]))
        self.position = [x,y] #como lo queremos mutable es una lista no tupla
        self.name = ""
        
class Game():
    def __init__(self):
        self.__screen = pygame.display.set_mode((640, 480))
        self.__background = pygame.image.load("images/background.png")
        pygame.display.set_caption("Carrera de bichos")
        
        self.runner = Runner(320,240)
        
    def start(self):
        gameOver = False

        while not gameOver: #hasta que haya un ganador
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_UP:
                        self.runner.position[1] -= 5 #en la Y cuando subes tienes que restar
                    elif event.key == K_DOWN :
                        self.runner.position[1] +=5 #en la Y cuando najas tienes que sumar
                    elif event.key == K_LEFT:
                        self.runner.position[0] -=5
                    elif event.key == K_RIGHT:
                        self.runner.position[0] +=5
                    else:
                        pass
            #Pimero carga el fondo y luego al jugador
            self.__screen.blit(self.__background, (0,0)) #para que no deja sombra 
            self.__screen.blit(self.runner.custome, self.runner.position)
         
            pygame.display.flip() #Luego refresca. No deja una traza de tortugas

if __name__ == '__main__':
    game = Game()
    pygame.init() #el font es opcional, puede no ponerlo
    game.start()