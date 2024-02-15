from django.db import models

class Form(models.Model):
    name = models.CharField(max_length = 100)
    id_num = models.IntegerField(primary_key=True)

class Posts(models.Model):
    id_var = models.AutoField(primary_key=True)
    title_var = models.CharField(max_length = 50)
    desc_var = models.CharField(max_length = 200)
    
    
