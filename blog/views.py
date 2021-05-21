from django.shortcuts import render
from django.http import HttpResponse
from .models import post,Level1,Level2,Level3,Level4
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def ordered(request):
    return render(request,'blog/finished.html')

@login_required
def cart(request):
    return render(request, 'blog/cart.html')


@login_required
def orders(request):
    return render(request, 'blog/orders.html')


def home(request):
    return render(request,'blog/home.html',{'title':'About-title'})

def about(request):
    context={
        'posts' : post.objects.all()
    }
    return render(request,'blog/about.html',context)


def level1(request):
    context={
        'level1s' : Level1.objects.all()
    }
    return render(request,'blog/lev1.html',context)


def level2(request):
    context={
        'level2s' : Level2.objects.all()
    }
    return render(request,'blog/lev2.html',context)


def level3(request):
    context={
        'level3s' : Level3.objects.all()
    }
    return render(request,'blog/lev3.html',context)

def level4(request):
    context={
        'level4s' : Level4.objects.all()
    }
    return render(request,'blog/lev4.html',context)


def help(request):
    return render(request,'blog/help.html')

