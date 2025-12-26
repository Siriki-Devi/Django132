from django.shortcuts import render
from .models import Person

def form(request):
    if request.method == "POST":
        Person.objects.create(
            name=request.POST.get("name"),
            age=request.POST.get("age"),
            dob=request.POST.get("dob"),
            first_movie=request.POST.get("first_movie"),
            location=request.POST.get("location"),
            movies=request.POST.get("movies")
        )
        return render(request, "about.html")
    return render(request, "form.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

