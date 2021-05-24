from django.shortcuts import redirect, render
from .models import Show

# Create your views here.
def index(request):
    shows = Show.objects.all()
    context ={
        'shows':shows
    }
    return render(request,'shows.html',context)

def new(request):
    return render(request,'index.html')

def create(request):
    if request.method == "POST":
        title = request.POST['title'],
        network = request.POST['network'],
        release_date = request.POST['release_date'],
        desc = request.POST['desc'],
        Show.objects.create(title=title,network=network,release_date=release_date,desc=desc)
    return redirect('/shows')

def edit(request,show_id):
    edit = Show.objects.get(id=show_id)
    context = {
        "show": edit
    }
    return render(request,'view.html',context)

def update(request,show_id):
    update = Show.objects.get(id=show_id)
    update.title = request.POST['title']
    update.network = request.POST['network']
    update.release_date = request.POST['release_date']
    update.desc = request.POST['desc']
    update.save()
    return redirect('/shows')

def show(request,show_id):
    view = Show.objects.get(id=show_id)
    context ={
        'show':view
    }
    return render(request,'update.html',context)

def delete(request,show_id):
    delete = Show.objects.get(id=show_id)
    delete.delete()
    return redirect('/shows')
