# -*- coding: utf-8 -*-



@auth.requires_membership('Administradores') 
def index(): 
    titulo = T("Bem vindo")

    grid = SQLFORM.smartgrid(db.ticket,csv=None,details=None,advanced_search=None,)

    return dict(titulo = titulo, grid=grid)
@auth.requires_membership('Administradores') 
def user(): 
    #response.view = 'generic.html'
    titulo = T("Cadastro de Usuarios")

    grid = SQLFORM.smartgrid(db.auth_user, linked_tables=['auth_membership'],csv=None,details=None,advanced_search=None,links=None,)

    




    return dict(titulo = titulo, grid=grid)
def test():

    
    rows = db(db.auth_membership.group_id == 2).select(db.auth_membership.ALL)

    for row in rows: 
        print (row)
        
    return dict(rows  = rows)

@auth.requires_membership('Administradores') 
def permission(): 
    titulo = T("Cadastro de permissões")


    grid = SQLFORM.grid(db.auth_permission,csv=None,details=None,advanced_search=None,orderby='group_id',fields = [db.auth_permission.group_id, db.auth_permission.name])

    return dict(titulo = titulo, grid=grid)

@auth.requires_membership('Administradores') 
def ticketsState(): 
    titulo = T("Estados de tickets")


    grid = SQLFORM.grid(db.stateTicket,csv=None,details=None,advanced_search=None,orderby='id',fields = [db.stateTicket.name, db.stateTicket.description])

    return dict(titulo = titulo, grid=grid)

@auth.requires_membership('Administradores') 
def urgencyTicket(): 
    titulo = T("Urgencia de tickets")


    grid = SQLFORM.grid(db.urgencyTicket,csv=None,details=None,advanced_search=None, orderby='id',fields = [db.urgencyTicket.name, db.urgencyTicket.description , db.urgencyTicket.slaTime])

    return dict(titulo = titulo, grid=grid)
def areaTicket(): 
    titulo = T("Area de tickets")


    grid = SQLFORM.grid(db.areaTicket,csv=None,details=None,advanced_search=None, orderby='id',fields = [db.areaTicket.name, db.areaTicket.description ])

    return dict(titulo = titulo, grid=grid)
def typeTicket(): 
    titulo = T("Tipo de tickets")


    grid = SQLFORM.grid(db.typeTicket,csv=None,details=None,advanced_search=None, orderby='id',fields = [db.typeTicket.name, db.typeTicket.description])

    return dict(titulo = titulo, grid=grid)