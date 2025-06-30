from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import random
import string
from datetime import datetime

from database.get_database import get_db
from models.basic_data import BasicData
from models.basic_data_dto import BasicDataDto

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/all")
async def get_all():
    return {"message": "Hello World"}

@app.post("/sync-data", response_model=BasicDataDto)
def sync_data(dto: BasicDataDto, db: Session = Depends(get_db)):
    synced_data = BasicData(
        id=dto.id,
        firstname=dto.firstName,
        lastname=dto.lastName,
        createdAt=dto.createdAt,
        synced=True
    )

    db.merge(synced_data)
    db.commit()
    db.refresh(synced_data)
    return BasicDataDto(
        id=synced_data.id,
        firstName=synced_data.firstname,
        lastName=synced_data.lastname,
        createdAt=synced_data.createdAt,
        synced=synced_data.synced
    )

@app.post("/random-data", response_model=BasicDataDto)
def create_random_data(db: Session = Depends(get_db)):
    first = ''.join(random.choices(string.ascii_letters, k=6))
    last = ''.join(random.choices(string.ascii_letters, k=8))

    data = BasicData(
        firstname=first,
        lastname=last,
        createdAt=datetime.utcnow(),
        synced=False
    )

    db.add(data)
    db.commit()
    db.refresh(data)
    return BasicDataDto(
        id=data.id,
        firstName=data.firstname,
        lastName=data.lastname,
        createdAt=data.createdAt,
        synced=data.synced
    )