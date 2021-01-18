from django.db import models


class City(models.Model):

    name = models.CharField(max_length=100, unique=True, verbose_name='Nazwa')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Miasto'
        verbose_name_plural = "Miasta"
        ordering = ['name']