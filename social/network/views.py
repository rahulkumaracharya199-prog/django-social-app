from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Post
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    return render (request, "home.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect ("profile")
        else:
            return render (request, "registration/login.html", {'error': 'Invalid username or password'})

    return render (request, "registration/login.html")

def register_view(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")

        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            email=email
        )

        user.save()
        return redirect("login")
    return render (request, "registration/register.html")

@login_required
def profileindex(request):
    data = {}
    data['posts'] = Post.objects.all().order_by('-created_at')
    return render (request, "profile/index.html", data)

@login_required
def logout_view(request):
    logout(request)
    return redirect ("index")

@login_required
def CreatePost(request):
    if request.method == "POST":
        content = request.POST.get("content")
        image = request.FILES.get("image")

        post = Post(author=request.user, content=content, image=image)
        post.save()
        return redirect("profile")

