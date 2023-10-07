import shutil
import os

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Request, UploadFile

from filters.tareas import tareas_process
from filters.threads import threads_process
from filters.sequencial import sequential_process

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

    tareas_times = tareas_process(img_extension=img_extension)
    threads_time = threads_process(img_extension=img_extension)
    sequencial_time = sequential_process(img_extension=img_extension)

    args = {
        "request": request,
        "image_processed": True,
        "sequencial_time": sequencial_time,
        "threads_time": threads_time,
        "tareas_time": tareas_times,
        "image_uploaded_path": "upload_image." + img_extension,
        "sequencial_img_path": "sequencial_processed_image." + img_extension,
        "tareas_img_path": "tareas_processed_image." + img_extension,
        "threads_img_path": "threads_processed_image." + img_extension

    }
    return templates.TemplateResponse(
        "index.html", context=args
    )
