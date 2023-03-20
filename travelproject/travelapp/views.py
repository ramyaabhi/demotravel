from django.http import HttpResponse
from django.shortcuts import render
from .models import Place


# Create your views here.

def demo(request):
    obj=Place.objects.all()
    return render(request, "index.html", {'result': obj})
def demo1(request):
    obj1=Place.objects.all()
    return render(request, "index.html", {'result': obj1})


#def demo(request):
  #  return render(request,"index.html")
   # name="India"
   # return render(request, "home.html",{'obj':name})
#def about(request):
   # return render(request, "result.html")
#def contact(request):
    #return HttpResponse("Hello am contact")
#def addition(request):
 #   x = int(request.GET['num1'])
  #  y = int(request.GET['num2'])
  #  res = x+y
  #  return render(request, "result.html", {'result': res})
