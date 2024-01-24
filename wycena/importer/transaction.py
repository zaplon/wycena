import csv
import datetime
import logging
import uuid

import openpyxl
from pydantic.v1 import DateError
from pydantic.v1.datetime_parse import parse_date
from pynamodb.exceptions import AttributeNullError

from wycena.db import models as db_models


def perform_import(file_path: str, **defaults):
    rows = get_rows(file_path)
    for row in rows:
        upsert_transaction(row, **defaults)


def get_rows(file_path) -> [dict]:
    extension = file_path.split('.')[-1]
    if extension in ['xlsx', 'xls']:
        wb = openpyxl.load_workbook(file_path)
        rows = []
        for sheet in wb.worksheets:
            first_row = next(sheet.iter_rows())
            headers = [c.value for c in first_row]
            for r in sheet.iter_rows():
                rows.append(dict(zip(headers, r.values())))
        return rows
    elif extension == 'csv':
        with open(file_path, "r") as f:
            dialect = csv.Sniffer().sniff(f.read(), delimiters=';,| ')
            f.seek(0)
            rows = list(csv.DictReader(f, dialect=dialect))
        return rows
    else:
        raise ValueError(f"Not supported extension: {extension}")


def upsert_transaction(row: dict, **defaults):
    row = {k.lower(): v for k, v in row.items()}
    transaction = db_models.Transaction()
    for field, col_handler in FIELD_HANDLERS.items():
        for col_name in col_handler[0]:
            if col_name in row:
                try:
                    val = col_handler[1](row[col_name]) if col_handler[1] is not None else row[col_name]
                except ValueError as e:
                    logging.error(e)
                    return
                setattr(transaction, field, val)
                break
    transaction.long, transaction.lat = get_coords(transaction)
    for k, v in defaults.items():
        if not getattr(transaction, k, None):
            setattr(transaction, k, v)
    transaction.id = str(uuid.uuid4())
    print(transaction.__dict__)
    try:
        transaction.save()
    except AttributeNullError as e:
        logging.warning(e)


def handle_float(val):
    return float(
        val.replace(",", ".").replace(" ", "").replace(u'\xa0', "")
    ) if val else None


def handle_int(val):
    return int(val) if val else None


def handle_date(val):
    try:
        date = parse_date(val) if val else None
    except DateError:
        fmts = ["%d.%m.%Y"]
        for fmt in fmts:
            try:
                date = datetime.datetime.strptime(val, fmt).date()
                break
            except ValueError:
                continue
        else:
            raise ValueError(f"Could not parse date: {val}")
    return datetime.datetime.combine(date, datetime.time.min)


def get_coords(transaction: db_models.Transaction):
    return 20, 50


FIELD_HANDLERS = {
    "street": (["ulica"], None),
    "building_nr": (["numer", "nr bud.", "numer budynku"], None),
    "city": (["miejscowość", "miasto"], None),
    "district": (["dzielnica"], None),
    "floor": (["piętro", "pietro", "Kond."], handle_int),
    "price": (["cena", "cena trans. [zł]"], handle_float),
    "area": (["powierzchnia", "p.u. [m2]"], handle_float),
    "transaction_date": (["data transakcji"], handle_date),
    "primary_market": (["rynek", "rodzaj rynku"], lambda x: True if x in ["1", "pierwotny"] else False),
    "number_of_rooms": (["izby", "Liczba pokoi"], handle_int),
    "number_of_floors": (["liczba pięter"], handle_int)
}
