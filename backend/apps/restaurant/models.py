from django.db import models
from backend.apps.accounts.models import User
from backend.apps.rooms.models import Contact
# Create your models here.

class RestaurantBook(models.Model):
    name=models.CharField(max_length=100,null=False,default=None)
    phone = models.CharField("Номер телефона", max_length=14,null=False)
    email = models.CharField(max_length=100,null=False)
    time = models.DateTimeField("Время брони", null=True)
    persons = models.PositiveSmallIntegerField("Persons",null=True,default=1)
    message=models.TextField(max_length=2000,null=True)


    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    

class Category(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def str(self):
        return f"{self.name}"


class RestaurantMenu(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,related_name="m_category",null=True)
    price  = models.DecimalField(max_digits=20, decimal_places=2)
    info = models.TextField("Описание")

    def print_menu_by_category():
        categories = Category.objects.all()
        for category in categories:
            items = RestaurantMenu.objects.filter(category=category)
            for item in items:
                print(f"{item.name} - {item.price}")