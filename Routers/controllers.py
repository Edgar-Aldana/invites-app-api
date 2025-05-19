from fastapi import APIRouter
from Schemas.requests import RequestInviteData, SendInviteRequest

from Schemas.responses import SendInviteResponse, ResponseInvite
from Services.invites_services import InvitesServices

invites_router = APIRouter(prefix="/invites")


@invites_router.post("/getInviteData")
async def get_invite_data(request: RequestInviteData) -> ResponseInvite:
    
    response_data = InvitesServices().get_invite_data(request.id_invitado)
    response = ResponseInvite(success=True, message="Invite data", data=response_data)

    return response



@invites_router.put("/updateInviteData")
async def update_invite_data(request: SendInviteRequest) -> SendInviteResponse:
    
    InvitesServices().update_invite_data(request)
    response = SendInviteResponse(success=True, message="Response Received", data=None)

    return response



