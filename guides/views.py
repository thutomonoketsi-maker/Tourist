from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from .models import GuideProfile


@login_required
def guides_list(request):

    search = request.GET.get('search', '').strip()

    guides = GuideProfile.objects.filter(
        is_approved=True,
        is_available=True,
    ).select_related('user')

    if search:
        guides = guides.filter(
            user__first_name__icontains=search
        ) | guides.filter(
            user__last_name__icontains=search
        ) | guides.filter(
            specialties__icontains=search
        )

    return render(
        request,
        'guides/guides_list.html',
        {
            'guides': guides,
            'search': search,
        }
    )


@login_required
def guide_detail(request, guide_id):

    guide = get_object_or_404(
        GuideProfile,
        id=guide_id,
        is_approved=True
    )

    return render(
        request,
        'guides/guide_detail.html',
        {
            'guide': guide,
        }
    )
