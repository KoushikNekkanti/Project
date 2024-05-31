from django.shortcuts import render
from .models import VisualData
def index(request):
    dat=VisualData.objects.all()
    print(dir(dat))
    return render(request,'index.html',{'data': dat})