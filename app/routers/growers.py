from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from app.database import get_db
from app import schemas, crud
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/growers",
    tags=["growers"],
)


@router.post("/upload-photo")
async def upload_photo(file: UploadFile = File(...)):
    res = await crud.upload_photo(file)
    return res

@router.post("/create", response_model=schemas.GrowersDataRead)
def create_growers(grower: schemas.GrowersDataCreate, db:  Session = Depends(get_db), ):
    res = crud.create_growers_list(grower, db)
    return res

@router.get("/", response_model=list[schemas.GrowersDataRead])
def read_growers(db: Session = Depends(get_db)):
    growers =  crud.get_grower(db)
    return growers

@router.get("/{grower_id}", response_model=schemas.GrowersDataRead)
def read_grower_by_id(grower_id: str, db: Session = Depends(get_db)):
    grower = crud.get_grower_by_id(grower_id, db)
    return grower

@router.patch("/update/{grower_id}", response_model=schemas.GrowersDataRead)
def update_grower(grower_id: str, grower_update: schemas.GrowersDataUpdate, db: Session = Depends(get_db)):
    updated_grower = crud.update_grower(grower_id, grower_update, db)
    return updated_grower
