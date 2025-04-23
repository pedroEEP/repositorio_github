from peewee import *

mi_db=SqliteDatabase("Asignaturas.db")

class Asignaturas(Model):
    nombre=CharField()
    nota=IntegerField()
    class Meta():
        database=mi_db
mi_db.connect()    
mi_db.create_tables([Asignaturas])

#Asignaturas.create(nombre="Ingles", nota=7)
#Asignaturas.create(nombre="Mates", nota=8)
"""
#consulta a toda la BBDD
resultado=Asignaturas.select()
print(resultado)
for i in resultado:
    print(i.nombre, i.nota)

#Consultar una asignatura en concreto
resultado=Asignaturas.get(Asignaturas.nombre=="Ingles")
print(resultado.nombre, resultado.nota)

#cambiar un campo de la asignatura
resultado=Asignaturas.get(Asignaturas.nombre=="Ingles")
resultado.nota=10
resultado.save()
"""
#imprimimos una en concreto
resultado=Asignaturas.get(Asignaturas.nombre=="Ingles")
#print(resultado.nombre, resultado.nota)

    
#borrar un registro
resultado=Asignaturas.get(Asignaturas.nombre=="Ingles")
resultado.delete_instance()

#consultar todos los registros de nuevo
resultado=Asignaturas.select()
print(resultado)
for i in resultado:
    print(i.nombre, i.nota)


