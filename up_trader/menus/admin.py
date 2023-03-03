from django.contrib import admin

from menus.models import Menu


class MenuAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Menu, MenuAdmin)
