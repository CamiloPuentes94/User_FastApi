### Users DB API ###

from fastapi import APIRouter,HTTPException, status
from db.models.user import User
from db.client import db_client
from db.schemas.user import user_schema


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
    
    if type(search_user("email", user.email)) == User:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail= "El usuario ya existe"
            )
    user_dict = dict(user)
    del user_dict["id"]

    id = db_client.local.users.insert_one(user_dict).inserted_id
    
    new_user = user_schema(db_client.local.users.find_one({"_id": id})) 
    
    return User(**new_user)

@router.put("/")
async def user(id: int):
    pass

@router.delete("/{id}")
async def user(id: int):
    pass

def search_user(field: str, key):
    
    try:
        user = db_client.local.users.find_one({field: key})
        return User(**user_schema(user))
    except:
        return {"error": "no se a encontrado el usuario"}