from django.core.exceptions import ValidationError
from django.db import models

from cities.models import City


class Train(models.Model):

    name = models.CharField(max_length=50,
                            unique=True,
                            verbose_name='Number train')
    travel_time = models.PositiveSmallIntegerField(verbose_name='Travel time')
    from_city = models.ForeignKey(City,
                                  on_delete=models.CASCADE,
                                  related_name='from_city_set',
                                  verbose_name='From the city')
    to_city = models.ForeignKey(City,
                                on_delete=models.CASCADE,
                                related_name='to_city_set',
                                verbose_name='To the city')

    def __str__(self):
        return f'Train N{self.name} form {self.from_city}'

    class Mete:
        verbose_name = 'Train'
        verbose_name_plural = 'Trains'
        ordering = ['travel_time']

    def clean(self):
        if self.from_city == self.to_city:
            raise ValidationError('The places of departure and arrival cannot be the same')

        qs = Train.objects.filter(
            from_city=self.from_city, to_city=self.to_city, travel_time=self.travel_time
        ).exclude(pk=self.pk)
        if qs.exists():
            raise ValidationError('This route already exists')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
