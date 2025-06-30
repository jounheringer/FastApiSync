from datetime import datetime
from sqlalchemy import Column, Integer, Boolean, DateTime, String

from database.database import Base


class BasicData(Base):
    __tablename__ = "basic_data"

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String, index=False)
    lastname = Column(String, unique=False, index=False)
    createdAt = Column(DateTime, default=datetime.now(datetime.now().astimezone().tzinfo))
    synced = Column(Boolean, unique=False, index=False)