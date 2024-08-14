from django.shortcuts import render
import datetime
# Create your views here.
def filter(request):
    dt=datetime.datetime.now()
    d={'data':'This is builtin filters','dt':dt,'c':11}
    return render(request,'filter.html',d)