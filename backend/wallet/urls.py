from django.urls import path
from .views import *

urlpatterns = [

    path('', home, name='home'),

    path(
        'dashboard/',
        dashboard,
        name='dashboard'
    ),

    path(
        'register/',
        register_view,
        name='register'
    ),

    path(
        'login/',
        login_view,
        name='login'
    ),

    path(
        'logout/',
        logout_view,
        name='logout'
    ),

    path(
        'add/',
        add_transaction,
        name='add_transaction'
    ),

    path(
    'edit/<int:id>/',
    edit_transaction,
    name='edit_transaction'
    ),

    path(
        'delete/<int:id>/',
        delete_transaction,
        name='delete_transaction'
    ),
]