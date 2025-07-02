from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import PostForm, OpenHouseForm
from .models import Post, OpenHouse
from django.http import JsonResponse

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', '/')
            return redirect(next_url)
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')


def register_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
        else:
            User.objects.create_user(username=username, password=password)
            messages.success(request, 'Account created successfully')
            return redirect('login')
    return render(request, 'register.html')



@login_required(login_url='login')
def home_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()

    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'form': form, 'posts': posts})


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def openhouse(request):
    events = OpenHouse.objects.all()
    return render(request, 'open_house/open-house.html', {'events': events})



@login_required
def createopenhouse(request):
    if request.method == 'POST':
        form = OpenHouseForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save()
            Post.objects.create(
                user=request.user,
                content=f"New Event Created: {event.event_name}",
                image=event.event_image
            )
            return redirect('open-house')
    else:
        form = OpenHouseForm()

    return render(request, 'open_house/create-open-house.html', {'form': form})


def eventdetail(request, pk):
    event = get_object_or_404(OpenHouse, pk=pk)
    return render(request, 'open_house/event_detail.html', {'event': event})


@login_required
def likepost(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return JsonResponse({
        'liked': liked,
        'total_likes': post.total_likes(),
    })




