import os
import requests

# Configura el token de acceso
token = os.environ["HUGGING_FACE_TOKEN"]

# Configura el nombre del repositorio
repo_id = "Sasjj/Encodebottelegram"

# Configura la URL de la API
url = f"https://huggingface.co/api/repos/{repo_id}/tree/main"

# Configura los archivos a subir
files = {
    "file": open("tu_archivo.txt", "rb")
}

# Configura los headers de la solicitud
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "multipart/form-data"
}

# Envía la solicitud
response = requests.post(url, headers=headers, files=files)

# Verifica si la solicitud fue exitosa
if response.status_code == 200:
    print("Archivos subidos con éxito")
else:
    print("Error al subir archivos")
