from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=150, verbose_name='имя')
    slug = models.SlugField(max_length=20, unique=True, db_index=True,
                            verbose_name="slug")
    dependence = models.ForeignKey('Menu', on_delete=models.CASCADE,
                                   verbose_name='зависимость', null=True,
                                   blank=True)
    url = models.CharField(max_length=200, verbose_name='ссылка')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'меню'
        verbose_name_plural = 'меню'
