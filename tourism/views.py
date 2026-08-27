from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .models import TourismPlace, SavedPlace


@login_required
def explore(request):

    category = request.GET.get('category', '').strip()
    search = request.GET.get('search', '').strip()

    places = TourismPlace.objects.filter(
        is_active=True
    )

    if category:
        places = places.filter(
            category=category
        )

    if search:
        places = places.filter(
            name__icontains=search
        )

    saved_place_ids = SavedPlace.objects.filter(
        user=request.user
    ).values_list(
        'place_id',
        flat=True
    )

    return render(
        request,
        'tourism/explore.html',
        {
            'places': places,
            'saved_place_ids': saved_place_ids,
            'selected_category': category,
            'search': search,
        }
    )


@login_required
def place_detail(request, place_id):

    place = get_object_or_404(
        TourismPlace,
        id=place_id,
        is_active=True
    )

    saved = SavedPlace.objects.filter(
        user=request.user,
        place=place
    ).exists()

    return render(
        request,
        'tourism/place_detail.html',
        {
            'place': place,
            'saved': saved,
        }
    )


@login_required
def save_place(request, place_id):

    place = get_object_or_404(
        TourismPlace,
        id=place_id,
        is_active=True
    )

    if request.method == 'POST':

        SavedPlace.objects.get_or_create(
            user=request.user,
            place=place
        )

    return redirect(
        'place_detail',
        place_id=place.id
    )


@login_required
def unsave_place(request, place_id):

    place = get_object_or_404(
        TourismPlace,
        id=place_id,
        is_active=True
    )

    if request.method == 'POST':

        SavedPlace.objects.filter(
            user=request.user,
            place=place
        ).delete()

    return redirect(
        'place_detail',
        place_id=place.id
    )


@login_required
def saved_places(request):

    saved = SavedPlace.objects.filter(
        user=request.user
    ).select_related(
        'place'
    )

    return render(
        request,
        'tourism/saved_places.html',
        {
            'saved_places': saved,
        }
    )