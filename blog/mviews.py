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
        'posts': Post.objects.all().exclude(tag='SAMPLE MATERIALS').order_by('date_posted'),
        'announces': Announcement.objects.all().order_by('-id')[:7]
       }
    return render(request, 'blog/mobile/content.html',context)


def about(request):
    return render(request, 'blog/mobile/about.html',context)

class LoginView(View):
    template_name="blog/mobile/login.html"
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
    template_name="blog/mobile/createpost.html"
    def get(self,request):
        if request.user.is_authenticated:
            form1=PostForm()
            return render(request,self.template_name,{'form1':form1})
            form2=AnnouncementForm()
            return render(request,self.template_name,{'form2':form2})
        else:
            return render(request,"blog/mobile/404.html")    
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
    template_name="blog/mobile/post_detail.html"
    def get(self,request,pk):
        post=Post.objects.get(pk=pk)
        return render(request,self.template_name,{'post':post})

def pgtrb(request):
    context={
        'posts': Post.objects.filter(tag='PG TRB').order_by('date_posted'),
        'announces': Announcement.objects.all().order_by('-id')[:7]
    }
    return render(request, "posts/mobile/pgtrb.html",context)

def polytrb(request):
    context={
        'posts': Post.objects.filter(tag='POLY TRB').order_by('date_posted'),
        'announces': Announcement.objects.all().order_by('-id')[:7]
    }
    return render(request, "posts/mobile/polytrb.html",context)

def engrtrb(request):
    context={
        'posts': Post.objects.filter(tag='ENGR TRB').order_by('date_posted'),
        'announces': Announcement.objects.all().order_by('-id')[:7]
    }
    return render(request, "posts/mobile/engrtrb.html",context)

def tnset(request):
    context={
        'posts': Post.objects.filter(tag='TNSET').order_by('date_posted'),
        'announces': Announcement.objects.all().order_by('-id')[:7]
    }
    return render(request, "posts/mobile/tnset.html",context)

def gate(request):
    context={
        'posts': Post.objects.filter(tag='GATE').order_by('date_posted'),
        'announces': Announcement.objects.all().order_by('-id')[:7]
    }
    return render(request, "posts/mobile/gate.html",context)

def sample(request):
    context={
        'posts': Post.objects.filter(tag='SAMPLE MATERIALS').order_by('date_posted'),
        'announces': Announcement.objects.all().order_by('-id')[:7]
    }
    return render(request, "posts/mobile/sample.html",context)
