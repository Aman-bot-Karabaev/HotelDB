from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    avatar = models.ImageField(
        upload_to="users/avatars/",
        null=True, # для базы
        blank=True, # для формы 
        verbose_name="Фото профиля"
    )
    phone = models.CharField("Номер телефона", max_length=14,null=False, default=False)

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    def __str__(self):
        return str(self.username)


    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    

class Comment(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField("Отзыв")


    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ["-created"]

    def str(self):
        return f"{self.content}"[:100]


class Employees(models.Model):
    avatar = models.ImageField(
        upload_to="users/avatars/",
        null=True, # для базы
        blank=True, # для формы 
        verbose_name="Фото профиля"
    )
    full_name=models.CharField(max_length=100,null=False,default=None)
    email=models.CharField(max_length=100,null=False)
    post = models.CharField(max_length=50,null=False,default=None)
    