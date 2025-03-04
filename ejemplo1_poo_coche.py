class Coche:
    # Atributos de la clase
    marca = "Toyota"
    modelo = "Corolla"
    color = "Rojo"

    # Método sencillo para mostrar información
    def mostrar_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Color: {self.color}")

    # Método para cambiar el color del coche
    def cambiar_color(self, nuevo_color):
        self.color = nuevo_color
        print(f"El coche ahora es de color {self.color}")

# Crear un objeto de la clase Coche
mi_coche = Coche()

# Llamar a los métodos de la clase
mi_coche.mostrar_info()  # Muestra la información del coche

mi_coche.cambiar_color("Azul")  # Cambia el color del coche a azul
mi_coche.mostrar_info()  # Verificar el cambio de color


