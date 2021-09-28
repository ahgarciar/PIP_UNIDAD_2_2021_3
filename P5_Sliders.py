import sys

from PyQt5 import uic, QtWidgets, QtGui, QtCore

qtCreatorFile = "P5_Sliders.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(10)
        self.horizontalSlider.setSingleStep(1)
        self.horizontalSlider.setValue(0)
        self.txt_valor_horizontal.setText("0")

        self.horizontalSlider.valueChanged.connect(self.cambioHorizontal)

        ########################################################################

        self.verticalSlider.setMinimum(0)
        self.verticalSlider.setMaximum(10)
        self.verticalSlider.setSingleStep(1)
        self.verticalSlider.setValue(0)
        self.txt_valor_vertical.setText("0")

        self.verticalSlider.valueChanged.connect(self.cambioVertical)

    #area de slots
    def cambioHorizontal(self):
        valor = self.horizontalSlider.value()
        self.txt_valor_horizontal.setText(str(valor))

    def cambioVertical(self):
        valor = self.verticalSlider.value()
        self.txt_valor_vertical.setText(str(valor))

    def mensaje(self,msj):
        m = QtWidgets.QMessageBox()
        m.setText(msj)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())