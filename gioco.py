from pgzero.actor import Actor
from pgzero.clock import clock
from random import randint
import pgzrun

TITLE = "Colpisci l'alieno"
WIDTH = 800
HEIGHT = 600

messaggio = ""
punteggio = 0
vite = 3
game_over = False
punteggio_finale = 0
countdown = 10  # variabile per il conto alla rovescia dopo Game Over

alieno = Actor("alieno")

def draw():
    screen.clear()
    screen.fill(color=(204,255,0))
    
    if game_over:
        screen.fill(color=(204,0,0))
        screen.draw.text("GAME OVER", center=(WIDTH/2, HEIGHT/2 - 70), fontsize=100, color="red")
        screen.draw.text(f"Punteggio ottenuto: {punteggio_finale}", center=(WIDTH/2, HEIGHT/2 + 10), fontsize=60, color="black")
        screen.draw.text(f"Nuova partita fra {countdown} secondi...", center=(WIDTH/2, HEIGHT/2 + 100), fontsize=40, color="black")
    else:
        alieno.draw()
        screen.draw.text(messaggio, center=(400, 40), fontsize=60)
        screen.draw.text(f"Punteggio: {punteggio}", topleft=(10, 10), fontsize=40, color="black")
        screen.draw.text(f"Vite: {vite}", topright=(WIDTH - 10, 10), fontsize=40, color="black")

def piazza_alieno():
    if not game_over:
        alieno.x = randint(50, WIDTH - 50)
        alieno.y = randint(50, HEIGHT - 50)
        alieno.image = "alieno"
        
def on_mouse_down(pos):
    global messaggio, punteggio, vite, game_over, punteggio_finale, countdown
    if game_over:
        return
    
    if alieno.collidepoint(pos):
        messaggio = "Uhia!"
        alieno.image = "esplosione"
        punteggio += 1
    else:
        messaggio = "Stoikhenion"
        vite -= 1
        if vite <= 0:
            game_over = True
            messaggio = ""
            punteggio_finale = punteggio
            countdown = 10
            clock.schedule(countdown_tick, 1.0)  # avvia il conto alla rovescia ogni secondo

def countdown_tick():
    global countdown
    countdown -= 1
    if countdown <= 0:
        reset_gioco()
    else:
        clock.schedule(countdown_tick, 1.0)

def reset_gioco():
    global punteggio, vite, game_over, messaggio
    punteggio = 0
    vite = 3
    game_over = False
    messaggio = "Nuova partita!"
    piazza_alieno()

piazza_alieno()
clock.schedule_interval(piazza_alieno, 0.8)
pgzrun.go()

