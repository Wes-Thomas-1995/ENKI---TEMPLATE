from django.shortcuts import render, redirect
import datetime


def Home_Page(request):
    date = datetime.date.today()
    date = date.strftime("%A - %B %d, %Y")

    context = {'date': date}
    return render(request, 'ENKI_HOME/home-page.html', context)


def Register(request):
    return render(request, 'ENKI_HOME/Register.html')


