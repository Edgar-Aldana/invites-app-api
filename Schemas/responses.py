from pydantic import BaseModel
from typing import List, Any


class APIResponse(BaseModel):
    
    success: bool
    message: str
    data: Any | None


class MembersData(BaseModel):
    
    id: int | str
    nombre: str
    asistira: bool


class MembersExtraData(BaseModel):
    
    id: int | str
    nombre: str



class GuestData(BaseModel):
    
    id_invitado: str
    tipo_invitado: str
    nombre: str
    num_integrantes: int
    menores: int
    adicionales: int


    miembros: List[MembersData]
    extras: List[MembersExtraData]
    telefono: str | None






class ResponseInviteData(BaseModel):
    
    id: int | str
    invitado: GuestData
    respuesta: bool
    asistira: bool | None
    buzon: str | None




class ResponseInvite(APIResponse):

    data: ResponseInviteData




class SendInviteResponse(APIResponse):

    data: str | None



class UserAuthData(BaseModel):

    token: str



class AuthResponse(APIResponse):

    data: UserAuthData