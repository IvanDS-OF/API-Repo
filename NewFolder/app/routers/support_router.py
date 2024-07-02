from fastapi import APIRouter, Form
from typing import Annotated

#We define here the method of the app

router = APIRouter(
    tags=["Support"]
)

@router.post("/support-ticket")
async def create_support_ticket(tittle: Annotated[str, Form()], message: Annotated[str, Form()]):
    return {"tittle": tittle, "message": message}



