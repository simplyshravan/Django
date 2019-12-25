from django.db import models

# Create your models here.
class FirstAppModel(models.Model):
    city = models.CharField(max_length=40,null=True)
    state = models.CharField(max_length=40, null = True)
    latitude=models.IntegerField()
    longitude=models.IntegerField()
    class Meta:
         db_table = "cities"
    