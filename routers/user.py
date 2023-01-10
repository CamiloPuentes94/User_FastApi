### Users DB API ###

from fastapi import APIRouter,HTTPException, status
from db.models.user import User
from db.client import db_client


router = APIRouter(prefix="/userdb",
                   tags=["userdb"],
                   responses={status.HTTP_404_NOT_FOUND: {"message": "no encontrado"}}
                   )

@router.get("/")
async def user():
    pass

@router.get("/{id}") #path
async def user(id: int):
    pass

@router.get("/") # Query
async def user(id: int):
    pass

@router.post("/", response_model=User, status_code= status.HTTP_201_CREATED)
async def user(user: User):

    user_dict = dict(user)

    db_client.local.users.insert_one(user_dict)

@router.put("/")
async def user(id: int):
    pass

@router.delete("/{id}")
async def user(id: int):
    pass