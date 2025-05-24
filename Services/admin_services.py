from fastapi import HTTPException

from Schemas.requests import LoginRequest
from Schemas.responses import UserAuthData
from Models.users_admin import UsersAdmin
from jose import jwt

class AdminServices():

    
    def login(self, request: LoginRequest):

        username = request.email
        password = request.password

        try:
            user_db = UsersAdmin.find_by_filter(username=username, password=password)

            if not user_db:
                raise HTTPException(status_code=400, detail="Incorrect username or password")
            if user_db.disabled:
                raise HTTPException(status_code=400, detail="Inactive user")
            if user_db.password != password:
                raise HTTPException(status_code=400, detail="Incorrect username or password")

            token = jwt.encode({"sub": user_db.username}, key="secret", algorithm="HS256")
            return UserAuthData(token=token)

        except Exception as e:
            raise HTTPException(status_code=404, detail=str(e))


        

