import email
from django.templatetags.static import static
from django.urls import reverse
from unicodedata import category
from django.db import models
from parler.models import TranslatableModel, TranslatedFields
from mptt.models import MPTTModel, TreeForeignKey
from .managers import CategoryManager
from django_resized import ResizedImageField
from django.core.validators import MaxLengthValidator, MinLengthValidator
import html2text


class Category(MPTTModel, TranslatableModel):
    
    parent = TreeForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="children")
    
    translations = TranslatedFields(
        title = models.CharField(max_length=255),
    )

    image = models.ImageField(null=True, blank=True)
    
    slug=models.SlugField()

    objects=CategoryManager()
    
    def __str__(self):
        return self.safe_translation_getter("title", any_language=True) or "-"
    

    @property
    def navigation_link(self):
        if self.slug:
            return reverse("category-products-page", kwargs={"slug": self.slug})
        return ""
    

    @property
    def background_image_url(self):
        if self.image:
            return self.image.url
        return static("/assets/img/breadcrumb.jpg")



class FollowLink(models.Model):
    icon_text = models.TextField(null=True, blank=True)
    icon = models.ImageField(null=True, blank=True)
    link = models.TextField()

    def __str__(self):
        return self.link or "-"
    
    def get_link(self):
        if self.link:
            return self.link
        return ""
    

    def get_icon(self):
        if self.icon:
            return "<img src='{}' style='width: 30px; height: 30px;'/>".format(self.icon.url)
        return self.icon_text


class BannerHero(TranslatableModel):
    translations = TranslatedFields(
        title1 = models.CharField(max_length=255, null=True, blank=True),
        title2 = models.CharField(max_length=255, null=True, blank=True),
        title3 = models.CharField(max_length=255, null=True, blank=True),
    )

    image = models.FileField()

    def __str__(self):
        return self.safe_translation_getter("title1", any_language=True) or "-"
    

    def get_image(self):
        if self.image:
            return self.image.url
        return ""


class FeatureItem(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(max_length=255),
        description = models.TextField()
    )

    icon = models.FileField(null=True, blank=True)
    icon_text=models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField()

    def get_icon(self):
        if self.icon:
            return "<img src='{}'/>".format(self.icon.url)
        return self.icon_text
    

    def __str__(self):
        return self.safe_translation_getter("title", any_language=True) or "-"



class Service(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(max_length=255),
        description = models.TextField(),
        content = models.TextField()
    )

    icon = models.FileField(null=True, blank=True)
    icon_text=models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField()

    def get_icon(self):
        if self.icon:
            return "<img src='{}'/>".format(self.icon.url)
        return self.icon_text
    

    def __str__(self):
        return self.safe_translation_getter("title", any_language=True) or "-"
    
    @property
    def url(self):
        return reverse("service-detail-page", kwargs={"slug": self.slug})



class Counter(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(max_length=15),
    )

    icon = models.FileField(null=True, blank=True)
    icon_text = models.CharField(max_length=255, null=True, blank=True)
    count = models.IntegerField()

    def get_icon(self):
        if self.icon:
            return "<img src='{}'/>".format(self.icon.url)
        return self.icon_text
    

    def __str__(self):
        return self.safe_translation_getter("title", any_language=True) or "-"


class Case(TranslatableModel):
    
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    translations = TranslatedFields(
        title = models.CharField(max_length=15),
        content = models.TextField()
    )

    slug = models.SlugField()
    image = ResizedImageField(size=[367, 400],  quality=100, crop=["middle", "center"], upload_to="images/")

    def __str__(self):
        return self.safe_translation_getter("title", any_language=True) or "-"

    @property
    def detail_link(self):
        return reverse(
            "case-detail-page",
            kwargs={
                "slug": self.slug
            }
        )
 

class Choose(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(max_length=255),
        description = models.TextField()
    )

    icon = models.FileField(null=True, blank=True)
    icon_text=models.CharField(max_length=255, null=True, blank=True)

    def get_icon(self):
        if self.icon:
            return "<img src='{}'/>".format(self.icon.url)
        return self.icon_text
    

    def __str__(self):
        return self.safe_translation_getter("title", any_language=True) or "-"


class TeamExpert(TranslatableModel):

    translations = TranslatedFields(
        title = models.CharField(max_length=255),
        description = models.TextField(),
        job=models.CharField(max_length=255)
    )
    slug = models.SlugField()
    image = ResizedImageField(size=[367, 400],  quality=100, crop=["middle", "center"], upload_to="images/", null=True, blank=True)


