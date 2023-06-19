from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from .models import Competition, Topic, Comment
from .forms import CreateCompetitionForm, UpdateCompetitionForm

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
    comments = room.comment_set.all().order_by('-created')
    comment_count = comments.count()

    if request.method == 'POST':
        new_comment = Comment.objects.create(
            user = request.user,
            competition = room,
            body = request.POST.get('body')
        )

    context = {'competition': room, 'comments': comments}
    return render(request, 'base/room.html', context)

def user_profile(request, pk):
    user = User.objects.get(id=pk)
    awards = user.award_set.all()
    award_count = awards.count()
    created_competitions = user.competition_set.all()
    context = { 'user': user, 'awards': awards, 'created_competitions': created_competitions,
               'award_count': award_count }
    
    return render(request, 'base/user_profile.html', context)

@login_required(login_url='login')
def create_competition(request):
    form = CreateCompetitionForm()
    
    if request.method == 'POST':
        form = CreateCompetitionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/competition_form.html', context)


def update_competition(request, pk):
    comp = Competition.objects.get(id=pk)
    form = UpdateCompetitionForm(instance=comp)

    if request.user != comp.host:
        return HttpResponse('not yours bitch!')

    if request.method == 'POST':
        form = UpdateCompetitionForm(request.POST, instance=comp)
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

def login_page(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Access denied')

    context = {'page': page}
    return render(request, 'base/login_register.html', context)

def register_user(request):
    page = 'register'
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        
        else:
            messages.error(request, 'An error occured')

    context = {'form': form, 'page': page}
    return render(request, 'base/login_register.html', context)

def logout_user(request):
    logout(request)
    return redirect('home')

def delete_comment(request, pk):
    comment = Comment.objects.get(id=pk)

    if request.method == 'POST':
        comment.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    context = {'comment': comment}
    return render(request, 'base/delete_comment.html', context)