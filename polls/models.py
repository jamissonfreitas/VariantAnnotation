from django.db import models

# Create your models here.


class VCF(models.Model):
    file_in = models.FileField('VCF in')
    file_out = models.FileField('VCF out')
    date = models.DateTimeField('date published')


class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
