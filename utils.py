import os
from fastapi import UploadFile
from uuid import uuid4


UPLOAD_DIR = "static/uploads/growers"
def saved_upload_file(upload_file: UploadFile, upload_dir: str = UPLOAD_DIR, grower_id: str) -> str:
      if upload_file.content_type not in ("image/jpeg", "image/png", "image/webp"):
        raise HTTPException(status_code=400, detail="Only JPEG/PNG/WEBP images are allowed for photo")

    os.makedirs(upload_dir, exist_ok=True)
    ext = os.path.splitext(upload_file.filename)[1] or ".jpg"
    filename = f"{uuid.uuid4().hex}{ext}"
    file_path = os.path.join(upload_dir, filename)

      with open(file_path, "wb") as f:
        f.write(upload_file.file.read())

    return filename