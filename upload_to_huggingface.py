import os
import requests

# Configura el token de acceso
token = os.environ["HUGGING_FACE_TOKEN"]

# Configura el nombre del repositorio
repo_id = "Sasjj/Encodebottelegram"

# Configura la URL de la API
url = f"https://huggingface.co/api/repos/{repo_id}/tree/main"

# Configura los archivos a subir
files = {}
for filename in os.listdir("."):
    if os.path.isfile(filename):
        files[filename] = open(filename, "rb")

# Configura los headers de la solicitud
headers = {
    "Authorization": f"Bearer {token}",
}

# Envía la solicitud
for filename, file in files.items():
    response = requests.put(
        f"https://huggingface.co/api/repos/{repo_id}/contents/{filename}",
        headers=headers,
        data=file,
    )

    # Verifica si la solicitud fue exitosa
    if response.status_code == 200:
        print(f"Archivo {filename} subido con éxito")
    else:
        print(f"Error al subir archivo {filename}: {response.text}")
