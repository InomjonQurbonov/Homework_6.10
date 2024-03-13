from django.shortcuts import render
from .models import Themes

def themes_list(request):
    themes = Themes.objects.all()
    return render(request,'themes/themes.html',{'themes':themes})

def theme_detail(request,pk):
    theme = Themes.objects.get(id=pk)
    return render(request,'themes/themes_details.html',{'theme':theme})