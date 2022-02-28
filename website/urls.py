from django.urls import path

from .views import *


urlpatterns = [
    path("", home_page, name="home-page"),
    path("category/<slug>/", category_products_page, name="category-products-page"),
    path("category/<category_slug>/<slug>/", product_detail_page, name="product-detail-page"),
    path("search/", search_page, name="search-page"),
    path("blog/search/", blog_search_page, name="blog-search-page"),
    path("blog/list-all/", blog_list_page_all, name="blog-list-page-all"),
    path("blog/list/<slug>/", blog_list_page, name="blog-list-page"),
    path("blog/<slug>/", blog_page, name="blog-detail-page"),
    path("about/", about_page, name="about-page"),
    path("how-to-buy/", how_to_buy, name="howtobuy-page"),
    path("service-detail-page/<slug>/", service_detail_page, name="service-detail-page"),
    path("case-detail-page/<slug>/", case_detail_page, name="case-detail-page"),
    path("feedback/", feedback, name="feedback"),
    path("feedback-saved/", feedback_saved, name="feedback-saved"),
    path("not-valid/", not_valid, name="not-valid"),
]