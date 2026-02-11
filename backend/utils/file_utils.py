import os
import uuid


BASE_UPLOAD_DIR = "data/raw_docs"


def ensure_upload_dir():
    os.makedirs(BASE_UPLOAD_DIR, exist_ok=True)


def save_uploaded_file(file_bytes: bytes, filename: str) -> str:
    ensure_upload_dir()

    ext = filename.split(".")[-1]
    new_name = f"{uuid.uuid4()}.{ext}"

    path = os.path.join(BASE_UPLOAD_DIR, new_name)

    with open(path, "wb") as f:
        f.write(file_bytes)

    return path
