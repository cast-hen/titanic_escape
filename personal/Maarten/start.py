import pygame

w = 500
h = 500
screen = pygame.display.set_mode((w, h),pygame.RESIZABLE)
# screenRect = pygame.Rect(0, 0, w, h)
clock = pygame.time.Clock()
maxFPS = 60
running = True
pygame.init()

circleData = [0, 0, 10, 250 // maxFPS] # x, y, radius, speed pixels/s // maxFPS
r = circleData[2]
circleRect = pygame.Rect((circleData[0] - 10, circleData[1] - 10), (2 * r, 2 * r))
movement = [0, 0] # 0 or 1 (x, y), amount

state = "nothing"

# all object
cube = pygame.Rect(w // 2 - 10, h // 2 - 10, 20, 20) # x, y, width, height
platform = pygame.Rect(0, 400, w, 20)

# movement functions
def movementBorders(objectCoords):
    if objectCoords[0] > w:
        objectCoords[0] -= w
    if objectCoords[0] < 0:
        objectCoords[0] += w
    if objectCoords[1] > h:
        objectCoords[1] -= h
    if objectCoords[1] < 0:
        objectCoords[1] += h
    return objectCoords

def collision(objectCoords, objectRect, state):
    if pygame.Rect.colliderect(cube, objectRect):
        state = "Dead"
    return state

def gravity(objectCoords):
    if objectCoords[1] < platform[1] - objectCoords[2]:
        objectCoords[1] += 1
    return objectCoords

def jump(objectCoords):
    pass


# other functions
def draw():
    screen.fill('black')
    pygame.draw.ellipse(screen, 'white', circleRect)
    pygame.draw.rect(screen, 'white', cube)
    pygame.draw.rect(screen, 'white', platform)


while not state == "Quit":

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state = "Quit"
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                movement = [0, -circleData[3], event.key]
            if event.key == pygame.K_RIGHT:
                movement = [0, circleData[3], event.key]
            if event.key == pygame.K_UP:
                movement = [1, -circleData[3], event.key]
            if event.key == pygame.K_DOWN:
                movement = [1, circleData[3], event.key]
        elif event.type == pygame.KEYUP and movement[2] == event.key:
            movement = None
        if event.type == pygame.MOUSEBUTTONDOWN:
            state = "Nothing"


    if movement is not None:
        circleData[movement[0]] += movement[1]
        circleData = movementBorders(circleData)
    gravity(circleData)
    circleRect = pygame.Rect((circleData[0] - 10, circleData[1] - 10), (2 * r, 2 * r))
    state = collision(circleData, circleRect, state)
    if state == "Dead":
        screen.fill('red')
    else:
        draw()
    pygame.display.flip()
    clock.tick(maxFPS)
quit()