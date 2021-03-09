from django.db import models

class Data(models.Model):
    '''Данные'''
    temp = models.DecimalField('Температура', max_digits=5, decimal_places=2)
    lightning = models.DecimalField('Влажность', max_digits=5, decimal_places=2)
    humidity = models.DecimalField('Освещенность', max_digits=5, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Данные'
        verbose_name_plural = 'Данные'