from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from app.database import Base

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


class GrowersData(Base):
    __tablename__ = "growers_data"
    id = Column(Integer, primary_key=True, autoincrement=True)
    grower_id = Column(String, unique=True, index=True, nullable=False)
    citizen_id = Column(String, unique=True, index=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    citizen_id_issue_date = Column(Date, nullable=False)
    citizen_id_expiry_date = Column(Date, nullable=False)
    citizen_birth_date = Column(Date, nullable=False)
    age = Column(Integer, nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=False)
    address = Column(String, nullable=False)
    state = Column(String, nullable=False)
    city = Column(String, nullable=False)
    zip_code = Column(String, nullable=False)
    photo = Column(String, nullable=False)




