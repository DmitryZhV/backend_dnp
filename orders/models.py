from django.db import models
from settings.models import Format

# Create your models here.
class StatusOrder(models.Model):
    name = models.CharField(max_length=24, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    

    def __str__(self):
        return "Статус %s" % self.name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

class Order(models.Model):
    
    total_qty = models.IntegerField(default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.ForeignKey(StatusOrder, on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True, auto_now=False)
    updated=models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Заказ %s %s" % (self.id, self.status.name)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def save(self, *args, **kwargs):

        super(Order, self).save(*args, **kwargs)

 
class ItemInOrder(models.Model):
    order = models.ForeignKey(Order, blank=True, null=True, default=None, on_delete=models.PROTECT)
    format = models.ForeignKey(Format, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='order_image/%s/' % order )
    qty = models.IntegerField(default=1)
    price_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_croup = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    
    

    # def __str__(self):
    #     return " %s" % self.product.name

    class Meta:
        verbose_name = 'Фото в заказе'
        verbose_name_plural = 'Изображения в заказе'