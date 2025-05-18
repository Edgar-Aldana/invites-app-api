from pydantic import BaseModel


class RequestInviteData(BaseModel):
    id_invitado: str