
from fastapi import HTTPException
from Models.guests import Guest
from Models.members import Members
from Models.responses import Invites
from Schemas.requests import SendInviteRequest
from Schemas.responses import GuestData, MembersData, ResponseInviteData


class InvitesServices:
    def __init__(self):
        pass


    def get_invite_data(self, id_invitado):


        try:
        
            invite_data = Invites.find_by_id_guest(id_invitado)
            guest_data = Guest.find_by_id(invite_data.id_invitado)

            guest_members = Guest.get_members(invite_data.id_invitado)

            guest_members_data = [MembersData(id=member.id, nombre=member.nombre, asistira=member.asistira) for member in guest_members]
            guest_data = GuestData(id_invitado=id_invitado, tipo_invitado=guest_data.tipo_invitado, nombre=guest_data.nombre, num_integrantes=guest_data.num_integrantes, 
                                   menores=guest_data.menores, adicionales=guest_data.adicionales, miembros=guest_members_data, telefono=guest_data.telefono)

            response_data = ResponseInviteData(id=invite_data.id, invitado=guest_data, respuesta=invite_data.respuesta, asistira=invite_data.asistira, buzon=invite_data.buzon)

            return response_data

        except Exception as e:
            raise HTTPException(status_code=404, detail=str(e))




    def update_invite_data(self, request: SendInviteRequest):

        try:

            if request.asistencia == "si":
                asistira = True
                guest_members = Guest.get_members(request.invitadoId)


                for member in guest_members:
                    if member.id in request.miembrosConfirmados:
                        Members.update(**{"id": member.id, "asistira": True})
                    else:
                        Members.update(**{"id": member.id, "asistira": False})

            else:
                asistira = False
                guest_members = Guest.get_members(request.invitadoId)

                for member in guest_members:
                    Members.update(**{"id": member.id, "asistira": False})
            
            
            Invites.update(**{"id_invitado": request.invitadoId, 
                                         "respuesta": True, 
                                         "asistira": asistira, 
                                         "buzon": request.mensaje})
        


            Guest.update(**{"id": request.invitadoId, "telefono": request.telefono})

            return "Invite Updated"

          

        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        

