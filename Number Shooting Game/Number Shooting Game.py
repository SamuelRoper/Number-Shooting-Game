import pygame

#import classes from other files
from Sprite import Sprite
from Crosshair import Crosshair
from Gun import Gun
from Ammo import Ammo
from Bullet import Bullet
from Circles import Circle

# Initialize the game engine
pygame.init()
pygame.font.init()


#define font
tracker_font = pygame.font.SysFont("monospace", 30)

# Define  colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set the height and width of the screen
size = (1800, 1000)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Number Shooting Game")
 
# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

#trackers
score = 0
number_of_bullets = 3
lives = 3
count = 0
reload = False
number_of_circles = 0

#load sprites
gun = pygame.image.load("Sprites/Gun.png")
crosshair = pygame.image.load("Sprites/Crosshair.png")
bullet = pygame.image.load("Sprites/Bullet.png")
ammo_have = pygame.image.load("Sprites/Ammo_left.png")


#create classes
player_crosshair = Crosshair(1, 2, 3, 4, 5, 6, crosshair)
game_gun = Gun(0, 700, 900, gun)
ammo1 = Ammo(1, 2, 3, 4, 600, 930, ammo_have, 1)
ammo2 = Ammo(1, 2, 3, 4, 600, 930, ammo_have, 2)
ammo3 = Ammo(1, 2, 3, 4, 600, 930, ammo_have, 3)
bullet1 = Bullet(10 ,game_gun.get_angle(), 3, 4, 600, 900, bullet)
bullet1.set_alive(False)
bullet2 = Bullet(10 ,game_gun.get_angle(), 3, 4, 600, 900, bullet)
bullet2.set_alive(False)
bullet3 = Bullet(10 ,game_gun.get_angle(), 3, 4, 600, 900, bullet)
bullet3.set_alive(False)
circle1 = Circle()
circle2 = Circle()
circle3 = Circle()


#functions
def update_ammo(ammo1, ammo2, ammo3, number_of_bullets):
    ammo1.update(number_of_bullets)
    ammo2.update(number_of_bullets)
    ammo3.update(number_of_bullets)
    ammo1.draw(screen)
    ammo2.draw(screen)
    ammo3.draw(screen)

def circle_collision(circle, bullet):
    if ((((circle.get_pos_x() - bullet.get_pos_x()) ** 2 + (circle.get_pos_y() - bullet.get_pos_y()) ** 2) ** (1/2)) < 50) and (circle.get_status() == True):
        return(True)
    else:
        return(False)

def check_collisions(circle, bullet1, bullet2, bullet3):
    if (circle_collision(circle, bullet1)) == True or (circle_collision(circle, bullet2)) == True or (circle_collision(circle, bullet3)) == True:
        return(True)
    else:
        return(False)



# Loop as long as done == False and player is not dead
while not done and lives > 0:
 
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN and reload == False:
            if number_of_bullets == 3:
                bullet1.set_alive(True)
                bullet1 = Bullet(12 ,game_gun.get_angle(), 3, 4, 760, 900, bullet)
                number_of_bullets -= 1
            elif number_of_bullets == 2:
                bullet2.set_alive(True)
                bullet2 = Bullet(12 ,game_gun.get_angle(), 3, 4, 760, 900, bullet)
                number_of_bullets -= 1
            elif number_of_bullets == 1:
                bullet3.set_alive(True)
                bullet3 = Bullet(12 ,game_gun.get_angle(), 3, 4, 760, 900, bullet)
                number_of_bullets -= 1

        #reloads when player presses r
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                reload = True
                count = 20
                number_of_bullets = 3
 
    # Clear the screen and set the screen background
    screen.fill(WHITE)

    #delays reload end for 2 seconds:
    count -= 1
    if count <= 0:
        reload = False


    #if there are less than 3 circles, a circle will be spawned
    if not circle1.get_status() and number_of_circles < 3:
        circle1 = Circle()
        circle1.set_alive(True)
        number_of_circles += 1

    if not circle2.get_status() and number_of_circles < 3:
        circle2 = Circle()
        circle2.set_alive(True)
        number_of_circles += 1

    if not circle1.get_status() and number_of_circles < 3:
        circle3 = Circle()
        circle3.set_alive(True)
        number_of_circles += 1


    #check circles are inside window
    if (not circle1.check_inside_window()) or (not circle2.check_inside_window()) or (not circle3.check_inside_window()):
        number_of_circles -= 1
        lives -= 1

    #if a circle collides with a bullet
    collision1 = check_collisions(circle1, bullet1, bullet2, bullet3)
    collision2 = check_collisions(circle2, bullet1, bullet2, bullet3)
    collision3 = check_collisions(circle3, bullet1, bullet2, bullet3)

    if collision1 == True:
        circle1.set_alive(False)
        score += 1
        number_of_circles -= 1
    elif collision2 == True:
        circle2.set_alive(False)
        score += 1
        number_of_circles -= 1
    elif collision3 == True:
        circle3.set_alive(False)
        score += 1
        number_of_circles -= 1



    #tracks the scores and lives
    score_tracker = tracker_font.render("Score: " + str(score), 1, BLACK)
    life_tracker = tracker_font.render("Lives: " + str(lives), 1, BLACK)


    #draws crosshair to screen
    player_crosshair.update()
    player_crosshair.draw(screen)

    #draws gun to screen
    game_gun.draw(screen)

    #draw ammo to screen
    update_ammo(ammo1, ammo2, ammo3, number_of_bullets)

    #draw circles to screen when spawned
    circle1.update()
    circle2.update()
    circle3.update()
    circle1.draw(screen)
    circle2.draw(screen)
    circle3.draw(screen)

    #draws bullets to screen when fired
    bullet1.update()
    bullet1.draw(screen)
    bullet2.update()
    bullet2.draw(screen)
    bullet3.update()
    bullet3.draw(screen)

    screen.blit(score_tracker, (1600, 50))
    screen.blit(life_tracker, (1600, 20))

    #Update the screen with what we've drawn.
    #This MUST happen after all the other drawing commands.
    pygame.display.flip()
 
    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(60)
 
# Be IDLE friendly
pygame.quit()