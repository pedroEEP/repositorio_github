import requests  # Importamos la librería requests

# URL de la API RandomUser para obtener un usuario aleatorio
url = "https://randomuser.me/api/"

# Hacer la solicitud HTTP
respuesta = requests.get(url)

# Mostrar la respuesta completa en texto y JSON
print("Respuesta en formato TEXT:")
print(respuesta.text)  # Muestra la respuesta en formato string

print("\n Respuesta en formato JSON:")
datos = respuesta.json()  # Convertimos a formato JSON (diccionario)
print(datos)  # Mostramos el JSON estructurado



