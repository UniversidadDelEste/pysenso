# -*- coding: utf-8 -*-

# try something like

def personas():
    form = SQLFORM(db.personas).process()
    return{'f': form}

def index():
    helo = 'Hola'
    return dict(p=helo)

def listas_personas():
    #datasource = db(db.personas.id>0).select()
    #table = SQLTABLE(datasource)
    #table = plugin_powerTable(datasource)
    table = plugins.powerTable
    #table.datasource = datasource
    table.datasource = db.personas
    table.uitheme = 'redmond'
    #table.keycolumn = 'id'
#    table.columns = ['personas.nombre','personas.apellido','personas.dni']
   #table.columns = ['personas.dni']
    #table.extra = dict(tooltipo=
    return dict(table=table.create())
