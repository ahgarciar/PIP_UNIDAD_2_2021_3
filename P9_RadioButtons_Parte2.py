import sys

from PyQt5 import uic, QtWidgets, QtGui, QtCore

qtCreatorFile = "P9_RadioButtons_Parte2.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        #self.rb_hombre.setChecked(True)
        self.rb_soltero.setChecked(True)
        self.rb_isc.setChecked(True)

        self.rb_hombre.toggled.connect(self.cambioHombre)
        self.rb_mujer.toggled.connect(self.cambioMujer)
        self.rb_otro.toggled.connect(self.cambioOtro)

        self.sexo = "NO DEFINIDO"


        self.btn_enviar.clicked.connect(self.enviar_formulario)

    #area de slots
    def enviar_formulario(self):
        print("Sexo: " + self.sexo)

    def cambioHombre(self):
        self.sexo = "HOMBRE"

    def cambioMujer(self):
        self.sexo = "MUJER"

    def cambioOtro(self):
        self.sexo = "OTRO"


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


