import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

ball_speed = [6, 6]
ball_size = 20
ball = pygame.Rect(WIDTH//2 - ball_size//2, HEIGHT//2 - ball_size//2, ball_size, ball_size)

paddle_width, paddle_height = 10, 100
paddle_speed = 10
paddle1 = pygame.Rect(30, HEIGHT//2 - paddle_height//2, paddle_width, paddle_height)
paddle2 = pygame.Rect(WIDTH - 40, HEIGHT//2 - paddle_height//2, paddle_width, paddle_height)

score1 = 0
score2 = 0
font = pygame.font.Font(None, 74)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and paddle1.top > 0:
        paddle1.move_ip(0, -paddle_speed)
    if keys[pygame.K_DOWN] and paddle1.bottom < HEIGHT:
        paddle1.move_ip(0, paddle_speed)

    # Mouvement de l'IA 
    if paddle2.centery < ball.centery and paddle2.bottom < HEIGHT:
        paddle2.move_ip(0, paddle_speed)
    if paddle2.centery > ball.centery and paddle2.top > 0:
        paddle2.move_ip(0, -paddle_speed)

    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    # Collision avec le haut et le bas de l'écran
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed[1] = -ball_speed[1]

    # Collision avec les raquettes
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_speed[0] = -ball_speed[0] * 1.2


    # Sortir de l'écran (gauche ou droite)
    if ball.left <= 0:
        score2 += 1
        ball = pygame.Rect(WIDTH//2 - ball_size//2, HEIGHT//2 - ball_size//2, ball_size, ball_size)
        ball_speed = [6, 6] if ball_speed[0] > 0 else [-6, 6]
    elif ball.right >= WIDTH:
        score1 += 1
        ball = pygame.Rect(WIDTH//2 - ball_size//2, HEIGHT//2 - ball_size//2, ball_size, ball_size)
        ball_speed = [6, 6] if ball_speed[0] > 0 else [-6, 6]

    # Affichage
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, paddle1)
    pygame.draw.rect(screen, WHITE, paddle2)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    # Afficher les scores
    score_text1 = font.render(str(score1), True, WHITE)
    score_text2 = font.render(str(score2), True, WHITE)
    screen.blit(score_text1, (WIDTH//4 - score_text1.get_width()//2, 20))
    screen.blit(score_text2, (3*WIDTH//4 - score_text2.get_width()//2, 20))

    pygame.display.flip()
    pygame.time.Clock().tick(60)
