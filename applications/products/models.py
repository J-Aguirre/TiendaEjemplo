from django.db import models

# Create your models here.

class Supplier(models.Model):
    """Model definition for Supplier."""

    # TODO: Define fields here
    company = models.CharField('Empresa', max_length=50)
    name = models.CharField('Representante', max_length=50)
    phone = models.CharField('Telefono', max_length=50)

    class Meta:
        """Meta definition for Supplier."""

        verbose_name = 'Supplier'
        verbose_name_plural = 'Suppliers'

    def __str__(self):
        return self.company
    

class Product(models.Model):
    """Model definition for Product."""

    # TODO: Define fields here
    name = models.CharField('Nombre', max_length=128)
    buy_price = models.FloatField('Precio de Compra', default=0.0)
    sell_price = models.FloatField('Precio de Venta', default=0.0)
    stock = models.IntegerField('Stock')
    available = models.BooleanField('Disponible', default=True)
    supplier = models.ManyToManyField(Supplier)

    class Meta:
        """Meta definition for Product."""

        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name

