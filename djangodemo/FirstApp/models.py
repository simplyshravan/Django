from django.db import models

# Create your models here.
class FirstAppModel(models.Model):
    city = models.CharField(max_length=40,null=True)
    state = models.CharField(max_length=40, null = True)
    sale_amount = models.IntegerField()
    #max_salary = models.IntegerField()
    class Meta:
         db_table = "sales"

class citiesModel(models.Model):
    id=models.IntegerField(primary_key=True)
    city = models.CharField(max_length=40,null=True)
    state = models.CharField(max_length=40, null = True)
    latitude=models.IntegerField()
    longitude=models.IntegerField()
    class Meta:
         db_table = "cities"