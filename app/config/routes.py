"""
    Routes Configuration File

    Put Routing rules here
"""
from system.core.router import routes

routes['default_controller'] = 'Users'
routes['POST']['/users/process'] = 'Users#create'
routes['/logout'] = 'Users#logout'
routes['POST']['/users/login'] = 'Users#submitlogin'
routes['/dashboard'] = 'Items#dashboard'
routes['/wish_item/add'] = 'Items#add'
routes['POST']['/wish_item/create'] = 'Items#create'
routes['POST']['/wish_item/wish'] = 'Items#wish'
routes['POST']['/wish_item/remove'] = 'Items#kill_dream'
routes['POST']['/wish_item/destroy'] = 'Items#kill_everyones_dream'
routes['/wish_items/<id>'] = 'Items#item_view'