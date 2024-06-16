import os

from fastapi import APIRouter, Depends,File, UploadFile
from fastapi.responses import FileResponse
from pathlib import Path
router = APIRouter(
    prefix="/img",
    tags=["Img"]
)
@router.get("/")
async def get_image(path:str):
    image_path = Path("src/img/"+path)
    if not image_path.is_file():
        return {"error": "Image not found on the server"}
    return FileResponse(image_path)
@router.post("/upload/")
async def upload_image(file:UploadFile = File(...)):
    file_location = f"src/img/{file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())
    return {"filename": file}