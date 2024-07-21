from databases import Database


class MemeDatabase:
    def __init__(self, database_url: str):
        self.database = Database(database_url)

    async def connect(self):
        await self.database.connect()

    async def disconnect(self):
        await self.database.disconnect()

    async def initialize(self):
        await self.database.execute(
            """
            CREATE TABLE IF NOT EXISTS memes(
                id SERIAL PRIMARY KEY,
                description TEXT,
                image_url TEXT
            )
            """
        )

    async def one(self, meme_id: int):
        meme = await self.database.fetch_one(
            "SELECT * FROM memes WHERE id = :meme_id", {"meme_id": meme_id}
        )
        return meme

    async def many(self):
        memes = await self.database.fetch_all("SELECT * FROM memes")
        return memes

    async def create(self, description: str, image_url: str) -> int:
        meme_id = await self.database.execute(
            "INSERT INTO memes(description, image_url) VALUES (:description, :image_url) RETURNING id",
            {"description": description, "image_url": image_url},
        )
        return meme_id

    async def replace(self, meme_id: int, description: str, image_url: str):
        await self.database.execute(
            "UPDATE memes SET description = :description, image_url = :image_url WHERE id = :meme_id",
            {"meme_id": meme_id, "description": description, "image_url": image_url},
        )

    async def delete(self, meme_id: int):
        await self.database.execute(
            "DELETE FROM memes WHERE id = :meme_id", {"meme_id": meme_id}
        )
