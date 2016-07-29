# -*- coding: utf-8 -*-
#formulário para criação de categorias
@auth.requires_membership('admin')
def create_categories():
    return dict(form=crud.create(db.categories))
  
#formulário para a criação de bolhas
@auth.requires_membership('admin')
def create_bubbles():
    return dict(form=crud.create(db.bubbles))

#função para gerar a estrutura xml da tabela bubbles   
def export_bubbles(rows,fields):
    bubbles=[]
    for row in rows: bubbles.append(TAG.bubble(*[TAG[f](row[f]) for f in fields]))
    return TAG.bubbles(*bubbles).xml()

#função para gerar o xml com os dados da tabela bubbles
def list_bubbles():
    response.headers['Content-Type']='application/xml'
    return export_bubbles(db(db.bubbles.status==True).select(),
        ['address','latitude','longitude','validity','category','description'])
