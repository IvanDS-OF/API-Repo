from fastapi import HTTPException, Form, File, UploadFile, Path, APIRouter
from typing import Annotated

router = APIRouter(
    tags=["Support"] #The correct way to defina a tag is with a List
) ##We can separate this endpoint with a tag


@router.post("/support")
async def create_support_ticket(tittle: str = Form(), message: str = Form()): ##We need to define as Form type our arguments
    return {"tittle": tittle, 
            "message": message}

