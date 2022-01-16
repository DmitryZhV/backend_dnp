from django.db import models

# Create your models here.


class Format(models.Model):
    name = models.CharField(max_length=24, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = 'Формат'
        verbose_name_plural = 'Форматы'

class Price(models.Model):
    format = models.ForeignKey(Format, blank=True, null=True, default=None, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "{} - {}".format(self.format, self.price)

    class Meta:
        verbose_name = 'Цена формата'
        verbose_name_plural = 'Цены'