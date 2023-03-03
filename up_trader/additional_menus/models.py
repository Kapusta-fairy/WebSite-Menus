from django.db import models


class AdditionalMenu(models.Model):
    menu = models.ForeignKey('menus.Menu', on_delete=models.CASCADE,
                             verbose_name='меню', default=None)
    page_name = models.CharField(max_length=200, verbose_name='имя страницы')

    def __str__(self):
        return self.menu

    class Meta:
        verbose_name = 'доп. меню'
        verbose_name_plural = 'доп. меню'