class SocialAccount(models.Model):
    team_expert = models.ForeignKey(TeamExpert, null=True, on_delete=models.SET_NULL, related_name="links")
    link=models.TextField()
    icon = models.FileField(null=True, blank=True)
    icon_text=models.CharField(max_length=255, null=True, blank=True)

    def get_icon(self):
        if self.icon:
            return "<img src='{}'/>".format(self.icon.url)
        return self.icon_text

    def __str__(self):
        return self.link or "-"



class ProcessItem(TranslatableModel):

    translations = TranslatedFields(
        title = models.CharField(max_length=30),
        description = models.CharField(max_length=70)
    )

    image = ResizedImageField(size=[100, 100],  quality=100, crop=["middle", "center"], upload_to="images/")

    def __str__(self):
        return self.safe_translation_getter("title", any_language=True) or "-"




class Testimonial(TranslatableModel):
    
    fullname = models.CharField(max_length=30)

    translations = TranslatedFields(
        comment = models.CharField(max_length=70),
        identity = models.CharField(max_length=70)
    )

    image = ResizedImageField(size=[100, 100],  quality=100, crop=["middle", "center"], upload_to="images/")
    rating = models.IntegerField(
        validators=[
            MaxLengthValidator,
            MinLengthValidator
        ]
    )

    def __str__(self):
        return self.fullname or "-"
    

    @property
    def stars_component(self):
        result = ""
        for _ in range(self.rating):
            result += "<i class='fas fa-star'></i>"
        return result
    

    def save(self, *args, **kwargs):
        if self.rating < 0:
            self.rating = 0
        if self.rating > 5:
            self.rating = 5
        return super(Testimonial, self).save(*args, **kwargs)


class Product(TranslatableModel):

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    translations = TranslatedFields(
        title = models.CharField(max_length=40),
        description = models.TextField(),
        content = models.TextField(),
    )

    slug = models.SlugField()
    
    image_content = ResizedImageField(size=[1920, 1280],  quality=100, crop=["middle", "center"], upload_to="images/")

    image_description = ResizedImageField(size=[550, 600],  quality=100, crop=["middle", "center"], upload_to="images/")

    def __str__(self):
        return self.safe_translation_getter("title", any_language=True) or "-"
    

    @property
    def detail_link(self):
        return reverse(
            "product-detail-page",
            kwargs={
                "category_slug": self.category.slug,
                "slug": self.slug
            }
        )
    
    @property
    def get_thumbnail(self):
        if self.image_description:
            return self.image_description.url
        if self.image_content:
            return self.image_content.url
        return static("staticfiles/assets/img/03.jpg")
    
    @property
    def short_description(self):
        if self.safe_translation_getter("description"):
            return self.safe_translation_getter("description")
        if self.safe_translation_getter("content"):
            return html2text.html2text(self.safe_translation_getter("content"))
        return ""



class BlogCategory(TranslatableModel):
    
    translations = TranslatedFields(
        title = models.CharField(max_length=50),
    )

    slug=models.SlugField()

    def __str__(self):
        return self.safe_translation_getter("title", any_language=True) or "-"
    
    @property
    def navigation_link(self):
        if self.slug:
            return reverse("blog-list-page", kwargs={"slug": self.slug})
        return ""


class Blog(TranslatableModel):

    category = models.ForeignKey(BlogCategory, on_delete=models.SET_NULL, null=True, related_name="posts")

    translations = TranslatedFields(
        title = models.CharField(max_length=50),
        content = models.TextField(),
    )

    date = models.DateTimeField(auto_now_add=True)

    author = models.CharField(max_length = 100)

    slug = models.SlugField()
    
    image_content = ResizedImageField(size=[1920, 1280],  quality=100, crop=["middle", "center"], upload_to="images/")

    image_description = ResizedImageField(size=[550, 600],  quality=100, crop=["middle", "center"], upload_to="images/")

    def __str__(self):
        return self.safe_translation_getter("title", any_language=True) or "-"
    
    @property
    def get_thumbnail(self):
        if self.image_description:
            return self.image_description.url
        if self.image_content:
            return self.image_content.url
        return static("staticfiles/assets/img/03.jpg")
    
    @property
    def short_description(self):
        if self.safe_translation_getter("content"):
            return html2text.html2text(self.safe_translation_getter("content"))
        
    @property
    def url(self):
        return reverse("blog-detail-page", kwargs={"slug": self.slug})


class Feedback(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    
    def __str__(self):
        return self.name or "-"