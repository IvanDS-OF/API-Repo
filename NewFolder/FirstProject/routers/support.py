from fastapi import HTTPException, Form, File, UploadFile, Path, APIRouter
from typing import Annotated

router = APIRouter()

@router.post("/support")
async def create_support_ticket(tittle: str = Form(), message: str = Form()): ##We need to define as Form type our arguments
    return {"tittle": tittle, 
            "message": message}

