from django.shortcuts import render
from .models import Volunteer


def home(request):
    return render(request, 'volunteer/home.html')


def about(request):
    return render(request, 'volunteer/about.html')


def register(request):

    if request.method == "POST":

        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        interest = request.POST['interest']

        Volunteer.objects.create(
            name=name,
            email=email,
            phone=phone,
            interest=interest
        )

        return render(request, 'volunteer/register.html',
                      {'message': 'Registration Successful!'})

    return render(request, 'volunteer/register.html')


    

    