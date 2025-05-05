from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("edadClase.ui",self)
        
        self.boton_comprobar.clicked.connect(self.comprobar_edad)
    def comprobar_edad(self):
        nombre=self.entry_nombre.text()
        edad=int(self.entry_edad.text())
        
        if edad>18:
            self.label_resultado.setText(f"{nombre} Mayor de edad")
        else:
            self.label_resultado.setText("menor de edad")

app=QApplication(sys.argv)
ventana=Ventana()
ventana.show()
sys.exit(app.exec_())