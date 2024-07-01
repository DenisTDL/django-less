from django.shortcuts import render


def one(request):
    return render(request, 'mysit/one.html')


def admin(request):
    return render(request, 'mysit/models.py')
