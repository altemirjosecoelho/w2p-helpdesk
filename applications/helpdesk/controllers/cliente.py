# -*- coding: utf-8 -*-
# tente algo como


@auth.requires_membership('Clientes') 
def index(): 
    message = T("Você esta logado com uma conta de Cliente do Sistema")

    return dict(message = message)
