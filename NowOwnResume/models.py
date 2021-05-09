from django.db import models
from datetime import date

from datetime import datetime


class Suggesstions(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, default="NILL")
    email = models.EmailField(max_length=100, default="NILL")
    address = models.CharField(max_length=250, default="NILL")
    mob = models.CharField(max_length=20, default="none")
    suggestion = models.CharField(max_length=2050, default="")
    today = date.today()
    now = datetime.now().time()

    def __str__(self):
        return self.name


class Resumes(models.Model):
    resume_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40, default="NILL")
    type = models.CharField(max_length=40, default="NILL")
    address = models.CharField(max_length=450, default="NILL")
    mob = models.CharField(max_length=20, default="none")
    today = today = date.today()
    now = datetime.now().time()

    def __str__(self):
        return self.name


class Templates(models.Model):
    template_id = models.AutoField(primary_key=True)
    templateFile = models.FileField(upload_to='templates')
    image = models.ImageField(upload_to='tempImage')
    today = date.today()
    now = datetime.now().time()

    def __str__(self):
        return str(self.template_id)
