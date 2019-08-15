from django.shortcuts import render
#from django.http import HttpResponse
from FirstApp.models import FirstAppModel,citiesModel

# Create your views here.
def FirstApp_view(request,*args,**kwargs):
    #print(request.user)
    #return HttpResponse("<h1>This is first App for django demo</h1>")
    #myinstance={'myvar':'10','myvar2':'hello20'
    #            , 'myvar3':[10,20,'hi','bye']}
    return render(request,'FirstApp.html',{'cities' : citiesModel.objects.all()})
