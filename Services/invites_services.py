
from fastapi import HTTPException
from Models.extras import Extras
from Models.guests import Guest
from Models.members import Members
from Models.responses import Invites
from Schemas.requests import SendInviteRequest
from Schemas.responses import GuestData, MembersData, MembersExtraData, ResponseInviteData


class InvitesServices:
    def __init__(self):
        pass


    def get_invite_data(self, id_invitado):


        try:
        
            invite_data = Invites.find_by_id_guest(id_invitado)
            guest_data = Guest.find_by_id(invite_data.id_invitado)

            guest_members = Guest.get_members(invite_data.id_invitado)
            guest_extras = Extras.find_by_filter(id_invitado=invite_data.id_invitado)

            guest_members_data = [MembersData(id=member.id, nombre=member.nombre, asistira=member.asistira) for member in guest_members]
            guest_extras_data = [MembersExtraData(id=extra.id, nombre=extra.nombre) for extra in guest_extras]
        
            
            
            guest_data = GuestData(id_invitado=id_invitado, tipo_invitado=guest_data.tipo_invitado, nombre=guest_data.nombre, 
                                   num_integrantes=guest_data.num_integrantes, menores=guest_data.menores, adicionales=guest_data.adicionales, 
                                   miembros=guest_members_data, extras=guest_extras_data, telefono=guest_data.telefono)

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


                extras_db = Extras.find_by_filter(id_invitado=request.invitadoId)
                if len(extras_db) != len(request.extras):
                    Extras.delete_by_filter(id_invitado=request.invitadoId)

                for extra in request.extras:
                    extra_db = Extras.find_by_filter(id=extra.id, id_invitado=request.invitadoId)
                    if not extra_db:
                        Extras.create(**{"id_invitado": request.invitadoId, "nombre": extra.nombre})
                    else:
                        Extras.update(**{"id": extra_db[0].id, "id_invitado": request.invitadoId, "nombre": extra.nombre})


            else:
                asistira = False
                guest_members = Guest.get_members(request.invitadoId)

                for member in guest_members:
                    Members.update(**{"id": member.id, "asistira": False})
                
                Extras.delete_by_filter(id_invitado=request.invitadoId)

            
            Invites.update(**{"id_invitado": request.invitadoId, 
                                         "respuesta": True, 
                                         "asistira": asistira, 
                                         "buzon": request.mensaje})
        


            Guest.update(**{"id": request.invitadoId, "telefono": request.telefono})

            return "Invite Updated"

          

        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        

