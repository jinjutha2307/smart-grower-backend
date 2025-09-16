from sqlalchemy.orm import Session
from app import models



def get_cities(state_id: int, db: Session):
    cities = db.query(models.City).filter(models.City.state_id == state_id).all()
    return cities


def get_zipcodes(city_id: int, db: Session):
    zips = db.query(models.Zipcode).filter(models.Zipcode.city_id == city_id).all()
    return zips
    