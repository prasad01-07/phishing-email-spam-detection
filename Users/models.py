from django.db import models

# Create your models here.
from django.db.models import CASCADE


class UserRegister_Model(models.Model):
    fname=models.CharField(max_length=300)
    lname=models.CharField(max_length=200)
    email = models.EmailField(max_length=400)
    userid=models.CharField(max_length=200)
    password=models.CharField(max_length=10)
    gender=models.CharField(max_length=200)

class SendMailModel(models.Model):
    sendermail=models.EmailField(max_length=50)
    to=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    chat=models.CharField(max_length=200)
    spam=models.CharField(max_length=200)
    category=models.CharField(max_length=100)





class Phishing_Model(models.Model):
    attack_type=models.CharField(max_length=100)
    text=models.CharField(max_length=500)


class PhishingThread_Model(models.Model):
    usid=models.ForeignKey(UserRegister_Model,on_delete=CASCADE)
    website=models.CharField(max_length=500)
    atk=models.CharField(max_length=100)

class FeedbackModel(models.Model):
    username = models.ForeignKey(UserRegister_Model, on_delete=CASCADE)
    feedback = models.CharField(max_length=300)