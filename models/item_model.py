from sqlalchemy import Column, Integer, String, Float, DateTime, func
from database import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    supplier = Column(String)
    buying_price = Column(Float)
    selling_price = Column(Float)
    quantity = Column(Integer)
    date_created = Column(DateTime(timezone=True), server_default=func.now())
    date_updated = Column(DateTime(timezone=True), onupdate=func.now())
    created_by = Column(String)

# Sales table should be there : under sales there should nbe a sold price