from django.contrib.auth.models import User
from django.db import models


class ProfileModel(models.Model):
    status = {
       ('Male', 'Male'),
       ('Female','Female')
    }
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=200)
    phone_number = models.PositiveIntegerField(null=True)
    location = models.CharField(max_length=200)
    profile_pic = models.ImageField(null = True, upload_to='images')
    gender = models.CharField(max_length=6, choices= status,default='Male')


    def __str__(self):
        return self.name


class UserList(models.Model):
    users = models.ForeignKey(User,on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.email