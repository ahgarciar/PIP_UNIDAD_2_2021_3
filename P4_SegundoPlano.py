import sys

from PyQt5 import uic, QtWidgets, QtGui, QtCore

qtCreatorFile = "P4_SegundoPlano.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.dial.setMinimum(0)
        self.dial.setMaximum(5)
        self.dial.setSingleStep(1)

        self.dial.setValue(0)
        #self.txt_valor.setText("0")

        self.dial.valueChanged.connect(self.valorCambio)

        self.diccionario = {}
        self.diccionario[0] = ["Jorge", "ISC", ":/NUMEROS/UNO"]
        self.diccionario[1] = ["Chris", "IC", ":/NUMEROS/DOS"]
        self.diccionario[2] = ["Jeremias", "ISC", ":/NUMEROS/TRES"]
        self.diccionario[3] = ["Karla", "II", ":/NUMEROS/CUATRO"]
        self.diccionario[4] = ["Granda", "IM", ":/NUMEROS/CINCO"]
        self.diccionario[5] = ["Villalobos", "IC", ":/NUMEROS/UNO"]

        alumno = self.diccionario[0]
        self.txt_valor.setText(alumno[0])

        self.txt_img.setPixmap(QtGui.QPixmap(alumno[2]))

        print("Total Elementos Diccionariio: "  + str(len(self.diccionario)))

        #########################################

        self.btn_iniciar.clicked.connect(self.iniciar)

        ###########################################

        self.SegundoPlano = QtCore.QTimer()
        self.SegundoPlano.timeout.connect(self.actualizaImagen)


    #area de slots
    def actualizaImagen(self):
        valor_actual = self.dial.value()  ##int
        fin = len(self.diccionario)

        print(valor_actual)
        alumno = self.diccionario[valor_actual]  # obtencion del alumno asociado al indice que se esta consultando

        self.txt_valor.setText(alumno[0])
        self.txt_img.setPixmap(QtGui.QPixmap(alumno[2]))

        self.dial.setValue(valor_actual+1)

        if valor_actual + 1 == fin:
            self.SegundoPlano.stop()

        # Tarea (Practica 2) - "Slider" de Imagenes <-- Video para el lunes 27 de sept

    def iniciar(self):
        self.SegundoPlano.start(1000)

        #valor_actual = self.dial.value()   ##int
        #fin = len(self.diccionario)

        #import time as t

        #for i in range(valor_actual, fin):
        #    print(i)
        #    alumno = self.diccionario[i] #obtencion del alumno asociado al indice que se esta consultando

        #    self.txt_valor.setText(alumno[0])
        #    self.txt_img.setPixmap(QtGui.QPixmap(alumno[2]))

            #t.sleep(1)

    def valorCambio(self):
        valor = self.dial.value()   ##int
        print(valor)

        #valor = str(valor)
        #self.txt_valor.setText(valor)

        alumno = self.diccionario[valor]

        self.txt_valor.setText(alumno[0])
        print(alumno[1])

        self.txt_img.setPixmap(QtGui.QPixmap(alumno[2]))

    def mensaje(self,msj):
        m = QtWidgets.QMessageBox()
        m.setText(msj)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())