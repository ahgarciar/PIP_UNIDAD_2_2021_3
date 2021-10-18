from ClicImagenes.QLabelClickeable import clickable

import sys

from PyQt5 import uic, QtWidgets, QtGui, QtCore

qtCreatorFile = "P10_Encuentra_el_Numero.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals

        self.diccionarioImagenes = {}
        self.diccionarioImagenes[1] = ":/NUMEROS/UNO"
        self.diccionarioImagenes[2] = ":/NUMEROS/DOS"
        self.diccionarioImagenes[3] = ":/NUMEROS/TRES"
        self.diccionarioImagenes[4] = ":/NUMEROS/CUATRO"
        self.diccionarioImagenes[5] = ":/NUMEROS/CINCO"


        self.diccionarioPreguntas = {}

        ##                         enunciado , respCorrecta, opciones
        #                   index:    0        1       2
        self.diccionarioPreguntas[0] = ["Numero 1", 1, [1, 2, 3, 4]]   #pregunta 0
        self.diccionarioPreguntas[1] = ["Numero 2", 2, [1, 2, 3, 5]]   #pregunta 1
        self.diccionarioPreguntas[2] = ["Numero 3", 3, [5, 2, 3, 4]]   #
        self.diccionarioPreguntas[3] = ["Numero 4", 4, [1, 5, 3, 4]]   #
        self.diccionarioPreguntas[4] = ["Numero 5", 5, [1, 4, 3, 5]]   #pregunta 4

        #desordenar


        ##CARGAR LAS IMAGENES EN LOS LABELS
        self.clavePregunta = 0   #numero de la prgunta actual

        self.cargarImagenes()

        self.IndexRespUsu = -1


        clickable(self.img_a).connect(self.imagenA)
        clickable(self.img_b).connect(self.imagenB)
        clickable(self.img_c).connect(self.imagenC)
        clickable(self.img_d).connect(self.imagenD)

        self.btn_enviar.clicked.connect(self.validarEnviar)


    #area de slots
    def validarEnviar(self):
        pregunta = self.diccionarioPreguntas[self.clavePregunta]

        indexBuscado = 1  # respCorrecta

        respCorrecta = pregunta[indexBuscado]

        indexBuscado = 2  # posibles respuestas
        posiblesRespuestasPregunta = pregunta[indexBuscado]  # una lista con 4 opciones

        numRespUsuario = posiblesRespuestasPregunta[self.IndexRespUsu]

        if respCorrecta == numRespUsuario:
            print("Respuesta Correcta")
        else:
            print("Respuesta Incorrecta")

        self.clavePregunta += 1
        self.cargarImagenes()


    def cargarImagenes(self):
        pregunta = self.diccionarioPreguntas[self.clavePregunta]
        print(pregunta)  # index 0: Nombre   index 1: respCorrecta   index 2: posibles respuesta

        indexBuscado = 0  # nombre
        self.txt_Nombre.setText(pregunta[indexBuscado])

        indexBuscado = 2  # posibles respuestas
        posiblesRespuestasPregunta = pregunta[indexBuscado]  # una lista con 4 opciones

        ##opcion 1
        index_posibleResp = 0  # se desea la primera opcion de respuesta
        numImagenDeseada = posiblesRespuestasPregunta[index_posibleResp]
        auxNombreImg = self.diccionarioImagenes[numImagenDeseada]
        # print(auxNombreImg)
        self.img_a.setPixmap(QtGui.QPixmap(auxNombreImg))

        ##opcion 2
        index_posibleResp = 1  # se desea la primera opcion de respuesta
        numImagenDeseada = posiblesRespuestasPregunta[index_posibleResp]
        auxNombreImg = self.diccionarioImagenes[numImagenDeseada]
        # print(auxNombreImg)
        self.img_b.setPixmap(QtGui.QPixmap(auxNombreImg))

        ##opcion 3
        index_posibleResp = 2  # se desea la primera opcion de respuesta
        numImagenDeseada = posiblesRespuestasPregunta[index_posibleResp]
        auxNombreImg = self.diccionarioImagenes[numImagenDeseada]
        # print(auxNombreImg)
        self.img_c.setPixmap(QtGui.QPixmap(auxNombreImg))

        ##opcion 4
        index_posibleResp = 3  # se desea la primera opcion de respuesta
        numImagenDeseada = posiblesRespuestasPregunta[index_posibleResp]
        auxNombreImg = self.diccionarioImagenes[numImagenDeseada]
        # print(auxNombreImg)
        self.img_d.setPixmap(QtGui.QPixmap(auxNombreImg))

        ######################################

    def imagenA(self):
        self.IndexRespUsu  = 0
        self.txt_opcion_usuario.setText("A")
        print("A")

    def imagenB(self):
        self.IndexRespUsu = 1
        self.txt_opcion_usuario.setText("B")
        print("B")

    def imagenC(self):
        self.IndexRespUsu = 2
        self.txt_opcion_usuario.setText("C")
        print("C")

    def imagenD(self):
        self.IndexRespUsu = 3
        self.txt_opcion_usuario.setText("D")
        print("D")


    def mensaje(self,msj):
        m = QtWidgets.QMessageBox()
        m.setText(msj)
        m.exec_()

        #ejercicio: añadir la funcionalidad del programa 9 al resto de las categorias

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


