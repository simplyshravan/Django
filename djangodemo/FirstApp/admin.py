from django.contrib import admin

# Register your models here.
from .models import FirstAppModel,citiesModel

admin.site.register(FirstAppModel)
#admin.site.register(citiesModel)