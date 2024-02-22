from django.db import models

# Create your models here.


class Stage(models.Model):
    month = ['enero']
    stage = models.IntegerField(verbose_name = 'Etapa')
    aplication_date = models.DateField(verbose_name = "Fecha de la aplicación")


@property
def year(self):
    return self.application_date.year

def __str__(self):
    return f"{ self.stage } - { self.year }"

class Meta:
    verbose_name = 'examen',
    verbose_name_plural = 'examenes'