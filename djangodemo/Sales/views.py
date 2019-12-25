from django.shortcuts import render

# Create your views here.
from Sales.models import salesModel

# Create your views here.
def Sales_view(request,*args,**kwargs):
    getsales=salesModel.objects.all();
    #print(request.user)
    #return HttpResponse("<h1>This is first App for django demo</h1>")
    #myinstance={'myvar':'10','myvar2':'hello20'
    #            , 'myvar3':[10,20,'hi','bye']}
    context={"sales":getsales}
    return render(request,'Sales.html',context)
