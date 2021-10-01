# -*- coding: utf-8 -*-

@auth.requires_membership('Analistas') 
def index(): 
    message = T("Você esta logado com uma conta de Analista do Sistema")

    return dict(message = message)