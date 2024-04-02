import pygame
import time
import random

# Inicializar pygame
pygame.init()

# Definir colores
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Definir dimensiones de la ventana
dis_width = 1080
dis_height = 720

# Crear la ventana del juego
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by AsencionCar')

# Configurar el reloj para controlar la velocidad del juego
clock = pygame.time.Clock()

# Tamaño de un bloque de la serpiente y velocidad del juego
snake_block = 10
snake_speed = 15

# Definir estilo de fuente para los mensajes
font_style = pygame.font.SysFont(None, 30)

# Función para mostrar mensajes en la pantalla
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

# Función principal del juego
def gameLoop():
    game_over = False
    game_close = False

    # Posición inicial de la cabeza de la serpiente
    x1 = dis_width / 2
    y1 = dis_height / 2

    # Velocidad inicial de la serpiente
    x1_change = 0
    y1_change = 0

    # Lista para almacenar los segmentos de la serpiente
    snake_List = []
    Length_of_snake = 1

    # Posición inicial de la comida
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    # Definir las coordenadas de la pared
    wall_left = 0
    wall_right = dis_width - snake_block
    wall_top = 0
    wall_bottom = dis_height - snake_block

    # Contador de puntuación
    score = 0

    # Bucle principal del juego
    while not game_over:

        # Bucle para manejar eventos cuando el juego está en pausa
        while game_close == True:
            dis.fill(blue)
            message("Perdiste! Tu puntuación fue: " + str(score) + " Presiona Q para cerrar o C para jugar de nuevo", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # Manejo de eventos del juego
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Verificar si la serpiente choca contra la pared
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        # Mover la serpiente
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        
        # Dibujar la comida
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        
        # Dibujar la pared
        pygame.draw.rect(dis, red, [wall_left, wall_top, dis_width, snake_block])  # Pared superior
        pygame.draw.rect(dis, red, [wall_left, wall_bottom, dis_width, snake_block])  # Pared inferior
        pygame.draw.rect(dis, red, [wall_left, wall_top, snake_block, dis_height])  # Pared izquierda
        pygame.draw.rect(dis, red, [wall_right, wall_top, snake_block, dis_height])  # Pared derecha

        # Almacenar la posición de la cabeza de la serpiente
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        
        # Eliminar el último segmento de la serpiente si ha crecido
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Verificar si la serpiente choca contra su propio cuerpo
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        # Dibujar la serpiente en la pantalla
        for x in snake_List:
            pygame.draw.rect(dis, yellow, [x[0], x[1], snake_block, snake_block])

        # Mostrar la puntuación en tiempo real
        score_font = pygame.font.SysFont(None, 25)
        value = score_font.render("Tu puntuación: " + str(score), True, white)
        dis.blit(value, [0, 0])

        # Actualizar la pantalla
        pygame.display.update()

        # Verificar si la serpiente ha comido la comida
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
            score += 1

        # Controlar la velocidad del juego
        clock.tick(snake_speed)

    # Salir del juego
    pygame.quit()
    quit()

# Iniciar el bucle principal del juego
gameLoop()
