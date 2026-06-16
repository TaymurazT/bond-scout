from sqlalchemy import Column, Integer, String, Date, Numeric

from app.db.database import Base


class Bond(Base):
    __tablename__ = "bonds"

    id = Column(Integer, primary_key=True)

    isin = Column(String(20), unique=True, nullable=False)

    ticker = Column(String(20))

    short_name = Column(String(255))

    issuer = Column(String(255))

    bond_type = Column(String(50))

    nominal = Column(Numeric)

    currency = Column(String(10))

    maturity_date = Column(Date)
