from django.db import models

class Form(models.Model):
    name = models.CharField(max_length = 100)
    id_num = models.IntegerField(primary_key=True)
    