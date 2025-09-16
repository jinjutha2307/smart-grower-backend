from fastapi import APIRouter, Depends, HTTPException
from app.database import SessionLocal
from app import schemas, crud
from sqlalchemy.orm import Session

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(
    prefix="/register",
    tags=["register"],
)

@router.get("/states/{state_id}/cities", response_model=list[schemas.CityBase])
def read_cities(state_id: int, db: Session = Depends(get_db)):
    cities = crud.get_cities(state_id, db)
    if not cities:
        raise HTTPException(status_code=404, detail="No cities found")
    return cities

@router.get("/cities/{city_id}/zipcodes", response_model=list[schemas.ZipCodeBase])
def read_zipcodes(city_id: int, db: Session = Depends(get_db)):
    zips = crud.get_zipcodes(city_id, db)
    if not zips:
        raise HTTPException(status_code=404, detail="No zip codes found")
    return zips