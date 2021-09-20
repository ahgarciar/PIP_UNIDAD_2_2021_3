import sys

from PyQt5 import uic, QtWidgets

qtCreatorFile = "P1_Control_Dial.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.dial.setMinimum(-10)
        self.dial.setMaximum(10)
        self.dial.setSingleStep(2)

        self.dial.setValue(-10)
        self.txt_valor.setText("-10")

        self.dial.valueChanged.connect(self.valorCambio)

    #area de slots
    def valorCambio(self):
        valor = self.dial.value()   ##int
        print(valor)

        valor = str(valor)

        self.txt_valor.setText(valor)


    def mensaje(self,msj):
        m = QtWidgets.QMessageBox()
        m.setText(msj)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())