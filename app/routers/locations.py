from fastapi import APIRouter, Depends, HTTPException
from app.database import get_db
from app import schemas, crud
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/locations",
    tags=["locations"],
)

@router.get("/states/{state_id}/cities", response_model=list[schemas.CityBase])
def read_cities(state_id: int, db: Session = Depends(get_db)):
    cities = crud.get_cities(state_id, db)
    return cities

@router.get("/cities/{city_id}/zipcodes", response_model=list[schemas.ZipCodeBase])
def read_zipcodes(city_id: int, db: Session = Depends(get_db)):
    zips = crud.get_zipcodes(city_id, db)
    return zips


