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
    return await crud.upload_photo(file)

@router.post("/create", response_model=schemas.GrowersDataRead)
def create_growers(grower: schemas.GrowersDataCreate, db:  Session = Depends(get_db), ):
    return crud.create_growers_list(grower, db)