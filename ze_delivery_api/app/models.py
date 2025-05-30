from sqlalchemy import Column, Integer, String, Text
from app.database import Base



class Partner(Base):
    __tablename__ = "partners"

    id = Column(Integer, primary_key=True, index=True)
    trading_name = Column(String(255), nullable=False)
    owner_name = Column(String(255), nullable=False)
    document = Column(String(18), unique=True, nullable=False)
    coverage_area = Column(Text, nullable=False)  # GeoJSON como string
    address = Column(Text, nullable=False)        # GeoJSON como string
