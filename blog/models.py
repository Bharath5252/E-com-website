from django.core.exceptions import TooManyFieldsSent
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, UserManager 
from django.db.models.fields.files import ImageField
from PIL import Image

class post(models.Model):
    title= models.CharField(max_length=100)
    content=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey( User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Level1(models.Model):
    name = models.CharField(max_length = 40)
    price = models.IntegerField()
    rating = models.FloatField(blank=True, null = True)
    quantity = models.IntegerField(blank=True)
    image=models.ImageField(default='default.jpg', upload_to='level1_pics')

    def __str__(self):
        return self.name

    def save(self):
        super().save()

        img=Image.open(self.image.path)

        if img.height>300 or img.width>300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Level1(models.Model):
    name = models.CharField(max_length = 40)
    price = models.IntegerField()
    rating = models.FloatField(blank=True, null = True)
    quantity = models.IntegerField(blank=True)
    image=models.ImageField(default='default.jpg', upload_to='level1_pics')

    def __str__(self):
        return self.name

    def save(self):
        super().save()

        img=Image.open(self.image.path)

        if img.height>300 or img.width>300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)


        
class Level2(models.Model):
    name = models.CharField(max_length = 40)
    price = models.IntegerField()
    rating = models.FloatField(blank=True, null = True)
    quantity = models.IntegerField(blank=True)
    image=models.ImageField(default='default.jpg', upload_to='leve21_pics')

    def __str__(self):
        return self.name
    def save(self):
        super().save()

        img=Image.open(self.image.path)

        if img.height>300 or img.width>300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Level3(models.Model):
    name = models.CharField(max_length = 40)
    price = models.IntegerField()
    rating = models.FloatField(blank=True, null = True)
    quantity = models.IntegerField(blank=True)
    image=models.ImageField(default='default.jpg', upload_to='level3_pics')

    def __str__(self):
        return self.name
    def save(self):
        super().save()

        img=Image.open(self.image.path)

        if img.height>300 or img.width>300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)




class Level4(models.Model):
    name = models.CharField(max_length = 40)
    price = models.IntegerField()
    rating = models.FloatField(blank=True, null = True)
    quantity = models.IntegerField(blank=True)
    image=models.ImageField(default='default.jpg', upload_to='level4_pics')

    def __str__(self):
        return self.name

    def save(self):
        super().save()

        img=Image.open(self.image.path)

        if img.height>300 or img.width>300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
  