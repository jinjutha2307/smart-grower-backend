from pydantic import BaseModel
from typing import List

# Simple for drop downs
class ZipCodeBase(BaseModel):
    id: int
    code: str

    class Config:
        orm_mode = True

class CityBase(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class StateBase(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

# Nested versions for hierarchical responses
class CityWithZipCodes(CityBase):
    zipcodes: List[ZipCodeBase] = []

class StateWithCities(StateBase):
    cities: List[CityBase] = []
