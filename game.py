import pygame as pg
from random import randrange

tamanno = (800, 600)

class Movil():
    def __init__(self, x, y, h, w, color=(255, 255, 255)):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color

    def actualizar(self):
        pass

    def Dibuja(self, lienzo):
        pg.draw.rect(lienzo, self.color, pg.Rect(self.x, self.y, self.w, self.h))

class Bola(Movil):

    def __init__(self, x, y, color = (255, 255, 255)):
        super().__init__(x,y, 20, 20, color) #misma instruccion que la de raqueta Movil.init
   
        self.movHor = True
        self.movVert = True
        self.incremento_x = 5
        self.incremento_y = 5
    
    def actualizar(self):
        """    
        if self.movHor == True:  
            if self.x < tamanno[0]-self.w:
                self.x +=1
            else:
                self.movHor = False
        else:
            if self.x  >  0:
                self.x -=1
            else:
                self.movHor = True

        if self.movVert == True:  
            if self.y < tamanno[1]-self.h:
                self.y +=1
            else:
                self.movVert = False
        else:
            if self.y  >  0:
                self.y -=1
            else:
                self.movVert = True
        """    
        self.x += self.incremento_x
        self.y += self.incremento_y
        
        if self.x + 20 > tamanno[0] or self.x < 0:
            self.incremento_x *= -1
        
        if self.y + 20 > tamanno[1] or self.y < 0:
            print(self.x)
            print(self.incremento_y)
            self.incremento_y *= -1

class Raqueta(Movil):
    def __init__(self, x, y, color=(255, 255, 255)):
        Movil.__init__(self, x, y, 80, 10, color)
        



class Game():

    def __init__(self, tamanno):
        self.pantalla = pg.display.set_mode(tamanno)
        self.reloj = pg.time.Clock() #limitar a x fps

        self.todos =[]

        self.player1 = Raqueta(30,(tamanno[1]//2)-40)
        self.player2 = Raqueta(tamanno[0]-30,(tamanno[1]//2) -40,)

        self.todos.append(self.player1)
        self.todos.append(self.player2)

        """
        for i in range(10):
            tamanyo = randrange(10, 41)
            bola = Bola(randrange(0, tamanno[0]), randrange(0, tamanno[1]), tamanyo, tamanyo, (randrange(256),randrange(256), randrange(256)))
            
            bola.movHor = randrange(2) == 1
            bola.movVert = randrange(2) == 1

            self.bolas.append(bola)
        """

        bola = Bola(tamanno[0]//2 - 10, tamanno[1]//2-10, (255, 255, 0))
        self.todos.append(bola)

    def bucle_ppal(self):
        game_over = False
        pg.init()

       
        while not game_over:
            self.reloj.tick(60) #limita a 60 fps

            eventos = pg.event.get()
            for evento in eventos:
                if evento.type == pg.QUIT:
                    game_over =True
            
            for movil in self.todos:
                movil.actualizar()

            self.pantalla.fill((0, 0, 0))

            for movil in self.todos:
                movil.Dibuja(self.pantalla)

            pg.display.flip()
            
        pg.quit()

#if __name__== "__main__":
juego = Game(tamanno)
juego.bucle_ppal()