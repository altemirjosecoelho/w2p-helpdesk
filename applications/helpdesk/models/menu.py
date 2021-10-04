# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------

response.menu = [
    (T('Home'), False, URL('default', 'index'), [])
]

# ----------------------------------------------------------------------------------------------------------------------
# provide shortcuts for development. you can remove everything below in production
# ----------------------------------------------------------------------------------------------------------------------

if auth.user :
    tipoUsuario = (auth.user_groups)

    if "Administradores" in tipoUsuario.values():
            _app = request.application
            response.menu += [
            (T('My Sites'), False, URL('default', 'site')),

            (T('Tickets'), False, '#', [
                (T('Em andamento'), False, URL('admin', 'ticketActive',)),
                (T('Novo'), False,URL('admin', 'ticketNew',)),
                (T('Definir Analista'), False,URL('admin', 'ticketForAnalist')),
                (T('Finalizados'), False,URL('admin', 'ticketHistoric')),
                ]),






            (T('Cadastro'), False, '#', [
                (T('Usuarios'), False, URL('admin', 'user',)),
                (T('Permissões'), False,URL('admin', 'permission',)),
                (T('Estados possiveis do Ticket'), False,URL('admin', 'ticketsState')),
                (T('Niveis de Urgencia do Ticket'), False,URL('admin', 'urgenceTicket')),
                ]),
            ]

