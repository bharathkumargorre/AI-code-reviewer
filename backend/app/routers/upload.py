from fastapi import APIRouter, UploadFile, File
import shutil

router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)


@router.post("/")
def upload_file(file: UploadFile = File(...)):

    filepath = f"app/uploads/{file.filename}"

    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "filename": file.filename,
        "path": filepath,
        "message": "File uploaded successfully"
    }