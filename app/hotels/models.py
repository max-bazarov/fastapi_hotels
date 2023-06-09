from sqlalchemy import JSON, Column, ForeignKey, Integer, String

from app.database import Base


class Hotel(Base):
    __tablename__ = 'hotel'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    services = Column(JSON)
    rooms_quantity = Column(Integer, nullable=False)
    image_id = Column(Integer)
