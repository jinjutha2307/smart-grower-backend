from pydantic import BaseModel, Field, EmailStr
from datetime import date
from typing import List

# Simple for drop downs
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


class GrowerBase(BaseModel):
    grower_id: str = Field(..., alias="growerId")
    first_name: str = Field(..., alias="firstName")
    last_name: str = Field(..., alias="lastName")
    gender: str = Field(..., alias="gender")
    phone: str = Field(..., alias="phone")
    email: EmailStr = Field(..., alias="email")
    address: str = Field(..., alias="address")
    city: str = Field(..., alias="city")
    state: str = Field(..., alias="state")
    zip_code: str = Field(..., alias="zipCode")
    photo: str = Field(..., alias="photo")

    class Config:
        populate_by_name = True


class GrowersDataCreate(GrowerBase):
    
    citizen_id: str = Field(..., alias="citizenId")
    citizen_id_issue_date: date = Field(..., alias="citizenIdIssueDate")
    citizen_id_expiry_date: date = Field(..., alias="citizenIdExpiryDate")
    citizen_birth_date: date = Field(..., alias="citizenBirthDate")
    age: str = Field(..., alias="age")
    

    class Config:
        populate_by_name = True # allows backend to use snake_case internally
    

class GrowersDataRead(GrowerBase):
    id: int   
    created_at: date

    class Config:
        from_attributes = True
