import os
from contextlib import asynccontextmanager
from typing import Annotated

from fastapi import FastAPI
from fastapi import Form, HTTPException, UploadFile

from api.database import MemeDatabase
from api.schema import MemeGet, MemeCreated


database = MemeDatabase(os.getenv("DATABASE_URL"))


@asynccontextmanager
async def database_lifespan(app: FastAPI):
    await database.connect()
    await database.initialize()
    yield
    await database.disconnect()


app = FastAPI(lifespan=database_lifespan)

@app.get("/memes")
async def get_memes() -> list[MemeGet]:
    memes = await database.many()
    return memes


@app.get("/memes/{id}")
async def get_meme(id: int) -> MemeGet:
    meme = await database.one(id)
    return meme


@app.post("/memes", status_code=201)
async def post_meme(description: Annotated[str, Form()], image: UploadFile) -> MemeCreated:
    try:
        validate_image_file(image)
    except HTTPException as e:
        raise e

    meme_id = await database.create(description, "image_url")
    return MemeCreated(id=meme_id)


def validate_image_file(file: UploadFile):
    """Валидация файла изображения.

    Файл должен весить не более 2 мегабайт, и является PNG/JPEG изображением.
    """
    if file.size > 2 * 1024 * 1024:
        raise HTTPException(status_code=413, detail="File is too large (>2MB)")

    if file.content_type not in ("image/png", "image/jpeg", "image/jpg"):
        raise HTTPException(status_code=415, detail="Unsopperted file type")


@app.put("/memes/{id}", status_code=200)
async def put_meme(id: int, description: Annotated[str, Form()], image: UploadFile):
    try:
        validate_image_file(image)
    except HTTPException as e:
        raise e

    await database.replace(id, description, "image_url")


@app.delete("/{id}", status_code=204)
async def delete_meme(id: int):
    await database.delete(id)
