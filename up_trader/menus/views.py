from django.shortcuts import render


def show_menu(request, menu_name):
    return render(request, 'menus/index.html', {'menu_name': menu_name})
