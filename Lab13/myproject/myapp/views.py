from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from myapp.models import person
from django.db.models import Q

def form(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")

        person.objects.create(
            name = name,
            age = age
        )
        return redirect("/")
    else:
        return render(request, "form1.html")

def index(request):
    all_Person = person.objects.all()

    query = request.GET.get('q')

    if query:
        all_Person = all_Person.filter(Q(name__icontains=query) | Q(age__icontains=query))

    return render(request, "index1.html", {"all_person": all_Person})

def edit(request, person_id):
    p = get_object_or_404(person, pk=person_id)
    
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")

        p.name = name
        p.age = age
        p.save()
        return redirect("/")
    else:

        return render(request, "edit.html", {"person": p})

def delete(request, person_id):
    p = get_object_or_404(person, pk=person_id)
    p.delete()
    return redirect("/")
