import pygame

pygame.init()
pantalla = pygame.display.set_mode((600, 600))
reloj = pygame.time.Clock()
salir = False

# Paso 1. Obtenemos la fuente
tipos = pygame.font.get_fonts()
letra = 'montserrat'
tipo_letra = None
if letra not in tipos:
    letra = pygame.font.get_default_font()
tipo_letra = pygame.font.SysFont(letra, 60, True, False)

# Paso 2. Preparamos el texto
texto = '3    9'

# Paso 3. Convertir el texto usando la tipografía en una imagen (píxeles)
img_texto = tipo_letra.render(texto, False, (100, 180, 0))
img_texto2 = tipo_letra.render('hola', True, (180, 180, 0))

while not salir:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            print('Has pulsado el botón de cerrar la ventana')
            salir = True

    pantalla.fill((0, 0, 100))

    # Paso 4. Pintar la imagen en la pantalla
    pantalla.blit(img_texto, (50, 100))
    pantalla.blit(img_texto2, (50, 200))

    pygame.display.flip()
    reloj.tick(15)


pygame.quit()
