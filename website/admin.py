from pyexpat import model
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from parler.admin import TranslatableAdmin, TranslatableModelForm
from mptt.admin import MPTTModelAdmin
from mptt.forms import MPTTAdminForm

from .models import *


class FeatureItemAdmin(TranslatableAdmin):

    def get_prepopulated_fields(self, request, obj=None):
        return {
            "slug": ("title",)
        }

class ServiceAdmin(SummernoteModelAdmin ,TranslatableAdmin):
    summernote_fields = ["content"]
    def get_prepopulated_fields(self, request, obj=None):
        return {
            "slug": ("title",)
        }

class CategoryAdminForm(MPTTAdminForm, TranslatableModelForm):
    pass


class CategoryAdmin(TranslatableAdmin, MPTTModelAdmin):
    form = CategoryAdminForm

    def get_prepopulated_fields(self, request, obj=None):
        return {"slug": ("title",)} 


class CaseAdmin(SummernoteModelAdmin ,TranslatableAdmin):
    summernote_fields = ["content"]
    def get_prepopulated_fields(self, request, obj=None):
        return {
            "slug": ("title",)
        }

class ChooseAdmin(SummernoteModelAdmin ,TranslatableAdmin):
    summernote_fields = ["description"]
    

class SocialAccountInline(admin.StackedInline):
    model = SocialAccount

class TeamExpertAdmin(SummernoteModelAdmin, TranslatableAdmin):
    summernote_fields = ["description"]
    inlines = [
        SocialAccountInline,
    ]
    def get_prepopulated_fields(self, request, obj=None):
        return {
            "slug": ("title",)
        }


class ProductAdmin(SummernoteModelAdmin, TranslatableAdmin):
    summernote_fields = ["content"]
    
    def get_prepopulated_fields(self, request, obj=None):
        return {
            "slug": ("title",)
        }

class BlogCategoryAdmin(TranslatableAdmin):
    def get_prepopulated_fields(self, request, obj=None):
        return {
            "slug": ("title",)
        }

class BlogAdmin(SummernoteModelAdmin, TranslatableAdmin):
    summernote_fields = ["content"]
    
    def get_prepopulated_fields(self, request, obj=None):
        return {
            "slug": ("title",)
        }


admin.site.register(Category, CategoryAdmin)

admin.site.register(FollowLink)
admin.site.register(BannerHero, TranslatableAdmin)
admin.site.register(FeatureItem, FeatureItemAdmin)
admin.site.register(Service , ServiceAdmin)
admin.site.register(Counter, TranslatableAdmin)
admin.site.register(Case, CaseAdmin)
admin.site.register(Choose , ChooseAdmin)
admin.site.register(TeamExpert, TeamExpertAdmin)
admin.site.register(ProcessItem, TranslatableAdmin)
admin.site.register(Testimonial, TranslatableAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(BlogCategory, BlogCategoryAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Partner)
admin.site.register(Feedback)