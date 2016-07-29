# -*- coding: utf-8 -*- 

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

#response.title = request.application
response.subtitle = T('Capture bolhas e ganhe prêmios!')
response.meta.author = 'Thomas Metz e Vinicius Vollrath'
response.meta.description = 'Jogo para celular com recursos de realidade aumentada e GPS.'
response.meta.keywords = 'game, jogo, android, mobile, bolhas, bubbles, gps, maps, premios'
response.meta.copyright = 'Copyright 2007-2010'
#########################################
## Make your own menus
##########################################
response.menu = [
    (T('Home'), False, URL(request.application,'default','index'), []),
    (T('Download'), False, URL(request.application,'default','download'), []),
    (T('The game'), False, URL(request.application,'default','game'), []),
    (T('Bubbles'), False, URL(request.application,'default','bubbles'), []),
    (T('Classification'), False, URL(request.application,'default','classification'), []),
    (T('Contact'), False, URL(request.application,'default','contact'), []),
    (T('Blog'), False, 'http://blog.ploc.me', [])
    ]
    
response.menu_partner = [
    (T('Create bubble'), False, URL(request.application,'manager','create_bubbles'), []),
    (T('Create categories'), False, URL(request.application,'manager','create_categories'), []),
    ]
    
response.menu_admin = [
    (T('Create bubble'), False, URL(request.application,'manager','create_bubbles'), []),
    (T('Create categories'), False, URL(request.application,'manager','create_categories'), []),
    ]
