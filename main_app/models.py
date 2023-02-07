from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

INSTOCK = (
    ('A', 'in stock'),
    ('B', 'out of stock')
)

class Paint(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=50)

  def get_absolute_url(self):
    return reverse('paints_detail', kwargs={ 'pk': self. id })

  def __str__ (self):
    return f'{self.name} {self.color}'

class Mini(models.Model):
    name = models.CharField(max_length=200)
    kind = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    price = models.CharField(max_length=600)
    image = models.CharField(max_length=600)
    paints = models.ManyToManyField(Paint)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail", kwargs={"mini_id": self.id})

class Stock(models.Model):
    date = models.DateField('Last Updated')
    inventory = models.CharField(
        max_length=1,
        choices=INSTOCK,
        default=INSTOCK[0][0]
        )
    mini = models.ForeignKey(Mini, on_delete=models.CASCADE)

    def __str__ (self):
        return f"{self.get_inventory_display()} on {self.date}"
