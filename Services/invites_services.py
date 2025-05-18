
from fastapi import HTTPException
from Models.guests import Guest
from Models.responses import Invites
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



        

