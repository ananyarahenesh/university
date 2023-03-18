from django.http import HttpResponse
from django.shortcuts import render
from  . models import Department
# Create your views here.
def demo(request):
    obj = Department.objects.all()
    return render(request,"index.html",{'result':obj})