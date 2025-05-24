from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum
from Routers.controllers import invites_router
from Routers.admin import auth_router

import Models as models
from Data.connection_db import engine


try:
    models.Base.metadata.create_all(bind=engine)
except Exception as e:
    print(e)




app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(invites_router)
app.include_router(auth_router)


@app.get("/")
async def root():
    return {"message": "Test API Success"}



handler = Mangum(app)