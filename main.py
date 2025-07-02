from fastapi import FastAPI, Depends
from typing import List, Any

from sqlalchemy.orm import Session
import random
import string
from datetime import datetime

from database.database import Base, engine
from database.get_database import get_db
from models.basic_data import BasicData
from models.basic_data_dto import BasicDataDto

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/all")
async def get_all(db: Session = Depends(get_db)):
    return db.query(BasicData).all()

@app.post("/sync-data")
def sync_data(data: List[BasicDataDto], db: Session = Depends(get_db)):
    saved_data = []

    for dto in data:
        if dto.id is None:
            synced_data = BasicData(
                uid=dto.uid,
                firstName=dto.firstName,
                lastName=dto.lastName,
                synced=True
            )
            saved_data.append(synced_data)

    db.add_all(saved_data)
    db.commit()
    for synced_data in saved_data:
        db.refresh(synced_data)

    return saved_data

@app.post("/random-data", response_model=BasicDataDto)
def create_random_data(db: Session = Depends(get_db)):
    first = ''.join(random.choices(string.ascii_letters, k=6))
    last = ''.join(random.choices(string.ascii_letters, k=8))

    data = BasicData(
        firstName=first,
        lastName=last,
        synced=False
    )

    db.add(data)
    db.commit()
    db.refresh(data)
    return BasicDataDto(
        id=data.id,
        firstName=data.firstName,
        lastName=data.lastName,
        synced=data.synced
    )