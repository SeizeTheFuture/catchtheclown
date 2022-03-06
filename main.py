import pygame
import random

# Initialize pygame
pygame.init()

# Set display surface
WINDOW_WIDTH = 1750
WINDOW_HEIGHT = 700
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Catch the Clown")

# Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

# Set game values
PLAYER_STARTING_LIVES = 5
CLOWN_STARTING_VELOCITY = 3
CLOWN_ACCELERATION = .5

score = 0
player_lives = PLAYER_STARTING_LIVES

clown_velocity = CLOWN_STARTING_VELOCITY
clown_dx = random.choice([-1, 1])
clown_dy = random.choice([-1, 1])

# Set colors
BLUE = (26, 130, 167)
PURPLE = (109, 61, 146)
RED = (229, 56, 73)

# Set font
font = pygame.font.Font("AlloyInk-nRLyO.ttf", 32)
end_font = pygame.font.Font("AlloyInk-nRLyO.ttf", 64)

# Set text
title_text = font.render("Catch the Clown", True, BLUE)
title_rect = title_text.get_rect()
title_rect.topleft = (50, 10)

score_text = font.render("Score: " + str(score), True, RED)
score_rect = score_text.get_rect()
score_rect.topright = ((WINDOW_WIDTH - 50, 10))

lives_text = font.render("Lives: " + str(player_lives), True, RED)
lives_rect = lives_text.get_rect()
lives_rect.topright = ((WINDOW_WIDTH - 50, 50))

game_over_text = end_font.render("Game Over", True, RED, BLUE)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

continue_text = end_font.render("Click Anywhere To Play Again", True, RED, BLUE)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 128)

# Set sound and music
click_sound = pygame.mixer.Sound("click_sound.wav")
click_sound.set_volume(.5)
miss_sound = pygame.mixer.Sound("miss_sound.wav")
miss_sound.set_volume(.5)
pygame.mixer.music.load("ctc_background_music.wav")

# Set images
background_image = pygame.image.load("circusresized.jpg")
background_rect = background_image.get_rect()
background_rect.topleft = (-700, -400)
# Background Attribution
# <a href="https://www.freepik.com/vectors/cirque">Cirque vector created by vectorpouch - www.freepik.com</a>

clown_image = pygame.image.load("clown.png")
clown_rect = clown_image.get_rect()
clown_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

# The main game loop
pygame.mixer.music.play(-1, 0, 0)
running = True
while running:
    # Check to see if the user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # A click is made
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]

            # The clown was clicked
            if clown_rect.collidepoint(mouse_x, mouse_y):
                click_sound.play()
                score += 1
                clown_velocity += CLOWN_ACCELERATION
                previous_directions = (clown_dx, clown_dy)
                while previous_directions == (clown_dx, clown_dy):
                    clown_dx = random.choice([-1, 1])
                    clown_dy = random.choice([-1, 1])
            # The clown was missed
            else:
                miss_sound.play()
                player_lives -= 1

    # Move the clown
    clown_rect.x += clown_dx * clown_velocity
    clown_rect.y += clown_dy * clown_velocity

    # Bounce the clown off the edges of the display
    if clown_rect.right >= WINDOW_WIDTH or clown_rect.left <= 0:
        clown_dx *= -1
    if clown_rect.top <= 0 or clown_rect.bottom >= WINDOW_HEIGHT:
        clown_dy *= -1

    # Blit Background
    display_surface.blit(background_image, background_rect)

    # Update HUD
    score_text = font.render("Score: " + str(score), True, RED)
    lives_text = font.render("Lives: " + str(player_lives), True, RED)

    # Blit HUD
    display_surface.blit(title_text, title_rect)
    display_surface.blit(score_text, score_rect)
    display_surface.blit(lives_text, lives_rect)

    # Check for game over
    if player_lives == 0:
        display_surface.blit(game_over_text, game_over_rect)
        display_surface.blit(continue_text, continue_rect)
        pygame.display.update()
        is_paused = True
        pygame.mixer.music.stop()
        while is_paused:
            for event in pygame.event.get():
                # The player wants to quit
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False
                # The player wants to play again
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    is_paused = False
                    score = 0
                    player_lives = 5
                    clown_velocity = CLOWN_STARTING_VELOCITY
                    clown_dx = random.choice([-1, 1])
                    clown_dy = random.choice([-1, 1])
                    clown_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
                    pygame.mixer.music.play(-1, 0, 0)

    # Blit Assets
    display_surface.blit(clown_image, clown_rect)

    # Update display and tick clock
    pygame.display.update()
    clock.tick(FPS)

# End the game
pygame.quit()
