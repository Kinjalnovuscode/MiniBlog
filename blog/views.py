from django.shortcuts import render, HttpResponseRedirect
from .forms import SignupForm, loginform ,PostForm
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages
from .models import Post
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import permission_required

def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html',{'posts':posts})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def dashboard(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:  # Allow superusers to see all posts
            posts = Post.objects.all()
        else:
            posts = Post.objects.filter(user_id=request.user.id)  # Filter by logged-in user's ID
        user_name = request.user.get_full_name()
        return render(request, 'dashboard.html', {'posts': posts, 'user_name': user_name})
    else:
        return HttpResponseRedirect('/login/', messages.error(request, 'Please Login First to view dashboard'))

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            userr = form.save()

            # Assign the user to the 'Author' group
            author_group = Group.objects.get(name='Author')
            userr.groups.add(author_group)

            messages.success(request, 'Signup successful! Please log in to continue.')
            return HttpResponseRedirect('/login/')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = loginform(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    print(user.id)
                    return HttpResponseRedirect('/dashboard/') #redirect to dashboard page after successful login
                else:
                    messages.error(request, 'Invalid Username or Password')
        else:
            form = loginform()  # Make sure to initialize the form for GET requests

        return render(request, 'login.html', {'form': form})
    else:
        return HttpResponseRedirect('/dashboard/')  

def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                print("//////////")
                print(request.user.id)
                # Pass the logged-in user to the save method
                form.save(user=request.user)  # This ensures that the user_id gets saved
                messages.success(request, 'Your Blog is added successfully!')
                return HttpResponseRedirect('/dashboard/')  # Redirect to the dashboard
        else:
            form = PostForm()  
        return render(request, 'addpost.html', {'form': form})
    else:
        return HttpResponseRedirect('/login/')


def update_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            form = PostForm(request.POST, instance=pi)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your Blog is updated successfully!')
                return HttpResponseRedirect('/dashboard/')
        else:
            pi = Post.objects.get(pk=id)
            form = PostForm(instance=pi)
        return render(request, 'updatepost.html', {'form': form})
    else:
        return HttpResponseRedirect('/login/')

@permission_required('blog.delete_post', raise_exception=True)
def delete_post(request, id):
    if request.user.is_authenticated:
        post_to_delete = Post.objects.get(id=id)
        post_to_delete.delete()
        messages.success(request, 'Post deleted successfully!')
        return HttpResponseRedirect('/dashboard/')
    else:
        messages.error(request, 'You do not have permission to delete this post.')
        return HttpResponseRedirect('/dashboard/')