import os
import requests
import json

# Configura el token de acceso
token = os.environ["HUGGING_FACE_TOKEN"]

# Configura el nombre del repositorio
repo_id = "Sasjj/Encodebottelegram"

# Configura la URL de la API
url = f"https://huggingface.co/api/repos/{repo_id}"

# Configura los archivos a subir
files = {}
for filename in os.listdir("."):
    if os.path.isfile(filename):
        files[filename] = open(filename, "rb")

# Crea un commit
commit_message = "Subiendo archivos a Hugging Face"
commit_data = {
    "commit_message": commit_message,
    "files": {}
}
for filename, file in files.items():
    commit_data["files"][filename] = file.read()

# Envía la solicitud
response = requests.post(
    url + "/contents",
    headers={
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    },
    data=json.dumps(commit_data)
)

# Verifica si la solicitud fue exitosa
if response.status_code == 200:
    print("Archivos subidos con éxito")
else:
    print("Error al subir archivos:", response.text)
