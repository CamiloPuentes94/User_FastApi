from fastapi import FastAPI

app = FastAPI()

app.include_router(users_db.router)