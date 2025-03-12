class coche():
    def __init__(self,marca,modelo,color):
        self.marca=marca
        self.modelo=modelo
        self.color=color
        self.encendido= False
        self.velocidad=0

#    def __str__(self):
#        return ",".join([f"Marca:{self.marca}",
#            f"Modelo: {self.modelo}",
#            f"Color: {self.color}",
#            f"Velocidad: {self.velocidad}",
#            f"Estado: {'Encendido' if self.encendido else 'Apagado'}"])

    def __str__(self):
        return f"""Marca: {self.marca} 
        Modelo: {self.modelo} 
        Color: {self.color}
        Estado: {'Encendido' if self.encendido else 'Apagado'}
        Velocidad: {self.velocidad}"""


    def mostrar_info(self):
        print(f"La marca del coche es: {self.marca}, el modelo {self.modelo}, color {self.color}")

    def cambiar_color(self, nuevo_color):
        self.color=nuevo_color
        print(f"El nuevo color es: {self.color}")
    def detener(self):
        if self.encendido:
            self.velocidad=0
            self.encendido=False
            print("El coche se ha apagado")
        else:
            print("El coche esta ya parado")

    def acelerar(self, incremento):
        if self.encendido:
            self.velocidad+=incremento
        else:
            print("No puedes acelerar un coche apagado")

    def frenar(self,decremento):
        if self.encendido:
            if (self.velocidad-decremento)>0:
                self.velocidad-=decremento
            else:
                self.velocidad=0
                print("El coche se ha parado completamente")
        else:
            print("No se puede frenar un coche apagado")



marca=input("dame la marca del coche: ")
modelo=input("dame el modelo del coche: ")
color=input("dame el color del coche: ")
mi_coche=coche(marca,modelo,color)

print(mi_coche)



#mi_coche.encendido=True
#print(mi_coche.color)
#mi_coche.mostrar_info()
#mi_coche.cambiar_color("azul")
#mi_coche.acelerar(100)

#print(mi_coche)