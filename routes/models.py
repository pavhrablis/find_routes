from django.db import models

from cities.models import City
from trains.models import Train


class Route(models.Model):

    name = models.CharField(max_length=50,
                            unique=True,
                            verbose_name='Name route')
    travel_times = models.PositiveSmallIntegerField(verbose_name='All travel time')
    from_city = models.ForeignKey(City,
                                  on_delete=models.CASCADE,
                                  related_name='route_from_city_set',
                                  verbose_name='From the city')
    to_city = models.ForeignKey(City,
                                on_delete=models.CASCADE,
                                related_name='route_to_city_set',
                                verbose_name='To the city')

    trains = models.ManyToManyField(Train, verbose_name='List trains')

    def __str__(self):
        return f'Route N{self.name} form {self.from_city}'

    class Mete:
        verbose_name = 'Route'
        verbose_name_plural = 'Routes'
        ordering = ['travel_times']
