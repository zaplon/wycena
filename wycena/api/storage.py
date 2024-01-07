import os

import boto3

from wycena.settings import settings


def read(key: str) -> bytes:
    if settings.USE_LOCAL_STORAGE:
        with open(os.path.join(settings.MEDIA_PATH, key), "rb") as f:
            data = f.read()
        return data
    else:
        s3_client = boto3.client('s3')
        obj = s3_client.get_object(Bucket=settings.S3_BUCKET_NAME, Key=key)
        return obj.read()


def save(data: bytes, prefix: str, file_name: str) -> str:
    if settings.USE_LOCAL_STORAGE:
        dst = os.path.join(settings.MEDIA_PATH, file_name)
        with open(dst, "wb") as f:
            f.write(data)
        return dst
    else:
        s3_client = boto3.client('s3')
        key = f"{prefix}/{file_name}"
        s3_client.put_object(Bucket=settings.S3_BUCKET_NAME, Key=key, Body=data)
        return key
