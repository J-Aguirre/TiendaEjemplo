from django.db import models

# Create your models here.

class User(models.Model):
    """Model definition for User."""

    # TODO: Define fields here
    first_name = models.CharField('Nombre', max_length=50)
    last_name = models.CharField('Apellido', max_length=50)
    age = models.IntegerField('Edad')
    email = models.CharField('COrreo Electronico', max_length=50)
    password = models.CharField('Contraseña', max_length=50)

    class Meta:
        """Meta definition for User."""

        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.first_name + '-' + self.last_name
