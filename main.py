from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
from sys import exit
import random
import time

x = 800
y = 800
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((x, y))
pygame.display.set_caption('Dino Collector Performance Task')

font = pygame.font.Font('freesansbold.ttf', 100)
smaller_font = pygame.font.Font('freesansbold.ttf', 40)
slightly_smaller_font = pygame.font.Font('freesansbold.ttf', 50)

title_text = font.render('Dino Collector', True, (255, 255, 255))
title_text_rect = title_text.get_rect()
title_text_rect.center = (x // 2, 200)

start_text = smaller_font.render('Press Space to Start', True, (255, 255, 255))
start_text_rect = start_text.get_rect()
start_text_rect.center = (x // 2, 500)

dino_egg = pygame.transform.scale(pygame.image.load('dinosaur_egg.png'), (400, 400)).convert()
dino_egg_rect = dino_egg.get_rect()
dino_egg_rect.center = (x // 2, 300)

my_dino_text = slightly_smaller_font.render('View Dinos', True, (255, 255, 255))
my_dino_text_rect = my_dino_text.get_rect()
my_dino_text_rect.center = (x // 2, 700)

mouse = pygame.mouse.get_pos()

dinos = {
0: ['Allosaurus'], 1: ['Ankylosaurus'], 2: ['Archaeopteryx'], 3: ['Argentinosaurus'], 4: ['Baryonyx'], 5: ['Brachiosaurus'], 6: ['Carnotaurus'], 7: ['Compsognathus'], 8: ['Dilophosaurus'], 9: ['Diplodocus'], 10: ['Edmontonia'], 11: ['Eoraptor'], 12: ['Gallimimus'], 13: ['Giganotosaurus'], 14: ['Gobisaurus'], 15: ['Iguanodon'], 16: ['Maiasaura'], 17: ['Megalosaurus'], 18: ['Micropachycephalosaurus'], 19: ['Microraptor'], 20: ['Nigersaurus'], 21: ['Oviraptor'], 22: ['Pachycephalosaurus'], 23: ['Parasaurolophus'], 24:['Protoceratops'], 25: ['Sarcosuchus'], 26: ['Spinosaurus'], 27: ['Stegosaurus'], 28: ['Styracosaurus'], 29: ['Supersaurus'], 30: ['Therizinosaurus'], 31: ['Triceratops'], 32: ['Troodon'], 33: ['Tyrannosaurus Rex'], 34: ['Utahraptor'], 35: ['Velociraptor'],
36: ['Dimorphodon'], 37: ['Pteranodon'], 38: ['Pterodactylus'], 39: ['Quetzalcoatlus'],
40: ['Dunkleosteus'], 41: ['Elasmosaurus'], 42: ['Helicoprion'], 43: ['Ichthyosaurus'], 44: ['Megalodon'], 45: ['Mosasaurus'], 46: ['Plesiosaurus']
  }

player_dinos = []

game_active = False
last_hatch_time = 0
hatch_text_duration = 5
player_dino_time = 0
player_dino_duration= 5

def hatch_dino(current_dino):
  global last_hatch_time
  global newDino
  hatch_text = smaller_font.render('You hatched a '+ dinos[current_dino][0], True, (255, 255, 255))
  hatch_text_rect = hatch_text.get_rect()
  hatch_text_rect.center = (x // 2, 60)
  screen.blit(hatch_text, hatch_text_rect)
  newDino = dinos[current_dino][0]

  player_dinos.append(newDino)
  last_hatch_time = time.time()
  return newDino


while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()
    if game_active:
      screen.fill((0, 0, 0))
      screen.blit(dino_egg, dino_egg_rect)
      my_dino_button = pygame.draw.rect(screen, (0, 200, 100), pygame.Rect(250, 650, 300, 100))
      screen.blit(my_dino_text, my_dino_text_rect)
      if event.type == pygame.MOUSEBUTTONDOWN:
        if dino_egg_rect.collidepoint(event.pos): 
          hatch_dino(random.randint(0, 46))
        elif my_dino_button.collidepoint(event.pos):
          player_dinos_fixed = str(player_dinos)
          player_dinos_fixed = player_dinos_fixed.replace("[","")
          player_dinos_fixed = player_dinos_fixed.replace("]","")
          player_dinos_fixed = player_dinos_fixed.replace("'","")
          player_dino_time = time.time()
          player_dinos_text = smaller_font.render('Your dinos are: '+ player_dinos_fixed, True, (255, 255, 255))
          player_dinos_text_rect = player_dinos_text.get_rect()
          player_dinos_text_rect.center = (x // 2, 600)
          screen.blit(player_dinos_text, player_dinos_text_rect)
          print(player_dinos_fixed)

          
      if time.time() - last_hatch_time < hatch_text_duration:
        hatch_text = smaller_font.render('You hatched a '+ newDino, True, (255, 255, 255))
        hatch_text_rect = hatch_text.get_rect()
        hatch_text_rect.center = (x // 2, 60)
        screen.blit(hatch_text, hatch_text_rect)
      if time.time() - player_dino_time < player_dino_duration:
        player_dinos_text = smaller_font.render('Your dinos are: '+ player_dinos_fixed, True, (255, 255, 255))
        screen.blit(player_dinos_text, player_dinos_text_rect)

    else: 
      screen.fill((0, 200, 100))
      screen.blit(title_text, title_text_rect)
      screen.blit(start_text, start_text_rect)
      if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        game_active = True

    pygame.display.update()
    clock.tick(60)