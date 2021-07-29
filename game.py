import pygame as pg

tamanno = (800, 600)

class Bola():

    def __init__(self, x, y, w, h, color = (255, 255, 255)):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
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
        
class Game():

    def __init__(self, tamanno):
        self.pantalla = pg.display.set_mode(tamanno)
        self.reloj = pg.time.Clock() #limitar a x fps

    def bucle_ppal(self):
        bola = Bola(tamanno[0]//2-10, tamanno[1]//2-10, 20, 20)
        game_over = False
        pg.init()
        mov = False
        while not game_over:
            self.reloj.tick(60) #limita a 60 fps
            eventos = pg.event.get()
            for evento in eventos:
                if evento.type == pg.QUIT:
                    game_over =True
            
            bola.actualizar()            

            self.pantalla.fill((0, 0, 0))
            pg.draw.rect(self.pantalla, bola.color, pg.Rect(bola.x, bola.y, bola.w, bola.h))

            pg.display.flip()
            
        pg.quit()

#if __name__== "__main__":
juego = Game(tamanno)
juego.bucle_ppal()