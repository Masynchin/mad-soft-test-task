from fastapi import FastAPI


app = FastAPI(prefix="/memes")


@app.get("")
async def get_memes():
    ...


@app.get("/{id}")
async def get_meme(id: int):
    ...


@app.post("")
async def post_meme():
    ...


@app.put("/{id}")
async def put_meme(id: int):
    ...


@app.delete("/{id}")
async def delete_meme(id: int):
    ...
