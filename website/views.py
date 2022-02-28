from multiprocessing import context
from django.db.models import Q
from django.http import JsonResponse
from django.urls import reverse
from django.shortcuts import redirect, render
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from django.db.models.aggregates import Count
from .forms import FeedbackForm

from website.models import *
from website.api_views import *


def home_page(request):
    banner_heros = BannerHero.objects.all()
    feature_items = FeatureItem.objects.all()
    services = Service.objects.all()
    counters = Counter.objects.all()
    cases=Case.objects.all()
    chooses = Choose.objects.all()
    team_experts = TeamExpert.objects.all()
    process_items =ProcessItem.objects.all()
    testimonials = Testimonial.objects.all()
    blogs = Blog.objects.all().order_by("-id")[:3]
    return render(
        request,
        "index.html",
        context={
            "banner_heros": banner_heros,
            "feature_items": feature_items,
            "services" : services,
            "counters" : counters,
            "cases" : cases,
            "chooses" : chooses,
            "team_experts" : team_experts,
            "process_items" : process_items,
            "testimonials" : testimonials,
            "blogs" : blogs
        }
    )


def category_products_page(request, slug):
    try:
        category = Category.objects.get(slug=slug)
    except:
        return redirect(reverse("home-page"))
    
    products = Product.objects.filter(category=category)

    return render(
        request,
        "pages/category.html",
        context={
            "category": category,
            "products": products
        }
    )


def product_detail_page(request, category_slug, slug):
    try:
        product = Product.objects.get(
            category__slug=category_slug,
            slug=slug
        )
    except:
        return redirect(reverse("home-page"))
    
    other_categories = Category.objects.all().exclude(slug=category_slug)

    return render(
        request,
        "pages/product.html",
        context={
            "product": product,
            "other_categories": other_categories
        }
    )


def about_page(request):
    counters = Counter.objects.all()
    team_experts = TeamExpert.objects.all()

    return render(
        request,
        "pages/about.html",
        context={
            "counters" : counters,
            "team_experts" :team_experts
        }
    )


def contact_page(request):
    return render(
        request,
        "pages/contact.html",
        context={}
    )

def search_page(request):
    query = request.GET.get("q", None)

    if not query:
        return redirect(reverse("home-page"))

    products = Product.objects.filter(
        Q(translations__title__icontains=query) |
        Q(translations__description__icontains=query) |
        Q(translations__content__icontains=query)
    )
    return render(
        request,
        "pages/search.html",
        context={
            "products": products
        }
    )


def blog_page(request, slug):
    all_blogs_count = Blog.objects.count()
    blog_categories=BlogCategory.objects.annotate(posts_count=Count("posts")).all()
    last_three_blogs=Blog.objects.all().order_by("-id")[:3]
    try:
        blog = Blog.objects.get(slug=slug)
    except:
        return redirect(reverse("blog-list-page"))
    return render(
        request,
        "pages/blog-detail.html",
        context={
            "blog" : blog,
            "blog_categories" : blog_categories,
            "last_three_blogs" : last_three_blogs,
            "all_blogs_count" : all_blogs_count
        }
    )


def blog_list_page(request, slug):
    
    try:
        blog_category = BlogCategory.objects.get(slug=slug)
    except:
        return redirect(reverse("home-page"))
    
    blog_list = Blog.objects.filter(category=blog_category)
        
    
    page = request.GET.get('page', 1)

    paginator = Paginator(blog_list, 3)
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)

    return render(request, 'pages/blog.html', { 'blogs': blogs })


def blog_list_page_all(request):
    
    blog_list = Blog.objects.all()
        
    
    page = request.GET.get('page', 1)

    paginator = Paginator(blog_list, 3)
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)

    return render(request, "pages/blog.html", { "blogs": blogs })


def blog_search_page(request):
    query = request.GET.get("q2", None)

    if not query:
        return redirect(reverse("home-page"))

    blogs = Blog.objects.filter(
        Q(translations__title__icontains=query) |
        Q(translations__content__icontains=query)
    )

    return render(request, "pages/blog.html", { "blogs": blogs })


def how_to_buy(request):
    form = FeedbackForm()
    return render(
        request,
        "pages/howtobuy.html",
        {
            "form" : form
        }
    )


def service_detail_page(request, slug):

    try:
        service = Service.objects.get(slug=slug)
    except:
        return redirect(reverse("home-page"))

    return render(
        request, 
        "pages/service-detail-page.html", 
        { 
            "service": service 
        }
        
        )


def case_detail_page(request, slug):

    try:
        case = Case.objects.get(
            slug=slug
        )
    except:
        return redirect(reverse("home-page"))


    return render(
        request, 
        "pages/case-detail-page.html", 
        { 
            "case": case 
        }
        
        )


def feedback(request):
    form = FeedbackForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse("feedback-saved"))
    else:
        return redirect(reverse("not-valid"))


def feedback_saved(request):
    return render(request, "pages/form_saved.html")

def not_valid(request):
    return render(request, "pages/not_valid.html")
