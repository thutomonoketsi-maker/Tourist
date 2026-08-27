
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def guide_home(request):

    return render(
        request,
        'guide/home.html'
    )