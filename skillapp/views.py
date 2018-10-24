from django.shortcuts import render, redirect
from .models import Profile, Section, Posts
from .forms import SignupForm, PostForm

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

# @login_required
def section(request,section_id):
    # section = Posts.objects.filter(id=section_id)
    return render(request,'skill/section.html',locals())
