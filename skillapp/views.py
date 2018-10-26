from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile, Section, Posts
from .forms import SignupForm, PostForm, ProfileForm

# def signup(request):
#     return render(request,"registration/registration_form.html")

def signup(request):
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            auth_login(request, user)
            return redirect('edit_profile')
    else:
        form = SignupForm()

    return render(request, 'registration/signup.html', {'form': form})

def home(request):
    # form = QuestionForm()
    sections = Section.objects.all()
    return render(request, "skill/index.html", {"sections":sections})

def profile(request):
    current_user = request.user
    profile=Profile.objects.filter(user=request.user)
    return render (request,'profile.html',{'profile':profile})

def edit_profile(request):
    form = ProfileForm()
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=current_user.profile)
        if form.is_valid():
            form.save()

            return redirect('profile')

    return render(request, 'edit-profile.html', {'form': form})

# @login_required
def section(request,section_id):
    posts = Posts.objects.filter(section=request.user.profile.section)
    return render(request,'skill/section.html',locals())

@login_required
def new_post(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            posted = post_form.save(commit=False)
            posted.user = request.user.profile
            posted.section = request.user.profile.section
            posted.save()
        return redirect('skill/post.html')
    else:
        post_form = PostForm()
    return render(request,'skill/new-post.html', locals())

@login_required
def post(request,post_id):
    post = Posts.objects.get(section=request.user.profile.section)
    # comments = Comment.objects.all()
    # co_form = CommentForm()
    return render(request,'skill/post.html',{"post": post})
