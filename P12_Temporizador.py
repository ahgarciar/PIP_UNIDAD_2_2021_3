import sys

from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "P11_Temporizador.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_accion.clicked.connect(self.accion)

        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.temporizador)

        self.tiempo = -1

    #area de slots
    def accion(self):
        t = self.btn_accion.text()
        if t == "INICIAR":
            velTempo = int(self.txt_velocidad.text())

            self.btn_accion.setText("PAUSAR")
            #codigo para iniciar el proceso del temporizador
            self.tiempo = int(self.txt_tiempo.text())
            self.txt_tempo.setText(str(self.tiempo))
            self.segundoPlano.start(velTempo)
        else: #PAUSAR
            self.btn_accion.setText("INICIAR")
            self.segundoPlano.stop()
            self.txt_tiempo.setText(str(self.tiempo))


    def temporizador(self):
        print("hola")
        self.tiempo -= 1
        self.txt_tempo.setText(str(self.tiempo))
        if self.tiempo == 0:
            self.btn_accion.setText("INICIAR")
            self.mensaje("Se acabo el tiempo!!!! ")
            self.segundoPlano.stop()

    #Práctica :  Simular un Reloj con Horas, Minutos y Segudos empleando un Timer
    # De preferencia, de 24hrs

    #Tarea: Buscar como reproducir efectos de sonido en python



    def mensaje(self,msj):
        m = QtWidgets.QMessageBox()
        m.setText(msj)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())