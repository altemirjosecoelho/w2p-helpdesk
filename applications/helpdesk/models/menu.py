# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------
# provide shortcuts for development. you can remove everything below in production
# ----------------------------------------------------------------------------------------------------------------------

if auth.user :
    tipoUsuario = (auth.user_groups)

    if "Administradores" in tipoUsuario.values():
            _app = request.application
            response.menu = [
                (T('Tickets'), False, '#', [
                (T('Em andamento'), False, URL('admin', 'index',)),
                (T('Novo'), False,URL('admin', 'ticketNew',)),
                (T('Definir Analista'), False,URL('admin', 'ticketForAnalist')),
                (T('Finalizados'), False,URL('admin', 'ticketHistoric')),
                ]),






            (T('Cadastro'), False, '#', [
                (T('Usuarios'), False, URL('admin', 'user',)),
                (T('Permissões'), False,URL('admin', 'permission',)),
                (T('Area de Ticket'), False,URL('admin', 'areaTicket')),
                (T('Tipo de Ticket'), False,URL('admin', 'typeTicket')),
                (T('Estado de  Ticket'), False,URL('admin', 'ticketsState')),
                (T('Niveis de Urgencia de Ticket'), False,URL('admin', 'urgencyTicket')),
                ]),
            ]
    if "Clientes" in tipoUsuario.values():
            response.menu = [
                (T('Tickets'), False, '#', [
                (T('Novo'), False,URL('cliente', 'ticketNew',)),
                (T('Em andamento'), False, URL('cliente', 'index',)),
                
                (T('Finalizados'), False,URL('cliente', 'ticketHistoric')),
                ]),
            ]