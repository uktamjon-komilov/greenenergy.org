from django.contrib import admin

from .models import *


# class CourseAdmin(admin.ModelAdmin):

#     def get_prepopulated_fields(request, obj=None):
#         return {
#             "slug": ("title",)
#         }


# admin.site.register(Course, CourseAdmin)


admin.site.register(FollowLink)