from .models import Category, FollowLink


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
