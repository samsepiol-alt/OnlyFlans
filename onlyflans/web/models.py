from django.db import models
from django.contrib.auth.models import User

import uuid
# Create your models here.

class Flan(models.Model):

    flan_uuid = models.UUIDField()
    name = models.CharField(max_length=64)
    descripcion = models.TextField(blank=True)
    image_url = models.URLField()
    slug = models.SlugField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_private =models.BooleanField()
    is_premium = models.BooleanField()

    def __str__(self):
        return f'{self.name}'

    class Meta:
        permissions = [
            ("can_view_premium", "Can view premium flans"),
        ]


class ContactForm(models.Model):


    contact_form_uuid = models.UUIDField(default=uuid.uuid4())
    customer_name = models.CharField(max_length=64)
    message = models.TextField(blank=True)
    customer_email = models.EmailField()

    def __str__(self):
        return f'{self.customer_name}'




class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Flan, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.quantity * self.product.price