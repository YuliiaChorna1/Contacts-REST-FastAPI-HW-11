from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, func


Base = declarative_base()


class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, index=True)
    surname = Column(String(80), nullable=False, index=True)
    email = Column(String(250), nullable=False, index=True, unique=True)
    phone = Column(String(30), nullable=False)
    birthday = Column(Date, nullable=False)
    created_at = Column('created_at', DateTime, default=func.now())
    updated_at = Column('updated_at', DateTime, default=func.now())
    address = Column(String(300), nullable=True)
    # picture = relationship("Picture", backref="contacts")

