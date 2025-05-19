from typing import List, Optional
from pydantic import BaseModel

class RequestInviteData(BaseModel):
    id_invitado: str



class GuestData(BaseModel):
    id_invitado: str
    telefono: str
    miembrosConfirmados: List[int]


class SendInviteRequest(BaseModel):
    
    invitadoId: str
    
    asistencia: str
    miembrosConfirmados: List[int]

    telefono: str
    mensaje: str | None
    
    agregarExtras: bool
    extras: Optional[List[int]] = []
