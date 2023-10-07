import shutil
import os

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Request, UploadFile

from filters.tareas import process

app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


@app.get("/")
async def root(request: Request):
    args = {
        "request": request,
        "image_processed": False,
    }
    return templates.TemplateResponse(
        "index.html", context=args
    )


@app.post("/upload-image/")
async def upload_image(image: UploadFile, request: Request):
    # Ensure the "static" directory exists
    os.makedirs("static", exist_ok=True)

    img_extension = image.filename.split(".")[-1]
    # Save the uploaded file to the "static" directory
    with open(os.path.join("static", f"upload_image.{img_extension}"), "wb") as image_file:
        shutil.copyfileobj(image.file, image_file)

    process_times = process(img_extension=img_extension)
    args = {
        "request": request,
        "image_processed": True,
        "sequencial_time": process_times["sequencial_time"],
        "parallel_time": process_times["parallel_time"],
        "sequencial_img_path": "sequencial_processed_image." + img_extension,
        "parallel_img_path": "parallel_processed_image." + img_extension,
        "image_uploaded_path": "upload_image." + img_extension

    }
    return templates.TemplateResponse(
        "index.html", context=args
    )
