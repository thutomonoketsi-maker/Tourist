from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Itinerary


@login_required
def my_trips(request):

    trips = Itinerary.objects.filter(
        user=request.user
    ).order_by('-created_at')

    return render(
        request,
        'itinerary/my_trips.html',
        {
            'trips': trips
        }
    )


@login_required
def create_trip(request):

    error = None

    if request.method == 'POST':

        name = request.POST.get('name', '').strip()
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        if not name:
            error = "Please give your trip a name."

        elif start_date and end_date and start_date > end_date:
            error = "Your end date cannot be before your start date."

        else:

            Itinerary.objects.create(
                user=request.user,
                name=name,
                start_date=start_date or None,
                end_date=end_date or None
            )

            return redirect('my_trips')

    return render(
        request,
        'itinerary/create_trip.html',
        {
            'error': error
        }
    )