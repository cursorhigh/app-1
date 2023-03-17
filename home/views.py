from django.shortcuts import render , redirect
from django.http import HttpResponse ,HttpResponseRedirect
from django.contrib.auth.models import User , auth

# Create your views here.
from leaderboard.models import Person
def home(request):
    return render(request,'home.html')
def download_page(request):
    return render (request,'Download-page.html')
def msgl(request):
    return render (request,'message.html')
def reg(request):
    return redirect('http://127.0.0.1:8000/register/')
def logout(request):
    auth.logout(request)
    return redirect('http://127.0.0.1:8000/')
def leaderboard(request):
    return HttpResponseRedirect('/leaderboard/')
def log(request):
    return redirect('http://127.0.0.1:8000/login/')

def gpage(request):
    return redirect('http://127.0.0.1:8000/gamepage/')
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

@login_required
def google_login_callback(request):
    # Get the user's Google account
    google_account = SocialAccount.objects.get(user=request.user, provider='google')

    # Create a new Person model instance for the user (if it doesn't already exist)
    try:
        person = Person.objects.get(name=request.user.username)
    except Person.DoesNotExist:
        person = Person.objects.create(name=request.user.username)


    # Save the person model
    person.save()

    # Redirect the user back to the leaderboard
    return redirect('/')
