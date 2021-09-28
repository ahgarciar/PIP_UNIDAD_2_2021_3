import sys

from PyQt5 import uic, QtWidgets, QtGui, QtCore

qtCreatorFile = "P8_RadioButtons.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.rb_hombre.setChecked(True)
        self.rb_soltero.setChecked(True)
        self.rb_isc.setChecked(True)

        #self.rb_hombre.clicked.connect(self.cambioSexo)
        #self.rb_mujer.clicked.connect(self.cambioSexo)

        self.rb_hombre.toggled.connect(self.cambioSexo)
        self.rb_mujer.toggled.connect(self.cambioSexo)

    #area de slots
    def cambioSexo(self):
        estadoHombre = self.rb_hombre.isChecked()
        estadoMujer = self.rb_mujer.isChecked()
        print(str(estadoHombre) + "  " + str(estadoMujer))

    def mensaje(self,msj):
        m = QtWidgets.QMessageBox()
        m.setText(msj)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


