from django.urls import path


from .views import *


urlpatterns = [
    path("", home_page, name="home-page"),
    path("about/", about_page, name="about-page"),
    path("contact/", contact_page, name="contact-page"),
]