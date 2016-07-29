# -*- coding: utf-8 -*- 
def index():
    response.flash = T('You are successfully running web2py.')
    return dict(message=T('Hello World'))

def user():
    """
    exposes:
    http://..../[app]/default/user/login 
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())

def download():
    return dict()

def game():
    return dict()
    
def bubbles():
    return dict()
    
def classification():
    gamers=db(db.auth_user.points>0).select(orderby=~db.auth_user.points)
    return dict(gamers=gamers)
   
def contact():
    #cretes the form       
    form = SQLFORM(db.contact,formstyle='divs',submit_button='Enviar')
        
    #validation of the form   
    if form.accepts(request.vars, session):
            
        try:
            subject='Formulário de contato Ploc.Me'
            email_user(sender=form.vars.email,\
                       message='Tel: %s - Data: %s '\
                                % (form.vars.tel,form.vars.date),\
                       subject=subject)
        except Exception, e:
            pass               
              
        response.flash = 'Aceito'
        
        #Success Message
        form = DIV(H3('Mensagem enviada, entraremos em contato em breve.'))
            
    elif form.errors:
        response.flash = 'Erros'
                                    
    return dict(form=form)
