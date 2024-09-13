import strawberry
from fastapi import FastAPI, UploadFile
from starlette.middleware.cors import CORSMiddleware
from strawberry.fastapi import GraphQLRouter

from wycena.abstract_models import QueryOptions, PropertyType
from wycena.api import storage
from wycena.api.mutation import Mutation
from wycena.api.query import Query
from wycena.db.models import Transaction
from wycena.importer.transaction import perform_import

schema = strawberry.Schema(Query, Mutation)

graphql_app = GraphQLRouter(schema)

app = FastAPI()
origins = [
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
async def upload_transactions(files: list[UploadFile], city: str,
                              property_type: PropertyType):
    for f in files:
        key = storage.save(file_name=f.filename, data=f.file.read(), prefix="transactions")
        perform_import(key, city=city, property_type=property_type)

@app.get("/excel/transactions/")
async def excel_transactions(address: str, price: int = None, distance: float = None,
                             built_date: int = None):
    transactions = Transaction.filter(QueryOptions(page_size=10))[0]
    res = []
    for transaction in transactions:
        res.append(";".join(
            [transaction.street, transaction.city, str(transaction.price)]
        ))
    return "\n".join(res)
