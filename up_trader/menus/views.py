from django.shortcuts import render


def show_menu(request):
    return render(request, 'menus/index.html')
