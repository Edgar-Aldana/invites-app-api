from fastapi import FastAPI
from mangum import Mangum
from Routers.controllers import invites_router

import Models as models
from Data.connection_db import engine


try:
    models.Base.metadata.create_all(bind=engine)
except Exception as e:
    print(e)




app = FastAPI()

app.include_router(invites_router)


@app.get("/")
async def root():
    return {"message": "Test API Success"}



handler = Mangum(app)