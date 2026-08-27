from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from guides.models import GuideProfile
from .models import Booking


@login_required
def book_guide(request, guide_id):

    guide = get_object_or_404(
        GuideProfile,
        id=guide_id,
        is_approved=True
    )

    error = None

    if request.method == 'POST':

        date = request.POST.get('date', '')
        time = request.POST.get('time', '')
        number_of_people = request.POST.get('number_of_people', '1')
        message = request.POST.get('message', '').strip()

        if not date or not time:
            error = "Please select a date and time for your booking."

        else:

            try:
                num = int(number_of_people)
                if num < 1:
                    error = "Number of people must be at least 1."
            except ValueError:
                error = "Please enter a valid number of people."

            if not error:
                today = timezone.now().date()
                from datetime import datetime as dt
                booking_date = dt.strptime(date, '%Y-%m-%d').date()
                if booking_date < today:
                    error = "You cannot book a date in the past."

        if not error:
            Booking.objects.create(
                tourist=request.user,
                guide=guide,
                date=date,
                time=time,
                number_of_people=number_of_people,
                message=message,
                status='pending'
            )

            return redirect('my_bookings')

    return render(
        request,
        'booking/book_guide.html',
        {
            'guide': guide,
            'error': error,
        }
    )


@login_required
def my_bookings(request):

    bookings = Booking.objects.filter(
        tourist=request.user
    ).select_related(
        'guide', 'guide__user'
    ).order_by('-created_at')

    return render(
        request,
        'booking/my_bookings.html',
        {
            'bookings': bookings,
        }
    )


@login_required
def cancel_booking(request, booking_id):

    booking = get_object_or_404(
        Booking,
        id=booking_id,
        tourist=request.user
    )

    if booking.status in ['pending', 'confirmed']:
        booking.status = 'cancelled'
        booking.save()

    return redirect('my_bookings')
