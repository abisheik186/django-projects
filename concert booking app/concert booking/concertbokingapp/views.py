from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegistrationForm,CustomAuthenticationForm
from .models import concertslist,tcktbooking,bookinghistory
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import datetime
def home(request):
    user=request.user
    allconcerts=concertslist.objects.all()
    form = UserRegistrationForm()
    login_form = CustomAuthenticationForm()
    if user != None:
        bookhis=bookinghistory.objects.filter(name=user.username)
    return render(request, 'home.html',{'concerts':allconcerts,'form':form,'loginform':login_form,'history':bookhis})
def register(request):
    if request.method == 'POST':
        if request.POST.get('submit') == 'signup':
            form = UserRegistrationForm(request.POST) 
            if form.is_valid():
                form.save()   
        elif request.POST.get('submit') == 'login':
            form=CustomAuthenticationForm(request.POST)   
    else:
        form = UserRegistrationForm()
    return render(request, 'home.html')#, {'form': form})
@csrf_exempt
def booktickets(request):
    if request.method == 'POST':
        concert_id = request.POST.get('concertId')
        tcktcount = request.POST.get('numoftckt')
        concert = concertslist.objects.get(id=concert_id)
        tcktcount = int(tcktcount)

        booking = tcktbooking(name=request.user.username, email=request.user.email, concerttitle=concert.title, count=tcktcount)
        booking.save()
        concert.availticket -= tcktcount
        concert.save()
        booktime=datetime.datetime.now()
        history=bookinghistory(title=concert.title,artist=concert.artist,venue=concert.venue,name=request.user.username,email=request.user.email,count=tcktcount,bookedtime=booktime)
        history.save()