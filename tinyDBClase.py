from tinydb import TinyDB, Query

mi_db=TinyDB("asignaturas3.json")
Asignaturas=Query()

#mi_db.insert({"nombre":"Ingles","nota":7})
#mi_db.insert({"nombre":"Geografia","nota":8})
"""
resultado=mi_db.all()
print(resultado)
for i in resultado:
    print(f"Nombre: {i['nombre']} Nota: {i['nota']}")

resultado=mi_db.search(Asignaturas.nombre=="Ingles")
print(resultado)


mi_db.update({"nota":10},Asignaturas.nombre=="Ingles")
resultado=mi_db.search(Asignaturas.nombre=="Ingles")
print(resultado)
"""

#mi_db.remove(Asignaturas.nombre=="Ingles")
resultado=mi_db.all()
#print(resultado)
for i in resultado:
    print(f"Nombre: {i['nombre']} Nota: {i['nota']}")