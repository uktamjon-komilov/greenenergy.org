from django import template
from django.urls import reverse
from django.utils.translation import gettext as _

register = template.Library()

@register.filter(name="show_about_button")
def show_about_button(request):
    about_button_title = _("Discover More")
    url = reverse("about-page")
    full_url = request.get_full_path()
    if url != full_url:
        return f"<a href='{url}' class='theme-btn'>{about_button_title}<i class='fas fa-arrow-circle-right'></i></a>"
    return ""