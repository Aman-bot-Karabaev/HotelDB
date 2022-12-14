from django.db import models

# Create your models here.
from backend.apps.accounts.models import User


class Contact(models.Model):
    name=models.CharField(max_length=100,null=False)
    email=models.CharField(max_length=100,null=False)
    message=models.TextField(max_length=2000,null=True)
    phone = models.CharField("Номер телефона", max_length=14,null=False)
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def str(self):
        return f"{self.name}"

class RoomImage(models.Model):
    image = models.ImageField("Фото", upload_to="rooms/imgs/", null=True)



class Rooms(models.Model):
    info = models.TextField("Описание")
    price = models.DecimalField(max_digits=20, decimal_places=2)
    picture = models.ImageField("Фото", upload_to="rooms/imgs/")
    room_image = models.ForeignKey(RoomImage, on_delete=models.CASCADE, null=True)
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    persons = models.CharField("persons",max_length=20,null=True)
    

    class Meta:
        verbose_name = "Номер"
        verbose_name_plural = "Номера"

    def __str__(self):
        return f"Room #{self.id}"



from django.utils.timezone import now
class Booking(models.Model):
    BOOKING_STATUS_DRAFT = "draft"
    BOOKING_STATUS_NEW = "new"
    BOOKING_STATUS_CONFIRMED = "confirmed"
    BOOKING_STATUS_REJECTED = "rejected"
    BOOKING_STATUS_FINISHED = "finished"
    BOOKING_STATUSES = (
        (BOOKING_STATUS_DRAFT, 'Черновик'),
        (BOOKING_STATUS_NEW, 'Новый'),
        (BOOKING_STATUS_CONFIRMED, 'Подтвержден'),
        (BOOKING_STATUS_REJECTED, 'Отменен'),
        (BOOKING_STATUS_FINISHED, 'Завершен'),
    )
    
    customer = models.ForeignKey(Contact, on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    check_in = models.DateField("Дата заезда", null=True)
    check_out = models.DateField("Дата выезда", null=True)
    adult = models.PositiveSmallIntegerField("Adult",null=True,default=1)
    children = models.PositiveSmallIntegerField("Children",null=True, default=0 )
    sum = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    room = models.ForeignKey(Rooms, related_name="rooms", null=True, blank=True,on_delete=models.SET_NULL)
    status = models.CharField("Status", choices=BOOKING_STATUSES, max_length=10, default=BOOKING_STATUS_DRAFT)
    created = models.DateTimeField("Created",auto_now_add=True, null=True )

    def get_days(self):
        r = self.check_out-self.check_in
        return r.days

    @property
    def get_booking_price(self):
        r = self.room.price * self.get_days()
        return r 
    
    
