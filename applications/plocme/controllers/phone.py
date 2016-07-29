# coding: utf8
def index():
    """
    exposes:
    http://..../[app]/phone/user/login 
    http://..../[app]/phone/user/logout
    http://..../[app]/phone/user/register
    http://..../[app]/phone/user/profile
    http://..../[app]/phone/user/retrieve_password
    http://..../[app]/phone/user/change_password
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())
