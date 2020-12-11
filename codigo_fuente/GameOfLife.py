#Importar módulos
import pygame
import numpy
import time
import tkinter
from tkinter import ttk
from tkinter import messagebox as msg
def main():
    """
    Inicia los parámetros de la ventana de configuración
    """
    #Ventana inicial
    ventana_inicio = tkinter.Tk()
    ventana_inicio.geometry("500x350")
    ventana_inicio.title("Game of life")
    ventana_inicio.configure(bg = "black")
    #Elementos
    in_ancho = tkinter.Entry(ventana_inicio, bg = "gray", fg = "black", justify = "center")
    in_alto = tkinter.Entry(ventana_inicio, bg = "gray", fg = "black", justify = "center")
    in_nX = tkinter.Entry(ventana_inicio, bg = "gray", fg = "black", justify = "center")
    in_nY = tkinter.Entry(ventana_inicio, bg = "gray", fg = "black", justify = "center")
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
    #Establecemos resolución
    NX = 0
    NY = 0
    Ancho = 0
    Alto = 0
    try:
        NX = int(in_nX.get())
        NY = int(in_nY.get())
        Ancho = int(in_ancho.get())
        Alto = int(in_alto.get())
    except:
        NX = 20
        NY = 20
        Ancho = 600
        Alto = 600
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
    titulo = tkinter.Label(ventana_inicio, text = "El juego de la vida", font = ("Arial bold", 18), bg = "Black", fg = "white")
    Res = tkinter.Label(ventana_inicio, text = "Resolución", font = ("Arial bold", 15), bg = "black", fg = "white")
    Anch = tkinter.Label(ventana_inicio, text = "Ancho", bg = "black", fg = "white")
    Alt = tkinter.Label(ventana_inicio, text = "Alto", bg = "black", fg = "white")
    Rej = tkinter.Label(ventana_inicio, text = "Rejilla", font = ("Arial bold", 15), bg = "black", fg = "white")
    RX = tkinter.Label(ventana_inicio, text = "Rejilla horizontal", bg = "black", fg = "white")
    RY = tkinter.Label(ventana_inicio, text = "Rejilla vertical", bg = "black", fg = "white")
    StarButton = tkinter.Button(ventana_inicio, text = "Crear", command = inicio, bg = "gray", fg = "white")
    Tuto = tkinter.Label(ventana_inicio, text = "Instrucciones: ", font = ("Arial bold", 12), bg = "black", fg = "white")
    Indic = tkinter.Label(ventana_inicio, text = "Pulse las teclas F1, F2, F3 o F4 para guardar \nPulse las teclas 1, 2, 3 o 4 para cargar los respectivos estados guardados \nPulse Escape para cerrar el juego \nPulse espacio para pausar o reanudar el juego \nPulse F para aumentar la velocidad o S para descenderla \nClick izquierdo para añadir una célula y click derecho para borrarla", bg = "black", fg = "white")
    titulo.grid(column = 1, row = 0)
    Res.grid(column = 0, row = 1)
    Anch.grid(column = 0, row = 2)
    in_ancho.grid(column = 1, row = 2)
    Alt.grid(column = 0, row = 3)
    in_alto.grid(column = 1, row = 3)
    Rej.grid(column = 0, row = 4)
    RX.grid(column = 0, row = 5)
    in_nX.grid(column = 1, row = 5)
    RY.grid(column = 0, row = 7)
    in_nY.grid(column = 1, row = 7)
    StarButton.grid(column = 1, row = 8)
    Tuto.grid(column = 1, row = 9)
    Indic.grid(column = 1, row = 10)
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
    estado = numpy.zeros((nX,nY)) # Iniciar estatus de las celdas
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
    save = []
    for i in range(4):
        save.append((estado))
    edit = 0.1
    while run:
        nuevo_estado = numpy.copy(estado) # Copiar estado
        Descanso = 0
        for i in pygame.event.get():   #Definimos controles
            if i.type == pygame.QUIT:   #Cerrar el juego
                run = False

            if i.type == pygame.KEYDOWN:    #Presionar espacio para pausar
                if i.key == pygame.K_SPACE:
                    Pausa = not Pausa
                if i.key == pygame.K_ESCAPE:    #Escape para salir
                    pygame.quit()
                    main()
                if i.key == pygame.K_F1:        #Slots de guardado
                    save[0] = numpy.copy(estado)
                    time.sleep(Descanso)
                if i.key == pygame.K_F2:
                    save[1] = numpy.copy(estado)
                    time.sleep(Descanso)
                if i.key == pygame.K_F3:
                    save[2] = numpy.copy(estado)
                    time.sleep(Descanso)
                if i.key == pygame.K_F4:
                    save[3] = numpy.copy(estado)
                    time.sleep(Descanso)
                if i.key == pygame.K_1 or i.key == pygame.K_KP1:
                    estado = numpy.copy(save[0])
                    nuevo_estado = numpy.copy(save[0])
                    pygame.display.flip()
                    time.sleep(Descanso)
                if i.key == pygame.K_2 or i.key == pygame.K_KP2:
                    estado = numpy.copy(save[1])
                    nuevo_estado = numpy.copy(save[1])
                    pygame.display.flip()
                    time.sleep(Descanso)
                if i.key == pygame.K_3 or i.key == pygame.K_KP3:
                    estado = numpy.copy(save[2])
                    nuevo_estado = numpy.copy(save[2])
                    pygame.display.flip()
                    time.sleep(Descanso)
                if i.key == pygame.K_4 or i.key == pygame.K_KP4:
                    estado = numpy.copy(save[3])
                    nuevo_estado = numpy.copy(save[3])
                    pygame.display.flip()
                    time.sleep(Descanso)
                if i.key == pygame.K_f:             #Controles de velocidad
                    if edit > 0:
                        edit = round(edit, 2)
                        edit -= 0.05
                if i.key == pygame.K_s:
                    if edit < 0.75:
                        edit = round(edit, 2)
                        edit += 0.05
            
            Click = pygame.mouse.get_pressed()  #Registramos los botones del ratón
            if (Click[0] + Click[1] + Click[2]) > 0:
                pX, pY = pygame.mouse.get_pos() #Obtenemos la posición del ratón
                x, y = int(pX/xSize), int(pY/ySize) #Rastreamos celda de esas coordenadas
                nuevo_estado[x,y] = not Click[2]    #Modificamos esa celda

        screen.fill(bg_color) # Vaciamos la pantalla

        for x in range(nX):
            for y in range(nY):


                if not Pausa:
                    Descanso = 0.1
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

        estado = numpy.copy(nuevo_estado)
        pygame.display.flip()
        if not Pausa:
            time.sleep(edit)
        else:
            time.sleep(Descanso)

    pygame.quit()

main()
