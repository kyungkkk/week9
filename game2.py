import pygame # 1. pygame 선언
import random

pygame.init() # 2. pygame 초기화

# 3. pygame에 사용되는 전역변수 선언

BLACK = (0, 0, 0)
size = [600, 800]
screen = pygame.display.set_mode(size)

done = False
clock = pygame.time.Clock()

# 4. pygame 무한루프
def runGame():
    global done
    while not done:
        clock.tick(10)
        screen.fill(BLACK)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True
        
        pygame.display.update()

runGame()
pygame.quit()

def runGame():
    bomb_image = pygame.image.load('bomb.png')
    bomb_image = pygame.transform.scale(bomb_image, (50, 50))
    bombs = []
 
    for i in range(5):
        rect = pygame.Rect(bomb_image.get_rect())
        rect.left = random.randint(0, size[0])
        rect.top = -100
        dy = random.randint(3, 9) ## 떨어지는 속도
        bombs.append({'rect': rect, 'dy': dy})

person_image = pygame.image.load('person.png')
person_image = pygame.transform.scale(person_image, (100, 100))
person = pygame.Rect(person_image.get_rect())
person.left = size[0] // 2 - person.width // 2
person.top = size[1] - person.height
person_dx = 0
person_dy = 0
