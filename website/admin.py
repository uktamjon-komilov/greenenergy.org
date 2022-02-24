from django.contrib import admin
from parler.admin import TranslatableAdmin

from .models import *


# class CourseAdmin(admin.ModelAdmin):

#     def get_prepopulated_fields(request, obj=None):
#         return {
#             "slug": ("title",)
#         }


# admin.site.register(Course, CourseAdmin)


admin.site.register(FollowLink)
admin.site.register(BannerHero, TranslatableAdmin)