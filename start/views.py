from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse

from .forms import *
from .models import *
from main.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
# Create your views here.

def introduction (request):
    med = Med.objects.get(pk=1)
    genre = Genre.objects.all()

    context = {
        'med': med,
        'genre': genre,
    }

    return render(request, 'startup_page.html', context)
    # return HttpResponse('Welcome')

def registerform(request):
    form = RegisterForm(request.POST)
    profile_form = UserProfileForm(request.POST)
    if request.method == 'POST':

        if form.is_valid() and profile_form.is_valid():
            user = form.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()

            username= form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            is_staff = True
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect ('home')

        else:
            messages.warning(request, form.errors)
            return redirect('register')

    # else:
    #     form = RegisterForm(request.POST)
    #     profile_form = UserProfileForm(request.POST)
    med = Med.objects.get(pk=1)

    context = {
        'form': form,
        'profile_form': profile_form,
        'med': med,
    }

    return render(request, 'startup_page.html', context)

def loginform (request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password= password)
        if user:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid username/password')

    med = Med.objects.get(pk=1)

    return render(request, 'startup_page.html', {'med': med})

def logoutfunc(request):
    logout(request)
    return redirect('login')

@login_required(login_url='/login')
def home (request):
    blog = BlogCreate.objects.all()[:30]
    med = Med.objects.get(pk=1)
    genre = Genre.objects.all()

    context = {
        'blog': blog,
        'med': med,
        'genre': genre,
    }
    # return HttpResponse('You are home')
    return render(request, 'home.html', context)

@login_required(login_url='/login')
def profile (request):
    pro = User.objects.get(username=request.user.username)
    med = Med.objects.get(pk=1)
    genre = Genre.objects.all()
    subscribers = Followers.objects.filter(followed=pro)

    context = {
        'pro': pro,
        'med': med,
        'genre': genre,
        'subscribers': subscribers,
    }

    return render (request, 'profile.html', context)

@login_required(login_url='/login')
def userupdate (request):
    pro = User.objects.get(username=request.user.username)
    med = Med.objects.get(pk=1)
    genre = Genre.objects.all()
    if request.method == 'POST':
        profileform1 = ProfileUpdateForm1(request.POST, request.FILES, instance=request.user.userprofile)
        profileform = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if profileform.is_valid() and profileform1.is_valid():
            # can = profileform.save()

            # profilefo = profileform1.save(commit=False)
            # profilefo.can = can

            # profilefo.save()

            profileform.save()
            profileform1.save()
            messages.success(request, 'Your Account has been updated.')
            return redirect('userupdate')
        else:
            messages.warning(request, profileform.errors)
            messages.warning(request, profileform1.errors)
            return redirect('userupdate')

    context = {
        'med': med,
        'pro': pro,
        'genre': genre,
    }

    return render (request, 'userupdate.html', context)

@login_required(login_url='/login')
def userpasswordchange(request):
    med = Med.objects.get(pk=1)
    genre = Genre.objects.all()

    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successsfully updated')
            return redirect('user')

        else:
            messages.error(request, 'Please correct the error below.<br>' + str(form.errors))
            return redirect ('userpassword')

    else:
        pro = User.objects.get(username=request.user.username)
        form = PasswordChangeForm(request.user)

        context = {
            'form': form,
            'pro': pro,
            'genre': genre,
            'med': med
        }
    return render (request, 'userpasswordchange.html', context)

@login_required(login_url='/login')
def contact (request):
    med = Med.objects.get(pk=1)
    genre = Genre.objects.all()

    context = {
        'med': med,
        'genre': genre,
    }

    return render(request, 'contact.html', context)

@login_required(login_url='/login')
def searchbar (request):
    if request.method == 'GET':
        search = request.GET.get('search')
        post = BlogCreate.objects.all().filter(title__icontains=search)
        det = BlogCreate.objects.all().filter(description__icontains=search)
        name = User.objects.all().filter(username__icontains=search)
        genre = Genre.objects.all()
        med = Med.objects.get(pk=1)

        context = {
            'med': med,
            'genre': genre,
            'post': post,
            'det': det,
            'name': name,
            'search': search,
        }
        

        return render (request, 'searchbar.html', context)

# def search_blog(request):
#     sblog = request.GET.get('sblog')
#     payload = []
    
#     if sblog:
#         bcs = BlogCreate.objects.filter(title__icontains = sblog)
#         names = User.objects.filter (username__icontains= sblog)

#         for bc in bcs:
#             payload.append(bc.title)

#         for name in names:
#             payload.append(name.username)

#     # post = BlogCreate.objects.all().filter(title=sblog)
#     # name = User.objects.all().filter(username=sblog)

#     context = {
#         # 'post': post,
#         # 'name': name,
#         'data': payload,
#         'status':200,
#     }

#     # return render (request, 'searchbar.html', context)
#     return JsonResponse({'status':200, 'data': payload})


@login_required(login_url='/login')
def myworks (request):
    user=request.user
    blog = BlogCreate.objects.filter(author_id= user)
    med = Med.objects.get(pk=1)
    genre = Genre.objects.all()

    context = {
        'blog': blog,
        'med': med,
        'genre':genre,
    }

    return render(request, 'my_works.html', context)

def subscriptions (request):
    user = request.user
    fol1 = Followers.objects.filter(follower=user.username)
    med = Med.objects.get(pk=1)
    genre = Genre.objects.all()

    context = {
        'fol1': fol1,
        'med': med,
        'genre':genre,
    }

    return render(request, 'subscriptions.html', context)

def likedblogs (request):
    user = request.user
    sad = Like.value = 'True'
    like = Like.objects.filter(user = user).order_by('post').filter(value='Like')

    context = {
        'like': like,
    }

    return render (request, 'liked_blogs.html', context)

# def bloggers (request):
#     med = Med.objects.get(pk=1)
#     # bog = request.blogcreate().author_id
#     blogger = User.objects.all().order_by('username')
#     bog = BlogCreate.objects.all()
#     genre = Genre.objects.all()

#     context = {
#         'blogger': blogger,
#         'med': med,
#         'genre':genre,
#         'bog': bog,
#     }

#     return render(request, 'bloggers.html', context)