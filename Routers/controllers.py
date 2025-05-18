from fastapi import APIRouter
from Schemas.requests import RequestInviteData
from Schemas.responses import ResponseInvite
from Services.invites_services import InvitesServices

invites_router = APIRouter(prefix="/invites")


@invites_router.post("/getInviteData")
async def get_invite_data(request: RequestInviteData) -> ResponseInvite:
    
    response_data = InvitesServices().get_invite_data(request.id_invitado)
    response = ResponseInvite(success=True, message="Invite data", data=response_data)

    return response





