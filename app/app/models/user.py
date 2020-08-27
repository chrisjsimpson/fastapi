from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String
# from sqlalchemy.orm import relationship

from app.db.database import Base

if TYPE_CHECKING:
    from .item import Item  # noqa: F401


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    disabled = Column(Boolean, default=False)
    is_superuser = Column(Boolean(), default=False)
    # items = relationship("Item", back_populates="owner")
