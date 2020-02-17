from django.db import models
from django.utils.translation import gettext as _


# Create your models here.

class Reader(models.Model):
    name = models.TextField(verbose_name='Кому одолжил(Имя)', null=True, blank=True)
    borrowed = models.DateField(verbose_name='Дата выдачи книги', null=True, blank=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    full_name = models.TextField(verbose_name=_('Имя автора'))
    birth_year = models.SmallIntegerField(verbose_name=_('Дата рожденья'))
    country = models.CharField(verbose_name=_('Страна'), max_length=200)

    def __str__(self):
        return self.full_name


class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    title = models.TextField(verbose_name=_('название книги'))
    description = models.TextField(verbose_name=_('описание'))
    year_release = models.SmallIntegerField(verbose_name=_('год'))
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE, related_name='Books_Reader', blank=True, null=True)

    def __str__(self):
        return self.title
