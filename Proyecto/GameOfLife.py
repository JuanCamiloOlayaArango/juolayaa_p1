#Importar módulos
import pygame
import numpy as np
import time
import tkinter

#Establecemos resolución
NX = 0
NY = 0
Ancho = 0
Alto = 0
Descanso = 0.1
def main():
    """
    Inicia los parámetros de la ventana de configuración
    """
    #Ventana inicial
    ventana_inicio = tkinter.Tk()
    ventana_inicio.geometry("600x600")
    ventana_inicio.title("Game of life")
    #Elementos
    in_ancho = tkinter.Entry(ventana_inicio)
    in_alto = tkinter.Entry(ventana_inicio)
    in_nX = tkinter.Entry(ventana_inicio)
    in_nY = tkinter.Entry(ventana_inicio)
    show(ventana_inicio, in_ancho, in_alto, in_nX, in_nY)

    #Función de inicio
def Iniciar(in_nX, in_nY, in_ancho, in_alto, ventana_inicio):
    """
    Asigna los valores ingresados e inicia el juego.

    :param Tk ventana_inicio: ventana inicial.
    :param Entry in_ancho: Entrada del ancho de la ventana.
    :param Entry in_alto: Entrada del alto de la ventana.
    :param Entry in_nX: Entrada del ancho de la rejilla.
    :param Entry in_nY: Entrada del alto de la rejilla.
    """
    global NX
    NX = int(in_nX.get())
    global NY
    NY = int(in_nY.get())
    global Ancho
    Ancho = int(in_ancho.get())
    global Alto
    Alto = int(in_alto.get())
    ventana_inicio.destroy()
    dimen(NX, NY, Ancho, Alto)

def show(ventana_inicio, in_ancho, in_alto, in_nX, in_nY):
    """
    Crea la ventana inicial con los parámetros dados.

    :param Tk ventana_inicio: ventana inicial.
    :param Entry in_ancho: Entrada del ancho de la ventana.
    :param Entry in_alto: Entrada del alto de la ventana.
    :param Entry in_nX: Entrada del ancho de la rejilla.
    :param Entry in_nY: Entrada del alto de la rejilla.
    """
    #Objetos de la ventana
    inicio = lambda: Iniciar(in_nX, in_nY, in_ancho, in_alto, ventana_inicio)
    titulo = tkinter.Label(ventana_inicio, text = "El juego de la vida")
    Res = tkinter.Label(ventana_inicio, text = "Resolución")
    Anch = tkinter.Label(ventana_inicio, text = "Ancho")
    Alt = tkinter.Label(ventana_inicio, text = "Alto")
    RX = tkinter.Label(ventana_inicio, text = "Rejilla horizontal")
    RY = tkinter.Label(ventana_inicio, text = "Rejilla vertical")
    StarButton = tkinter.Button(ventana_inicio, text = "Crear", command = inicio)
    titulo.pack()
    Res.pack()
    Anch.pack()
    in_ancho.pack()
    Alt.pack()
    in_alto.pack()
    RX.pack()
    in_nX.pack()
    RY.pack()
    in_nY.pack()
    StarButton.pack()

    ventana_inicio.mainloop()

def dimen(NX, NY, Ancho, Alto):
    """
    Establece las dimensiones de la ventana de juego

    :param int Ancho: Ancho de la ventana.
    :param int Alto: Alto de la ventana.
    :param int NX: Ancho de la rejilla.
    :param int NY: Alto de la rejilla.
    """
    #Dimensiones
    if Ancho < 1 or Alto < 1:
        Ancho = 600
        Alto = 600
    ancho, alto = Ancho, Alto
    if NX < 1 or NY < 1:
        NX = 50
        NY = 50
    xSize = ancho/NX
    ySize = alto/NY
    inicio(ancho, alto, NX, NY, xSize, ySize)

def inicio(ancho, alto, nX, nY, xSize, ySize):
    """
    Inicia la ventana de juego

    :param int ancho: Ancho de la ventana.
    :param int alto: Alto de la ventana.
    :param int nX: Ancho de la rejilla.
    :param int nY: Alto de la rejilla.
    :param int xSize: Ancho de la celda.
    :param int ySize: Alto de la celda.
    """
    pygame.init() # Iniciamos Pygame

    screen = pygame.display.set_mode([ancho,alto]) # Definimos tamaño de la pantalla

    bg_color   = (0,0,0) # Escogemos los colores
    live_color = (255,255,255)
    dead_color = (127,127,127)
    # Celdas vivas = 1; Celdas muertas = 0
    estado = np.zeros((nX,nY)) # Iniciar estatus de las celdas
    Game(xSize, ySize, nX, nY, screen, bg_color, live_color, dead_color, estado)

def Game(xSize, ySize, nX, nY, screen, bg_color, live_color, dead_color, estado):
    """
    Inicia el juego

    :param tuple bg_color: Color de fondo.
    :param tuple live_color: Color de celdas vivas.
    :param tuple dead_color: Color de celdas muertas.
    :param list estado: Matriz del estrado de las celdas.
    :param int nX: Ancho de la rejilla.
    :param int nY: Alto de la rejilla.
    :param int xSize: Ancho de la celda.
    :param int ySize: Alto de la celda.
    :param Module screen: ventana de juego.
    """
    Pausa = False

    run = True
    while run:

        nuevo_estado = np.copy(estado) # Copiar estado
        Descanso = 0

        for i in pygame.event.get():   #Definimos controles
            if i.type == pygame.QUIT:   #Cerrar el juego
                run = False

            if i.type == pygame.KEYDOWN:    #Presionar teclas para pausar
                Pausa = not Pausa
            
            Click = pygame.mouse.get_pressed()  #Registramos los botones del ratón
            if (Click[0] + Click[1] + Click[2]) > 0:
                pX, pY = pygame.mouse.get_pos() #Obtenemos la posición del ratón
                x, y = int(pX/xSize), int(pY/ySize) #Rastreamos celda de esas coordenadas
                nuevo_estado[x,y] = not Click[2]    #Modificamos esa celda

        screen.fill(bg_color) # Vaciamos la pantalla

        for x in range(nX):
            for y in range(nY):


                if not Pausa:
                    Descanso = 0.5
                    # Numero de vecinos
                    nN = estado[(x-1)%nX,(y-1)%nY] + estado[(x)%nX,(y-1)%nY] + \
                         estado[(x+1)%nX,(y-1)%nY] + estado[(x-1)%nX,(y)%nY] + \
                         estado[(x+1)%nX,(y)%nY] + estado[(x-1)%nX,(y+1)%nY] + \
                         estado[(x)%nX,(y+1)%nY] + estado[(x+1)%nX,(y+1)%nY]

                    # Regla 1: Una celula muerta con 3 vecinas revive
                    if estado[x,y] == 0 and nN==3:
                        nuevo_estado[x,y] = 1

                    # Regla 2: Una celula viva con mas de 3 vecinos o menos de 2 muere
                    elif estado[x,y] == 1 and (nN < 2 or nN > 3):
                        nuevo_estado[x,y] = 0

                poly = [(x*xSize,y*ySize), #Puntos del polígono
                        ((x+1)*xSize,y*ySize),
                        ((x+1)*xSize,(y+1)*ySize),
                        (x*xSize,(y+1)*ySize)]

                if nuevo_estado[x,y] == 1: #Dibujamos el relleno de cada celda
                    pygame.draw.polygon(screen,live_color,poly,0)
                else:
                    pygame.draw.polygon(screen,dead_color,poly,1)

        estado = np.copy(nuevo_estado)
        pygame.display.flip()
        time.sleep(Descanso)

    pygame.quit()

main()