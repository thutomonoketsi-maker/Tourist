from django.urls import path

from .views import (
    explore,
    place_detail,
    save_place,
    unsave_place,
    saved_places,
)


urlpatterns = [

    path(
        '',
        explore,
        name='explore'
    ),

    path(
        'place/<int:place_id>/',
        place_detail,
        name='place_detail'
    ),

    path(
        'place/<int:place_id>/save/',
        save_place,
        name='save_place'
    ),

    path(
        'place/<int:place_id>/unsave/',
        unsave_place,
        name='unsave_place'
    ),

    path(
        'saved/',
        saved_places,
        name='saved_places'
    ),

]