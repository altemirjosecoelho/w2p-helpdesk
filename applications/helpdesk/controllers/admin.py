# -*- coding: utf-8 -*-



@auth.requires_membership('Administradores') 
def index(): 
    message = T("Você esta logado com uma conta de Administrador do Sistema")

    return dict(message = message)
