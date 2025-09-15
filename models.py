from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class State(Base):
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)

    # relationship -> a state has many cities
    cities = relationship("City", back_populates="state", cascade="all, delete-orphan")

class City(Base):
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    # foreign key to State
    state_id = Column(Integer, ForeignKey("states.id"), index=True, nullable=False)

    # relationship -> a city belongs to state
    state = relationship("State", back_populates="cities")

    # relationship -> a city has many zip codes
    zipcodes = relationship("Zipcode", back_populates="city", cascade="all, delete-orphan")

class Zipcode(Base):
    __tablename__ = "zipcodes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String, index=True, nullable=False)
    city_id = Column(Integer, ForeignKey("cities.id"), index=True, nullable=False)

    # Many zipcodes to one city relationship
    city = relationship("City", back_populates="zipcodes")
