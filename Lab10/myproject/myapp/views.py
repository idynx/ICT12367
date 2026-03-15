from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import person

# Create your views here.
def index(request):
    all_person = person.objects.all()
    return render(request, 'index1.html',{"all_person":all_person})

def about(request):
    return render(request, 'about.html')

def form(request):
    return render(request, 'form1.html')