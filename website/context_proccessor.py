from .models import Category, FollowLink, StaticPage


def categories(request):
    try:
        categories = Category.objects.all()
    except:
        categories = []
    return {
        "categories": categories
    }


def links(request):
    try:
        follow_links = FollowLink.objects.all()
    except:
        follow_links = []
    return {
        "follow_links": follow_links
    }


def navbar_static_pages(request):
    static_pages = StaticPage.objects.filter(show_at_navbar=True)
    return {
        "navbar_static_pages": static_pages
    }