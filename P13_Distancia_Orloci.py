import sys

from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "P13_Distancia_Orloci.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.txt_vectorA.setText("8,6,7,8,10")
        self.txt_vectorB.setText("9,7,5,7,9")

        self.btn_calcular.clicked.connect(self.calcular)

    def calcular(self):
        print("Calculando distancia")

        vectorA = self.txt_vectorA.text().split(",")
        vectorA = [int(i) for i in vectorA]
        print(vectorA)


        vectorB = self.txt_vectorB.text().split(",")
        #vectorB = [int(i) for i in vectorB]
        vectorB = list(map(int, vectorB))

        print(vectorB)

        #Tarea - > Investigar operaciones con cadenas de caracteres en python
        #Tarea - > Investigar sobre listas de comprensión

        ##################################################

        norma2_vA = self.norma2(vectorA)
        print(norma2_vA)

        norma2_vB = self.norma2(vectorB)
        print(norma2_vB)

        mulNormas = norma2_vA * norma2_vB
        mulNormas = round(mulNormas,2)
        ##########################################
        tempSum = 0
        for i in range(len(vectorA)): #i = index
            tempSum += vectorA[i] * vectorB[i]
        tempSum = round(tempSum, 2)
        print("tempSum", tempSum)
        #########################################
        aux = tempSum / mulNormas
        print("resultado division: " , aux)
        aux = 2 * aux
        print("result div * 2: ", aux)
        ############################
        preraiz = 2 - aux
        print("pre raiz: ", preraiz)
        ############################
        distancia = preraiz**0.5
        #####################
        print("distancia: ", distancia)

        distancia = round(distancia,2)
        self.txt_distancia.setText(str(distancia))

    def norma2(self, vector):
        normaResult = 0

        for i in vector:  #para cada elemento i del vector
            normaResult += i**2 #elevar a i al cuadrado

        normaResult = normaResult**0.5

        return normaResult


    def mensaje(self,msj):
        m = QtWidgets.QMessageBox()
        m.setText(msj)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())