from typing import Annotated

import strawberry
from fastapi import FastAPI, File
from starlette.middleware.cors import CORSMiddleware
from strawberry.fastapi import GraphQLRouter

from wycena.api import storage
from wycena.api.mutation import Mutation
from wycena.api.query import Query
from wycena.importer.transaction import perform_import

schema = strawberry.Schema(Query, Mutation)

graphql_app = GraphQLRouter(schema)

app = FastAPI()
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(graphql_app, prefix="/graphql")


@app.post("/upload/transactions/")
async def upload_transactions(files: Annotated[list[bytes], File(description="Multiple files as bytes")]):
    for f in files:
        key = storage.save(file_name=f.filename, data=f.file.read(), prefix="transactions")
        perform_import(key)
