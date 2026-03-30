from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp.models import person

# Create your views here.
def index(request):
    all_person = person.objects.all()
    return render(request, 'index1.html',{"all_person":all_person})


def form(request):
    if request.method == "POST":
        # รับข้อมูลจากฟอร์ม
        name = request.POST.get("name")
        age = request.POST.get("age")

        new_person = person.objects.create( 
            name=name,
            age=age
        )

        # เปลี่ยนเส้นทางไปหน้าแรก
        return redirect("/")
    else:
        # แสดงฟอร์ม
        return render(request, "form1.html")