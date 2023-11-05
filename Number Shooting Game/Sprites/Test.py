import pygame

 
 
 
class Sprite():
    def __init__(self):
        self.alive = True
            
    def draw(self):
            screen.blit(gun, (100, 10))
 
# Initialize the game engine
pygame.init()
 
# Define  colours
WHITE = (255, 255, 255)

# Set the height and width of the screen
size = (1800, 1000)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("")
 
# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
 
gun = pygame.image.load("Gun.png").convert()
 
gun2 = Sprite()
 
# Loop as long as done == False
while not done:
 
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
 
    
 
    # Clear the screen and set the screen background
    screen.fill(WHITE)
 
    screen.blit(gun, (10, 10))
    gun2.draw()
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()
 
    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(60)
 
# Be IDLE friendly
pygame.quit()