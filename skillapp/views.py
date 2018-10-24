from django.shortcuts import render, redirect
from .models import Profile, Section
from .forms import SignupForm, QuestionForm

def signup(request):
    return render(request,"registration/registration_form.html")

def home(request):
    # form = QuestionForm()
    sections = Section.objects.all()
    return render(request, "skill/index.html", {"sections":sections})

def profile(request):
    return render(request,"profile.html")

def edit_profile(request):
    return render(request,"profile.html")
