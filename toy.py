import pygame
import math

# Inicializar o Pygame
pygame.init()

# Configuração da janela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Boneco Anatômico em Movimento")

# Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Função para desenhar o boneco
def draw_boneco(surface, angle):
    center_x, center_y = screen_width // 2, screen_height // 2

    # Cabeça
    pygame.draw.circle(surface, WHITE, (center_x, center_y - 100), 20)

    # Tronco
    pygame.draw.line(surface, WHITE, (center_x, center_y - 60), (center_x, center_y + 20), 41)
    pygame.draw.circle(surface, WHITE, (center_x, center_y - 60), 21)
    pygame.draw.circle(surface, WHITE, (center_x, center_y + 30), 21)
    # Braços (esquerdo e direito)
    arm_length = 60
    forearm_length = 50

    # Cálculo do movimento dos braços
    arm_angle = math.radians(angle)

    # Braço esquerdo
    left_shoulder = (center_x, center_y - 60)
    left_elbow = (
        center_x + int(math.cos(arm_angle) * arm_length),
        center_y - 60 + int(math.sin(arm_angle) * arm_length)
    )
    left_hand = (
        left_elbow[0] + int(math.cos(arm_angle + math.pi / 2) * forearm_length),
        left_elbow[1] + int(math.sin(arm_angle + math.pi / 2) * forearm_length)
    )
    pygame.draw.line(surface, WHITE, left_shoulder, left_elbow, 8)
    pygame.draw.line(surface, WHITE, left_elbow, left_hand, 8)

    # Braço direito
    right_shoulder = (center_x, center_y - 60)
    right_elbow = (
        center_x - int(math.cos(arm_angle) * arm_length),
        center_y - 60 + int(math.sin(arm_angle) * arm_length)
    )
    right_hand = (
        right_elbow[0] - int(math.cos(arm_angle + math.pi / 2) * forearm_length),
        right_elbow[1] + int(math.sin(arm_angle + math.pi / 2) * forearm_length)
    )
    pygame.draw.line(surface, WHITE, right_shoulder, right_elbow, 8)
    pygame.draw.line(surface, WHITE, right_elbow, right_hand, 8)

    # Pernas
    leg_length = 80
    pygame.draw.line(surface, WHITE, (center_x-15, center_y + 30), (center_x - 15, center_y + 50 + leg_length), 9)
    pygame.draw.line(surface, WHITE, (center_x+15, center_y + 30), (center_x + 15, center_y + 50 + leg_length), 9)

# Loop principal
running = True
clock = pygame.time.Clock()
angle = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Atualizar ângulo
    angle = (angle + 2) % 360

    # Preencher o fundo
    screen.fill(BLACK)

    # Desenhar o boneco
    draw_boneco(screen, angle)

    # Atualizar a tela
    pygame.display.flip()

    # Controlar a taxa de quadros
    clock.tick(60)

# Sair do Pygame
pygame.quit()

