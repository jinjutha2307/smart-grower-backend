from sqlalchemy.orm import Session
from app import models, schemas
from fastapi import UploadFile, File
import os
from app.utils.exceptions import not_found, bad_request, conflict, unauthorized


def get_cities(state_id: int, db: Session):
    cities = db.query(models.City).filter(models.City.state_id == state_id).all()
    if not cities:
        raise not_found(detail="cities")
    return cities


def get_zipcodes(city_id: int, db: Session):
    zips = db.query(models.Zipcode).filter(models.Zipcode.city_id == city_id).all()
    if not zips:
        raise not_found(detail="zip codes")
    return zips

async def upload_photo(file: UploadFile = File(...)):
    if not file.filename.endswith((".jpg", ".jpeg", ".png", ".webp")):
        raise bad_request(detail="Only JPG, PNG, WEBP files allowed")
    os.makedirs("uploads", exist_ok=True)
    file_path = f"uploads/{file.filename}" #server’s private storage

    with open(file_path, "wb") as f:
        f.write(await file.read())

    file_url = f"/static/{file.filename}"  #public URL to access the file
    return {"url": file_url}


def create_growers_list(grower: schemas.GrowersDataCreate, db: Session):
    existing = db.query(models.GrowersData).filter((models.GrowersData.grower_id == grower.grower_id) or (models.GrowersData.citizen_id == grower.citizen_id)).first()
    if existing:
        raise conflict(detail="Grower ID or Citizen ID already exists")

    db_grower = models.GrowersData(**grower.dict())
    db.add(db_grower)
    db.commit()
    db.refresh(db_grower)
    return db_grower


def get_grower(db: Session):
    growers = db.query(models.GrowersData).all()
    if not growers:
        raise not_found(detail="growers data")
    return growers
    