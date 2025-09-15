from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models, schemas
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Adjust as needed for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 1.Get cities by state_id
@app.get("/states/{state_id}/cities", response_model=list[schemas.CityBase])
def get_cities(state_id: int, db: Session = Depends(get_db)):
    cities = db.query(models.City).filter(models.City.state_id == state_id).all()
    if not cities:
        return HTTPException(status_code=404, detail="No cities found")
    else:
        return cities
     

# 2.Get zipcodes by city_id
@app.get("/cities/{city_id}/zipcodes", response_model=list[schemas.ZipCodeBase])
def get_zipcodes(city_id: int, db: Session = Depends(get_db)):
    zips = db.query(models.Zipcode).filter(models.Zipcode.city_id == city_id).all()
    if not zips:
        return HTTPException(status_code=404, detail="No zip codes found")
    else:
        return zips
