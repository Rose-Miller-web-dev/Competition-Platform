from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q

from .models import Competition, Topic
from .forms import CompetitionForm

# Create your views here.

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    competitions = Competition.objects.filter(Q(topic__name__icontains=q) |
                                              Q(title__icontains=q) |
                                              Q(description__icontains=q))

    comp_count = competitions.count()
    topic = Topic.objects.all()
    context = {'competitions': competitions, 'topic': topic, 'cc': comp_count}
    return render(request, 'base/home.html', context)

def compinfo(request, pk):
    room = Competition.objects.get(id=pk)
    
    context = {'competition': room}
    return render(request, 'base/room.html', context)

def create_competition(request):
    form = CompetitionForm()
    
    if request.method == 'POST':
        form = CompetitionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/competition_form.html', context)

def update_competition(request, pk):
    comp = Competition.objects.get(id=pk)
    form = CompetitionForm(instance=comp)

    if request.method == 'POST':
        form = CompetitionForm(request.POST, instance=comp)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/competition_form.html', context)

def delete_page(request, pk):
    obj = Competition.objects.get(id = pk)
    context = {'object': obj}

    if request.method == 'POST':
        obj.delete()
        return redirect('home')

    return render(request, 'base/delete.html', context)