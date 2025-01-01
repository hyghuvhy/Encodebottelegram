import os
from huggingface_hub import Repository

# Configura el token de acceso
token = os.environ["HUGGING_FACE_TOKEN"]

# Configura el nombre del repositorio
repo_name = "Sasjj/Encodebottelegram"

# Crea una instancia de la clase Repository
repo = Repository(
    local_dir=".",  # Directorio local que contiene los archivos a subir
    repo_type="model",  # Tipo de repositorio (model, dataset, etc.)
    repo_id=repo_name,  # ID del repositorio
    token=token,  # Token de acceso
)

# Sube los archivos al repositorio
repo.push_to_hub(commit_message="Subiendo archivos a Hugging Face")
