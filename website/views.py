from django.shortcuts import render

from website.models import *


def home_page(request):
    follow_links = FollowLink.objects.all()
    return render(
        request,
        "index.html",
        context={
            "follow_links": follow_links,
        }
    )


def about_page(request):
    return render(
        request,
        "pages/about.html",
        context={}
    )


def contact_page(request):
    return render(
        request,
        "pages/contact.html",
        context={}
    )