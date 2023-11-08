from django.shortcuts import render, redirect
from . models import Image

# Create your views here.
def index(request):
    q=Image.objects.all()
    return render(request,'index.html',{'result':q})
def add(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        img=request.FILES['img']
        desc=request.POST.get('desc')
        image=Image(name=name,img=img,desc=desc)
        image.save();
        return redirect('/')
    return render(request,'add.html')

