from sqlalchemy.orm import Session
from app import models, schemas
from fastapi import UploadFile, File
import os



def get_cities(state_id: int, db: Session):
    cities = db.query(models.City).filter(models.City.state_id == state_id).all()
    return cities


def get_zipcodes(city_id: int, db: Session):
    zips = db.query(models.Zipcode).filter(models.Zipcode.city_id == city_id).all()
    return zips

async def upload_photo(file: UploadFile = File(...)):
    os.makedirs("uploads", exist_ok=True)
    file_path = f"uploads/{file.filename}" #server’s private storage
    with open(file_path, "wb") as f:
        f.write(await file.read())

    file_url = f"/static/{file.filename}"  #public URL to access the file
    return {"url": file_url}


def create_growers_list(grower: schemas.GrowersDataCreate, db: Session):
    db_grower = models.GrowersData(**grower.dict())
    db.add(db_grower)
    db.commit()
    db.refresh(db_grower)
    return db_grower
    