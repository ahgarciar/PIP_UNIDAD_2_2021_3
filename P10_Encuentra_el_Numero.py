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
        imagenesOrden = [1, 2, 3, 4]

        #desordenar(imagenesOrden)

        clickable(self.img_a).connect(self.imagenA)
        clickable(self.img_b).connect(self.imagenB)
        clickable(self.img_c).connect(self.imagenC)
        clickable(self.img_d).connect(self.imagenD)


    #area de slots
    def imagenA(self):
        print("A")

    def imagenB(self):
        print("B")

    def imagenC(self):
        print("C")

    def imagenD(self):
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


