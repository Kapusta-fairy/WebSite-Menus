from django.urls import path

from menus.views import show_menu

urlpatterns = [
    path('', show_menu, name='show_menu'),
]
