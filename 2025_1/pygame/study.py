import pygame

pygame.init()
WIDTH , HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

piplup_image = pygame.image.load("piplup.png")
piplup_image = pygame.transform.scale(piplup_image, (200, 200)) 

img_rect = piplup_image.get_rect()
x = (WIDTH - img_rect.width) // 2
y = (HEIGHT - img_rect.height) // 2


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0, 0, 0))
    screen.blit(piplup_image, (x, y))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
