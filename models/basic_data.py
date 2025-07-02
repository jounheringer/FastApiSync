from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column

from database.database import Base


class BasicData(Base):
    __tablename__ = "basic_data"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    uid: Mapped[int] = mapped_column(index=False)
    firstName: Mapped[str] = mapped_column(String, nullable=False)
    lastName: Mapped[str] = mapped_column(String, nullable=False)
    synced: Mapped[bool] = mapped_column(Boolean, default=False)