from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post, Announcement
from django.contrib.auth.models import User
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate,login,logout
from django.http import JsonResponse
from .forms import PostForm, AnnouncementForm



    
def content(request):
    context={
        'posts': Post.objects.all(),
        'announces': Announcement.objects.all().order_by('-id')[:7]
       }
    return render(request, 'blog/content.html',context)



def about(request):
    context={
        'posts': Post.objects.all(),
        'announces': Announcement.objects.all().order_by('-id')[:7]
       }
    return render(request, 'blog/about.html',context)

class LoginView(View):
    template_name="blog/login.html"
    def get(self,request):
        return render(request,self.template_name)
    def post(self,request):
        try:
            user =User.objects.get(email=request.POST.get('email'))
        except:
            return render(request, self.template_name,{'error':True})    
        else:
            user = authenticate(request, 
            username=user.username, 
            password=request.POST.get('password')
            )
            if user is None:
                return render(request,self.template_name,{'error':True})
            login(request,user)
            response= redirect('content')
            response.set_cookie('role','user')
            return response
        
        return render(request,self.template_name)

class LogoutView(View,LoginRequiredMixin):
    def get(self,request):  
        logout(request)
        response=redirect('content')
        response.delete_cookie('role')
        return response

class PostCreateView(View,LoginRequiredMixin):
    template_name="blog/createpost.html"
    def get(self,request):
        if request.user.is_authenticated:
            form1=PostForm()
            return render(request,self.template_name,{'form1':form1})
            form2=AnnouncementForm()
            return render(request,self.template_name,{'form2':form2})
        else:
            return render(request,"blog/404.html")    
    def post(self,request):
        if request.user.is_authenticated:
            form1=PostForm(request.POST)
            if form1.is_valid():
                post=Post()
                post.title=request.POST.get('title')
                post.content=form1.cleaned_data.get('content')
                post.author=request.user
                post.link=request.POST.get('link')
                post.tag=request.POST.get('tag')
                post.save()
                return redirect('content')
                form1=PostForm(request.POST)
            form2=AnnouncementForm(request.POST)
            if form2.is_valid():
                announce=Announcement()
                announce.announcement=request.POST.get('announcement')
                announce.author=request.user
                announce.save()
                return redirect('content')
        else:
            return redirect('login')        
        return render(request,self.template_name,{'form1':form1,'form2':form2},)  

class PostDetailView(View):
    template_name="blog/post_detail.html"
    def get(self,request,pk):
        post=Post.objects.get(pk=pk)
        return render(request,self.template_name,{'post':post})


def pgtrb(request):
    context={
        'posts': Post.objects.filter(tag='PG-TRB'),
        'announces': Announcement.objects.all().order_by('-id')[:7]
    }

    return render(request, "posts/pgtrb.html",context)

def polytrb(request):
    context={
        'posts': Post.objects.filter(tag='POLY-TRB'),
        'announces': Announcement.objects.all().order_by('-id')[:7]
    }
    return render(request, "posts/polytrb.html",context)

def engrtrb(request):
    context={
        'posts': Post.objects.filter(tag='ENGR-TRB'),
        'announces': Announcement.objects.all().order_by('-id')[:7]
    }
    return render(request, "posts/engrtrb.html",context)

def tnset(request):
    context={
        'posts': Post.objects.filter(tag='TNSET'),
        'announces': Announcement.objects.all().order_by('-id')[:7]
    }
    return render(request, "posts/tnset.html",context)

def gate(request):
    context={
        'posts': Post.objects.filter(tag='GATE'),
        'announces': Announcement.objects.all().order_by('-id')[:7]
    }
    return render(request, "posts/gate.html",context)