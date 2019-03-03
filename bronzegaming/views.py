from django.shortcuts import render,redirect
from . import models
import datetime
import dateutil.parser
from django.utils import timezone

# Create your views here.
def home(request):
    all_posts = models.Post.objects.filter(due__gte=timezone.now()).order_by('-created')

    context = {
        'posts' : all_posts
    }
    return render(request,'base/home.html', context)

def new_post(request):
    context = {
        'platforms' : models.Platform.objects.all(),
        'games' : models.Game.objects.all(),
        'events' : models.Event.objects.all()
    }
    if request.user.is_authenticated:
        return render(request,'base/new_post.html', context)
    else:
        return redirect('home')
    

def view_post(request, post_id):
    current_post = models.Post.objects.get(id=post_id)
    comments = models.Comment.objects.filter(post=models.Post.objects.get(id=post_id))
    context = {
        'post' : current_post,
        'comments' : comments,
    }
    return render(request,'base/view_post.html', context)

def new_post_processing(request):
    if request.user.is_authenticated:
        user = request.user
        body = request.POST.get('body')
        title = request.POST.get('title')
        due = dateutil.parser.parse(request.POST.get('due'))
        platform = models.Platform.objects.get(id=request.POST.get('platform'))
        game = models.Game.objects.get(id=request.POST.get('game'))
        event = models.Event.objects.get(id=request.POST.get('event'))
        users_needed = request.POST.get('users_needed')
        new_post = models.Post(user=user,title=title,due=due,platform=platform,game=game,event=event, body=body, users_needed=users_needed)
        new_post.save()
        return redirect('view_post', post_id=new_post.id)
    else:
        return redirect('home')

def new_comment(request, post_id):
    new_comment = models.Comment(user=request.user, post=models.Post.objects.get(id=post_id), text=request.POST.get('text'))
    new_comment.save()
    return redirect('view_post', post_id=post_id)

def view_user(request, user_id):
    selected_user = models.User.objects.get(id=user_id)
    context = {
        'selected_user' : selected_user,
    }
    return render(request,'base/view_user.html', context)

def post_going(request, post_id):
    post = models.Post.objects.get(id=post_id)
    if post.users_needed:
        if request.user in post.users_going.all():
            pass
        else:
            post.users_needed -=1
    post.users_going.add(request.user)
    post.save()
    return redirect('view_post', post_id=post_id)