from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def tourist_home(request):

    return render(
        request,
        'tourist/home.html'
    )