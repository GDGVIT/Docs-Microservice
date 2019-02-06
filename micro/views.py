from django.shortcuts import render, redirect
from micro.forms import MicroForm
from micro.models import Micro

# Create your views here.
def newLink(request):
    if request.method == "POST":
        form = MicroForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/read/')
            except:
                pass
    else:
        form = MicroForm()
    return render(request, 'newLink.html', {'form': form})
def read(request):
    links = Micro.objects.all()
    return render(request,"read.html",{'links':links})
def edit(request, id):
    micro = Micro.objects.get(id=id)
    return render(request,'edit.html', {'micro':micro})
def update(request, id):
    micro = Micro.objects.get(id=id)
    form = MicroForm(request.POST, instance = micro)
    if form.is_valid():
        form.save()
        return redirect("/read/")
    return render(request, 'edit.html', {'micro': micro})
def remove(request, id):
    micro = Micro.objects.get(id=id)
    micro.delete()
    return redirect("/read/")