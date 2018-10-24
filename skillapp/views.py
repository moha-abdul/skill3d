from django.shortcuts import render, redirect
from .forms import SignupForm, QuestionForm

def signup(request):
    return render(request,"registration/registration_form.html")

def home(request):
    form = QuestionForm()
    return render(request, "skill/index.html", {"form":form})

def profile(request):
    return render(request,"profile.html")

def edit_profile(request):
    return render(request,"profile.html")
