# -*- coding: utf-8 -*-
#########################################################################
## This is controller for services
# login( email, pass, imei, phone ) return long
# Enviar os dados e o retorno sera o codigo que o sistema web gerar no cadastro
#
# syncBubbles ( id ) return String
# Enviar o maior codigo das bolhas no aplicativo e o retorno sera um xml com as bolhas maior que a do parâmetro
#
# syncCategories ( id ) return String
# Enviar o maior codigo das Categorias no aplicativo e o retorno sera um xml com as categoria maior que a do parâmetro
#
# getBubble( iduser, idbubble ) return boolean
# Na captura da bolha enviar o ID do usuário e o ID da bolha para salvar na tabela de user_bubble e retorno ok se sincronizado
#
#########################################################################
# SOAP Login
@service.soap('login',returns={'result':int},args={'email':str,'psw':str,'imei':str,'phone':str,})
def login(email,psw,imei,phone):
    if db((db.auth_user.email==email)&(db.auth_user.password==psw)).update(imei=imei,phone=phone):
        rows=db((db.auth_user.email==email)&(db.auth_user.password==psw)).select()
        for row in rows: row.id
        return row.id
    else:
        return 0

# Funções para gerar a estrutura XML      
def bubbles_xml(rows,fields):
    bubbles=[]
    for row in rows: bubbles.append(TAG.bubble(*[TAG[f](row[f]) for f in fields]))
    return TAG.bubbles(*bubbles).xml()
    
def categories_xml(rows,fields):
    categories=[]
    for row in rows: categories.append(TAG.category(*[TAG[f](row[f]) for f in fields]))
    return TAG.categories(*categories).xml()
    
# SOAP Sincronizar Bolhas
@service.soap('syncBubbles',returns={'result':str},args={'idbubble':int,})
def sync_bubbles(idbubble):
    if db((db.bubbles.id>idbubble)&(db.bubbles.status==True)).select():
        response.headers['Content-Type']='application/xml'
        return bubbles_xml(db((db.bubbles.id>idbubble)&(db.bubbles.status==True)).select(),
        ['id','address','longitude','latitude','validity','category','description']).decode('utf8')
    else:
        return 'Bolhas atualizadas'
        
# SOAP Sincronizar Categorias
@service.soap('syncCategories',returns={'result':str},args={'idcategories':int,})
def sync_categories(idcategories):
    if db(db.categories.id>idcategories).select():
        response.headers['Content-Type']='application/xml'
        return categories_xml(db(db.categories.id>idcategories).select(),
        ['id','category_name','points','description']).decode('utf8')
    else:
        return 'Categorias atualizadas'

#SOAP captura bolha
@service.soap('getBubble',returns={'result':bool},args={'iduser':int,'idbubble':int,'points':int,})
def get_bubble(iduser,idbubble,points):
    if db.user_bubble.insert(user=iduser,bubble=idbubble,user_points=points):
        user_update=db(db.auth_user.id==iduser).update(points=points)
        bubble_update=db(db.bubbles.id==idbubble).update(status=False)
        return 1
    else:
        return 0

def call():
    session.forget()
    return service()
