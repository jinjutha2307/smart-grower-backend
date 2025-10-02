from pydantic import BaseModel, EmailStr, Field
from datetime import date
from typing import List, Optional


def to_camel(string: str) -> str:
    parts = string.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])


class ZipCodeBase(BaseModel):
    id: int
    code: str

    class Config:
        from_attributes = True  #this tells Pydantic it can read SQLAlchemy objects

class CityBase(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True

class StateBase(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True

# Nested versions for hierarchical responses
class CityWithZipCodes(CityBase):
    zipcodes: List[ZipCodeBase] = []

class StateWithCities(StateBase):
    cities: List[CityBase] = []


class GrowersDataCreate(BaseModel):
    grower_id: str 
    citizen_id: str
    first_name: str
    last_name: str
    gender: str
    citizen_id_issue_date: date
    citizen_id_expiry_date: date
    citizen_birth_date: date
    age: int
    phone: str
    email: EmailStr
    address: str
    city: str
    state: str
    zip_code: str
    photo: str

    class Config:
        alias_generator = to_camel
        populate_by_name = True
        from_attributes = True
    
    

class GrowersDataRead(GrowersDataCreate):
    id: int   
    


    

class GrowersDataUpdate(BaseModel):
    citizen_id : Optional[str] = None
    first_name : Optional[str] = None
    last_name : Optional[str] = None
    gender : Optional[str] = None
    citizen_id_issue_date : Optional[date] = None
    citizen_id_expiry_date : Optional[date] = None
    citizen_birth_date : Optional[date] = None
    age : Optional[int] = None
    phone : Optional[str] = None
    email : Optional[str] = None
    address : Optional[str] = None
    state : Optional[str] = None
    city : Optional[str] = None
    zip_code : Optional[str] = None
    photo : Optional[str] = None

    class Config:
        lias_generator = to_camel
        from_attributes = True