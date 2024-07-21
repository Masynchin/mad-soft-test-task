import hashlib
from datetime import datetime
from io import BytesIO

from minio import Minio
from minio.error import S3Error


class MemeMinio:
    def __init__(self, url: str, access_key: str, secret_key: str):
        self.client = Minio(url, access_key, secret_key, secure=False)

    def upload(self, file_name: str, data: BytesIO, size: int, content_type: str) -> str:
        found = self.client.bucket_exists("images")
        if not found:
            self.client.make_bucket("images")

        object_name = generate_unique_object_name(file_name)
        result = self.client.put_object("images", object_name, data, size, content_type)
        return result.object_name

    def download(self, file_name: str):
        try:
            response = self.client.get_object("images", file_name)
            image_bytes = response.data
            response.close()
            response.release_conn()
            return image_bytes
        except S3Error:
            raise KeyError("No such file")


def generate_unique_object_name(file_name: str) -> str:
    return hashlib.sha256(f"{file_name}{datetime.now()}".encode("utf-8")).hexdigest()
