import random # Importerer det som er nødvendig
import pygame
pygame.init() # initialiser alle importerte pygamemoduler

win = pygame.display.set_mode((500, 500)) # Setter størrelsen av vinduet til 500x500 pixler

pygame.display.set_caption("Philippe sin jakt etter dessert") # Kaller spillet "Philippe sin jakt etter dessert"

walkRight = pygame.image.load("3.png") # Importerer alle bildene jeg trenger, alle er laget av meg untatt bakgrunnen
walkLeft = pygame.image.load("2.png")
walkUp = pygame.image.load("4.png")
walkDown = pygame.image.load("1.png")
bg = pygame.image.load("bakgrunn.jpg")
char = pygame.image.load("1.png")
kake = pygame.image.load("kake.png")

clock = pygame.time.Clock() # Se linje 94

class Spiller(): # Lager en class for spiller, definerer alle variabler jeg trenger
    def __init__(self, x, y):
        self.x = x # Definerer x- og y-verdi
        self.y = y
        self.vel = 5 # Setter fart til 5
        self.left = False # Definerer alle retninger og setter de til False
        self.right = False
        self.up = False
        self.down = False
        self.rect = char.get_rect() # Henter størrelser fra bildet
        self.width = char.get_width()
        self.height = char.get_height()

    def draw(self,win): # Fikser tegningen av Philippe så riktig bildet vises når man beveger seg
        if self.left:
            win.blit(walkLeft, (self.x,self.y))

        elif self.right:
            win.blit(walkRight, (self.x,self.y))

        elif self.up:
            win.blit(walkUp, (self.x,self.y))

        elif self.down:
            win.blit(walkDown, (self.x,self.y))

        else:
            win.blit(char, (self.x,self.y))

        self.rect.center = (self.x-5, self.y+10) # Fikser hitboxen til Philippe, endret litt på den fordi den passet ikke helt

class Mat(): # Lager en class for muffin, definerer alle variabler jeg trenger
    def __init__(self):
        self.update() # Updater muffin så den får en x- og y-verdi som er tilfeldig, se linje 65
        self.rect = kake.get_rect() # Henter størrelser fra bildet
        self.width = kake.get_width()
        self.height = kake.get_height()

    def draw(self,win):
        win.blit(kake, (self.x, self.y)) # Gjør sånn at muffin blir tegnet inn på riktig sted
        self.rect.center = (self.x, self.y) # Setter sånn at hitboxen følger muffinen

    def collision(self,player_hitbox): # Gjør sånn at hvis muffin og Philippe kolliderer updater muffin posisjonen sin
        if pygame.Rect.colliderect(self.rect,player_hitbox):
            self.update()

    def update(self): # Definerer sånn at når muffin får ny posisjon velges en tilfeldig x- og y-verdi mellom 50 og 450
        self.x = random.randint(50,450)
        self.y = random.randint(50,450)
        score.score += 1 # Når muffinen updater (AKA du treffer den) legges det til en score

class Score(): # Lager en class for score, definerer alle variabler jeg trenger
    def __init__(self,font):
        self.font = font # Definerer fonten
        self.score = -1 # Setter start-scoren som -1 fordi muffinen oppdateres en gang på starten

    def draw(self,win): # Definerer hvordan scoren skal bli tegnet inn
        self.text = self.font.render(f'score: {self.score}', True, (255,255,255), (0,0,0)) # Setter fargene til svart og hvit
        win.blit(self.text, (0,0))

def redrawGameWindow(): # Alt som trengs tegnes inn i spillet
    win.blit(bg, (0,0))
    man.draw(win)
    mat.draw(win)
    mat.collision(man.rect)
    score.draw(win)
    pygame.display.update()

font = pygame.font.Font('text.ttf', 22) # Importerer font for score
score = Score(font) # Definerer score som en Score class med font
man = Spiller(250, 250) # definerer man (AKA Philippe) som en Spiller class med x- og y-verdi 250
mat = Mat() # Definerer muffin som en Mat class
run = True # Setter run = True så programmet begynnes

while run:
    clock.tick(25) # setter fps til 25

    for event in pygame.event.get(): # Når spillet lukkes blir run = False og progammet stoppes
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed() # Definerer keys

    if keys[pygame.K_LEFT] and man.x > 0: # Fikser bevegelse til venstre med venstrepil, setter en begrensning med man.x > 0 så man ikke kan gå utenfor vinduet
        man.x -= man.vel # Setter bevegelsesretning venstre i fart vel (Se spiller class)
        man.left = True # Setter man.left til True så spillet viser riktig bilde
        man.right = False
    elif keys[pygame.K_RIGHT] and man.x < 500-man.width: # --II-- 102
        man.x += man.vel
        man.right = True # --II-- 104
        man.left = False
    elif keys[pygame.K_UP] and man.y > 0: # --II-- 102
        man.y -= man.vel
        man.up = True # --II-- 104
        man.down = False
        man.left = False # Måtte sette left og right som false her fordi det oppstod problemer med hvilket bilde som skulle vises
        man.right = False
    elif keys[pygame.K_DOWN] and man.y < 500-man.height: # --II-- 102
        man.y += man.vel
        man.down = True # --II-- 104
        man.up = False
        man.right = False # --II-- 114
        man.left = False
    else:
        man.right = False # Setter alt som False når ingen knapper trykkes
        man.left = False
        man.up = False
        man.down = False

    redrawGameWindow()

pygame.quit()