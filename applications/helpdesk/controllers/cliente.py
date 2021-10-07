# -*- coding: utf-8 -*-
# tente algo como

from gluon.tools import Crud
crud = Crud(db)

@auth.requires_membership('Clientes') 
def index(): 

    db.ticket.editar =    Field.Virtual(lambda row: A("Editar",_class="btn btn-alert", _href=URL('editar',args=row.ticket.id)))
    db.ticket.editar.label = 'Editar'

    Aberto = db(db.stateTicket.name == 'Aberto' ).select().first().id
    Finalizado = db(db.stateTicket.name == 'Finalizado' ).select().first().id


    query = (db.ticket.usuario == auth.user_id)
    query &= (db.ticket.Estado != Finalizado )
    grid = SQLFORM.grid(query ,create = False,csv=None,details=None,advanced_search=None, orderby='id',maxtextlength=50,deletable=False, editable=False, fields = [db.ticket.id ,db.ticket.Tipo, db.ticket.Area , db.ticket.Urgencia , db.ticket.Estado , db.ticket.description, db.ticket.editar ],formargs={})


    
 


    return dict (grid=grid )
def ticketHistoric():
    response.view = 'cliente/index.html'
    db.ticket.editar =    Field.Virtual(lambda row: A("Editar",_class="btn btn-alert", _href=URL('editar',args=row.ticket.id)))
    db.ticket.editar.label = 'Editar'

    Aberto = db(db.stateTicket.name == 'Aberto' ).select().first().id
    Finalizado = db(db.stateTicket.name == 'Finalizado' ).select().first().id


    query = (db.ticket.usuario == auth.user_id)
    query &= (db.ticket.Estado == Finalizado )
    grid = SQLFORM.grid(query ,create = False,csv=None,details=None,advanced_search=None, orderby='id',maxtextlength=50,deletable=False, editable=False, fields = [db.ticket.id ,db.ticket.Tipo, db.ticket.Area , db.ticket.Urgencia , db.ticket.Estado , db.ticket.description,],formargs={})



    return dict (grid=grid )

def ticketNew():
    #query = (db.ticket.usuario == auth.user.id)
    db.ticket.Estado.default = 1
    db.ticket.usuario.writable = False
    db.ticket.usuario.readable = False
    db.ticket.analista.writable = False
    db.ticket.analista.readable = False
    db.ticket.Estado.writable = False
    

    form = SQLFORM(db.ticket )
    form.vars.usuario = auth.user_id

    if form.accepts(request, session):
        response.flash = 'form accepted'
        redirect(URL('index'))
    elif form.errors:
        response.flash = 'form has errors'
 
    return dict(form=form)


def editar():
    pid = request.args(0) or redirect(URL('index'))
    userticket = db(db.ticket.id == pid ).select().first().usuario
    if (userticket == auth.user_id):
        db.ticket.usuario.writable = False
        db.ticket.usuario.readable = False
        db.ticket.analista.writable = False
        db.ticket.analista.readable = False
        db.ticket.Estado.writable = False
        form = SQLFORM(db.ticket , pid)
        if form.accepts(request, session):
            response.flash = 'form accepted'
            redirect(URL('index'))
        elif form.errors:
            response.flash = 'form has errors'

    else:
        form = T("Você não tem permissão para alterar este ticket")
    return dict(form=form)
