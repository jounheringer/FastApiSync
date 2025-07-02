from typing import Optional, List

from pydantic import BaseModel


class BasicDataDto(BaseModel):
    uid: Optional[int]
    id: Optional[int]
    firstName: str
    lastName: str
    synced: bool

    class Config:
        orm_mode = True