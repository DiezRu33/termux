import requests

# Función para enviar una pregunta a la API y obtener una respuesta
def obtener_respuesta(pregunta):
    url = "https://chat.googleapis.com/$discovery/rest?version=v1"  # Reemplaza con la URL de la API REST
    payload = {"pregunta": pregunta}
    response = requests.post(url, json=payload)
    respuesta = response.json()["respuesta"]
    return respuesta

# Loop principal de conversación
while True:
    pregunta = input("Usuario: ")
    respuesta = obtener_respuesta(pregunta)
    print("Máquina:", respuesta)
  
