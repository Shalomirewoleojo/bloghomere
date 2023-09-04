from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import *
from .forms import *
from start.models import Followers
from start.forms import FollowersForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    UpdateView,
    DeleteView,
)

# Create your views here.

@login_required(login_url='/login')
def create (request):
    if request.method == 'POST':
        form = BlogCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Your blog has been posted :)")
            return redirect('create')
        else:
            messages.warning(request, form.errors)
            return redirect('create')

    form = BlogCreateForm
    genre = Genre.objects.all()
    med = Med.objects.get(pk=1)
    user = request.user
    
    context = {
        'form': form,
        'genre': genre,
        'med': med
    }

    return render (request, 'create_blog.html', context)

@login_required(login_url='/login')
def audio (request):
    blog1 = BlogCreate.objects.all()
    med = Med.objects.get(pk=1)
    genre = Genre.objects.all()

    content = {
        'blog1': blog1,
        'med': med,
        'genre': genre,
    }
    return render(request, 'audio.html', content)

@login_required(login_url='/login')
def text (request):
    blog1 = BlogCreate.objects.all()
    med = Med.objects.get(pk=1)
    genre = Genre.objects.all()

    content = {
        'blog1': blog1,
        'med': med,
        'genre': genre,
    }
    return render(request, 'text.html', content)

@login_required(login_url='/login')
def video (request):
    blog1 = BlogCreate.objects.all()
    med = Med.objects.get(pk=1)
    genre = Genre.objects.all()

    content = {
        'blog1': blog1,
        'med': med,
        'genre': genre,
    }
    return render(request, 'video.html', content)

@login_required(login_url='/login')
def genre (request):
    if request.method == 'GET':
        sick = request.GET.get('sick')
        post = BlogCreate.objects.all().filter(category=sick)

        blog = BlogCreate.objects.all()[:11]
        med = Med.objects.get(pk=1)
        genre = Genre.objects.all()

        context = {
            'blog': blog,
            'med': med,
            'genre': genre,
            'post': post,
            'sick': sick,
        }
    
        return render (request, 'genre.html', context)


def textblog (request, id, slug):
    content = BlogCreate.objects.get(pk=id)
    comments = Comment.objects.filter(post_id = id)
    med = Med.objects.get(pk=1)
    genre = Genre.objects.all()

    context = {
        'genre': genre,
        'comments': comments,
        'med': med,
        'content': content,
    }

    return render (request, 'text_blog.html', context)


def videoblog (request, id, slug):
    content = BlogCreate.objects.get(pk=id)
    comments = Comment.objects.filter(post_id = id)
    med = Med.objects.get(pk=1)
    genre = Genre.objects.all()
    url = request.META.get('HTTP_REFERER')
    user = request.user

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('url')

    else:
        form = CommentForm()


    context = {
        'genre': genre,
        'med': med,
        'content': content,
        'comments': comments,
        'user': user,
        'form': form,
    }

    return render (request, 'video_blog.html', context)


def audioblog (request, id, slug):
    content = BlogCreate.objects.get(pk=id)
    comments = Comment.objects.filter(post_id = id)
    med = Med.objects.get(pk=1)
    genre = Genre.objects.all()

    context = {
        'genre': genre,
        'comments': comments,
        'med': med,
        'content': content,
    }

    return render (request, 'audio_blog.html', context)

@login_required(login_url='/login')
def like_post (request): 
    user = request.user
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = BlogCreate.objects.get(id=post_id)

        if user in post_obj.liked.all():
            post_obj.liked.remove(user)
        else:
            post_obj.liked.add(user)

        like, created = Like.objects.get_or_create(user=user, post_id = post_id)

        if not created:
            if like.value == 'Unlike':
                like.value = 'Like'
            else:
                like.value = 'Unlike'

        like.save()

    return redirect(url)

@login_required(login_url='/login')
def add_comment (request):
    user= request.user
    url = request.META.get('HTTP_REFERER')
    # post_id = request.POST.get('post_id')
    if request.method == 'POST':
        # post_id = request.POST.get('post_id')
        form = CommentForm(request.POST)
        if form.is_valid():
            
            # comment = form.save(commit=False)
            # comment.post = post
            # comment.save()
            # return redirect(url)
            form.save()

        else:
            return redirect(url)

    else:
        form = CommentForm()

    context = {
        'form': form,
    }

    return redirect(url)


@login_required(login_url='/login')
def view_profile (request, id):
    user= request.user
    author1 = User.objects.get (pk=id)
    blog = BlogCreate.objects.filter(author_id= author1)
    likes = BlogCreate.objects.filter(liked=user)
    delet = Followers.objects.filter(follower=user.username, followed=author1)
    sat = author1.id
    med = Med.objects.get(pk=1)
    genre = Genre.objects.all()
    subscribers = Followers.objects.filter(followed=author1)

    if request.method == 'POST':
        form = FollowersForm(request.POST)
        made = Followers.objects.get_or_create(follower=user.username, followed=author1)
        
        if not made:
            if form.is_valid():
                messages.success(request, 'thank you for subscribing')
                form.save()
                return redirect ('view', id=sat)

            else:
                messages.warning(request, form.errors)
                return redirect ('view', id=sat)

    context = {
        'author1': author1,
        'blog': blog,
        'med':med,
        'genre':genre,
        'subscribers': subscribers,
        'delet': delet,
    }

    return render(request, 'viewprofile.html', context)

# def delete(request):
#     itemid = request.POST['itemid']
#     BlogCreate.filter(pk=itemid).delete()
#     messages.success(request, message)
#     return redirect ('home')

@login_required(login_url='/login')
def unsubscribe (request, id):
    user= request.user
    author1 = User.objects.get (pk=id)
    sat = author1.id
    delet = Followers.objects.filter(follower=user.username, followed=author1)

    delet.delete()
    messages.success(request, 'unsubscribed')
    return redirect ('view', id=sat)

# def get_blog_queryset(query = None):
#     queryset = []
#     queries = query.split (" ") #splits up each word
#     for q in queries:
#         posts = BlogCreate.objects.filter(
#             Q(title__icontains = q) | #icontains gets rid of capitalization
#             Q(description__icontains = q) |
#             Q(text__icontains = q)
#         ).distinct()

#         for post in posts:
#             queryset.append(post)

#         names = User.objects.all(
#             Q(username__icontains = q)
#         )

#         for name in names:
#             queryset.append(name)
#     return list(set(queryset)) 
# set makes sure it's unique and list lets it get sent to template
    # return render (request, 'searchbar.html')
    

class PostUpdateView (LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = BlogCreate
    fields = ('title', 'category', 'image_cover', 'video', 'audio', 'text', 'description')
    success_url = '/myworks'
    template_name = 'update.html'
    context_object_name= 'item'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # def form_invalid(form, request):       
    #     messages.warning(request, form.errors)

    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.accepts('text/html'):
            return response

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model= BlogCreate
    template_name = 'blogcreate_confirm_delete.html'
    success_url = '/myworks'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

        # https://youtu.be/-s7e_Fy6NRU (class based views)