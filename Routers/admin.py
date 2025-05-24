from fastapi import APIRouter
from Schemas.requests import LoginRequest
from Schemas.responses import AuthResponse
from Services.admin_services import AdminServices

auth_router = APIRouter(prefix="/admin")


@auth_router.post("/auth")
async def login(request: LoginRequest) -> AuthResponse:
    
    response_data = AdminServices().login(request)
    response = AuthResponse(success=True, message="Login success", data=response_data)
    
    return response
    

