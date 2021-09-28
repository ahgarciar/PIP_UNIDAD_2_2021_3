import sys

from PyQt5 import uic, QtWidgets, QtGui, QtCore

qtCreatorFile = "P6_SliderColor.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.hs_R.setMinimum(0)
        self.hs_R.setMaximum(255)
        self.hs_R.setSingleStep(1)
        self.hs_R.setValue(0)
        self.txt_valor_R.setText("0")

        self.hs_R.valueChanged.connect(self.cambioR)

        ########################################################################

        self.hs_G.setMinimum(0)
        self.hs_G.setMaximum(255)
        self.hs_G.setSingleStep(1)
        self.hs_G.setValue(0)
        self.txt_valor_G.setText("0")

        self.hs_G.valueChanged.connect(self.cambioG)

        ########################################################################

        self.hs_B.setMinimum(0)
        self.hs_B.setMaximum(255)
        self.hs_B.setSingleStep(1)
        self.hs_B.setValue(0)
        self.txt_valor_B.setText("0")

        self.hs_B.valueChanged.connect(self.cambioB)

        ########################################################################

        self.R = 0
        self.G = 0
        self.B = 0

        self.cambiarColor()

    #area de slots
    def cambioR(self):
        self.R = self.hs_R.value()
        self.txt_valor_R.setText(str(self.R))
        self.cambiarColor()

    def cambioG(self):
        self.G = self.hs_G.value()
        self.txt_valor_G.setText(str(self.G))
        self.cambiarColor()

    def cambioB(self):
        self.B = self.hs_B.value()
        self.txt_valor_B.setText(str(self.B))
        self.cambiarColor()

    def cambiarColor(self):
        colorFondo = "background-color: rgb(" + str(self.R) + "," + str(self.G) + "," + str(self.B) + ");"
        self.btn_color.setStyleSheet(colorFondo)

    def mensaje(self,msj):
        m = QtWidgets.QMessageBox()
        m.setText(msj)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

    #Tarea (Programa). Semaforo automatizado con Colores

    #Tarea (Programa). Cambiar Tonalidad de un Color con UN Slider
    #   escoger un color y tendrán que mediante programación ajustar lo necesario
    #   para que se muestre como el color pasa de una tonalidad suave a una más fuerte

    #Tarea (Programa). Conversor de Centigrado a Farenheit y Viceversa (1 o 2 Sliders)


