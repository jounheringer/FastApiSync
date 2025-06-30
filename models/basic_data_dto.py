from datetime import datetime

from pydantic import BaseModel


class BasicDataDto(BaseModel):
    id: int
    firstName: str
    lastName: str
    createdAt: datetime
    synced: bool

    class Config:
        orm_mode = True