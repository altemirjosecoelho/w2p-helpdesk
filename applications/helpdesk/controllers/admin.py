# -*- coding: utf-8 -*-



@auth.requires_membership('Administradores') 
def index(): 
    titulo = T("Bem vindo")



    return dict(titulo = titulo)
@auth.requires_membership('Administradores') 
def user(): 
    titulo = T("Cadastro de Usuarios")


    grid = SQLFORM.smartgrid(db.auth_user, linked_tables=['auth_membership'],csv=None,details=None,advanced_search=None,links=None,)

    return dict(titulo = titulo, grid=grid)
@auth.requires_membership('Administradores') 
def permission(): 
    titulo = T("Cadastro de permissões")


    grid = SQLFORM.grid(db.auth_permission,csv=None,details=None,advanced_search=None,orderby='group_id',fields = [db.auth_permission.group_id, db.auth_permission.name])

    return dict(titulo = titulo, grid=grid)
@auth.requires_membership('Administradores') 
def ticketsState(): 
    titulo = T("Cadastro Estados de tickets")


    grid = SQLFORM.grid(db.stateTicket,csv=None,details=None,advanced_search=None,orderby='id',fields = [db.stateTicket.name, db.stateTicket.description])

    return dict(titulo = titulo, grid=grid)