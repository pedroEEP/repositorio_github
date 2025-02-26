print("programa de evaluacion de notas de alumnos")
nota_alumno=int(input("Dame una nota: "))
def evaluacion(nota):
	valoracion="aprobado"
	if nota<5:
		valoracion="suspenso"
	return(valoracion)
print((evaluacion(nota_alumno).upper()) + " " + str(nota_alumno))
print(evaluacion(nota_alumno).find("b"))
#si no encuentra algo devuelve -1
#Otro método igual o parecido a find()
print(evaluacion(nota_alumno).index("b"))
#La diferencia es que index si no encuentra nada nos devuelve un error
print(evaluacion(nota_alumno).isnumeric())
print(evaluacion(nota_alumno).isalpha())

print(evaluacion(nota_alumno).count("a"))
try:
	print(evaluacion(nota_alumno).len())
except AttributeError:
	print("len no es un metodo es una funcion")

print(len(evaluacion(nota_alumno)))
print(evaluacion(nota_alumno).startswith("a"))
print(evaluacion(nota_alumno).endswith("a"))

print(evaluacion(nota_alumno).replace("a","e"))

cadena_prueba="Hola, soy, Pedro"
nueva_cadena=cadena_prueba.split(",") 
#Nos devuelve una lista
print(nueva_cadena[0])













