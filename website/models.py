from django.templatetags.static import static
from django.urls import reverse
from django.db import models
from parler.models import TranslatableModel, TranslatedFields
from mptt.models import MPTTModel, TreeForeignKey
from .managers import CategoryManager
from django_resized import ResizedImageField
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.utils.translation import gettext_lazy as _
import html2text


class Category(MPTTModel, TranslatableModel):
    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
    
    parent = TreeForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="children", verbose_name=_("Parent category"))
    
    translations = TranslatedFields(
        title = models.CharField(max_length=255, verbose_name=_("Title")),
    )

    image = models.ImageField(null=True, blank=True, verbose_name=_("Image"))
    
    slug=models.SlugField(verbose_name=_("Short url"))

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
    class Meta:
        verbose_name = _("Follow link")
        verbose_name_plural = _("Follow links")

    icon = models.ImageField(null=True, blank=True, verbose_name=_("Icon file"))
    icon_text = models.TextField(null=True, blank=True, verbose_name=_("Font Awesome Icon"))
    link = models.TextField(verbose_name=_("Link"))

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
    class Meta:
        verbose_name = _("Banner")
        verbose_name_plural = _("Banners")
    
    translations = TranslatedFields(
        title1 = models.CharField(max_length=255, null=True, blank=True, verbose_name=_("Title 1")),
        title2 = models.CharField(max_length=255, null=True, blank=True, verbose_name=_("Title 2")),
        title3 = models.CharField(max_length=255, null=True, blank=True, verbose_name=_("Title 3")),
    )

    image = models.FileField(verbose_name=_("Image"))

    def __str__(self):
        return self.safe_translation_getter("title1", any_language=True) or "-"
    

    def get_image(self):
        if self.image:
            return self.image.url
        return ""


class FeatureItem(TranslatableModel):
    class Meta:
        verbose_name = _("Feature item")
        verbose_name_plural = _("Feature items")
    
    translations = TranslatedFields(
        title = models.CharField(max_length=255, verbose_name=_("Title")),
        description = models.TextField(verbose_name=_("Description"))
    )

    icon = models.FileField(null=True, blank=True, verbose_name=_("Icon file"))
    icon_text=models.CharField(max_length=255, null=True, blank=True, verbose_name=_("Font Awesome Icon"))
    slug = models.SlugField(verbose_name=_("Short url"))

    def get_icon(self):
        if self.icon:
            return "<img src='{}'/>".format(self.icon.url)
        return self.icon_text
    

    def __str__(self):
        return self.safe_translation_getter("title", any_language=True) or "-"



class Service(TranslatableModel):
    class Meta:
        verbose_name = _("Service")
        verbose_name_plural = _("Services")

    translations = TranslatedFields(
        title = models.CharField(max_length=255, verbose_name=_("Title")),
        description = models.TextField(verbose_name=_("Description")),
        content = models.TextField(verbose_name=_("Content"))
    )

    icon = models.FileField(null=True, blank=True, verbose_name=_("Icon file"))
    icon_text=models.CharField(max_length=255, null=True, blank=True, verbose_name=_("Font Awesome Icon"))
    slug = models.SlugField(verbose_name=_("Short url"))

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
    class Meta:
        verbose_name = _("Counter")
        verbose_name_plural = _("Counters")
    
    translations = TranslatedFields(
        title = models.CharField(max_length=15, verbose_name=_("Title")),
    )

    icon = models.FileField(null=True, blank=True, verbose_name=_("Icon file"))
    icon_text = models.CharField(max_length=255, null=True, blank=True, verbose_name=_("Font Awesome Icon"))
    count = models.IntegerField(verbose_name=_("Number"))

    def get_icon(self):
        if self.icon:
            return "<img src='{}'/>".format(self.icon.url)
        return self.icon_text
    

    def __str__(self):
        return self.safe_translation_getter("title", any_language=True) or "-"


class Case(TranslatableModel):
    class Meta:
        verbose_name = _("Case")
        verbose_name_plural = _("Cases")
    
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name=_("Category"))

    translations = TranslatedFields(
        title = models.CharField(max_length=15, verbose_name=_("Title")),
        content = models.TextField(verbose_name=_("Content"))
    )

    slug = models.SlugField(verbose_name=_("Short url"))
    image = ResizedImageField(size=[367, 400],  quality=100, crop=["middle", "center"], upload_to="images/", verbose_name=_("Image"))

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
    class Meta:
        verbose_name = _("Option")
        verbose_name_plural = _("Options")

    translations = TranslatedFields(
        title = models.CharField(max_length=255, verbose_name=_("Title")),
        description = models.TextField(verbose_name=_("Description"))
    )

    icon = models.FileField(null=True, blank=True, verbose_name=_("Icon file"))
    icon_text=models.CharField(max_length=255, null=True, blank=True, verbose_name=_("Font Awesome Icon"))

    def get_icon(self):
        if self.icon:
            return "<img src='{}'/>".format(self.icon.url)
        return self.icon_text
    

    def __str__(self):
        return self.safe_translation_getter("title", any_language=True) or "-"


class TeamExpert(TranslatableModel):
    class Meta:
        verbose_name = _("Expert")
        verbose_name_plural = _("Experts")
    
    translations = TranslatedFields(
        title = models.CharField(max_length=255, verbose_name=_("Title")),
        description = models.TextField(verbose_name=_("Description")),
        job=models.CharField(max_length=255, verbose_name=_("Position"))
    )
    slug = models.SlugField(verbose_name=_("Short url"))
    image = ResizedImageField(size=[367, 400],  quality=100, crop=["middle", "center"], upload_to="images/", null=True, blank=True, verbose_name=_("Image"))


class SocialAccount(models.Model):
    class Meta:
        verbose_name = _("Social network")
        verbose_name_plural = _("Social networks")
    
    team_expert = models.ForeignKey(TeamExpert, null=True, on_delete=models.SET_NULL, related_name="links", verbose_name=_("Expert"))
    link=models.TextField(verbose_name=_("Link"))
    icon = models.FileField(null=True, blank=True, verbose_name=_("Icon file"))
    icon_text=models.CharField(max_length=255, null=True, blank=True, verbose_name=_("Font Awesome Icon"))

    def get_icon(self):
        if self.icon:
            return "<img src='{}'/>".format(self.icon.url)
        return self.icon_text

    def __str__(self):
        return self.link or "-"



class ProcessItem(TranslatableModel):
    class Meta:
        verbose_name = _("Process item")
        verbose_name_plural = _("Process items")
    
    translations = TranslatedFields(
        title = models.CharField(max_length=30, verbose_name=_("Title")),
        description = models.CharField(max_length=70, verbose_name=_("Description"))
    )

    image = ResizedImageField(size=[100, 100],  quality=100, crop=["middle", "center"], upload_to="images/", verbose_name=_("Image"))

    def __str__(self):
        return self.safe_translation_getter("title", any_language=True) or "-"




class Testimonial(TranslatableModel):
    class Meta:
        verbose_name = _("Testimonial")
        verbose_name_plural = _("Testimonials")
    
    fullname = models.CharField(max_length=30, verbose_name=_("Fullname"))

    translations = TranslatedFields(
        comment = models.CharField(max_length=70, verbose_name=_("Comment")),
        identity = models.CharField(max_length=70, verbose_name=_("Commenter"))
    )

    image = ResizedImageField(size=[100, 100],  quality=100, crop=["middle", "center"], upload_to="images/", verbose_name=_("Image"))
    rating = models.IntegerField(
        validators=[
            MaxLengthValidator,
            MinLengthValidator
        ],
        verbose_name=_("Rating score")
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
    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
    
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name=_("Category"))

    translations = TranslatedFields(
        title = models.CharField(max_length=40, verbose_name=_("Title")),
        description = models.TextField(verbose_name=_("Short description")),
        content = models.TextField(verbose_name=_("Content")),
    )

    slug = models.SlugField(verbose_name=_("Short url"))
    
    image_content = ResizedImageField(size=[1920, 1280],  quality=100, crop=["middle", "center"], upload_to="images/", verbose_name=_("Main image"))

    image_description = ResizedImageField(size=[550, 600],  quality=100, crop=["middle", "center"], upload_to="images/", verbose_name=_("Thumbnail image"))

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
    class Meta:
        verbose_name = _("Blog category")
        verbose_name_plural = _("Blog categories")
    
    translations = TranslatedFields(
        title = models.CharField(max_length=50, verbose_name=_("Title")),
    )

    slug=models.SlugField(verbose_name=_("Short url"))

    def __str__(self):
        return self.safe_translation_getter("title", any_language=True) or "-"
    
    @property
    def navigation_link(self):
        if self.slug:
            return reverse("blog-list-page", kwargs={"slug": self.slug})
        return ""


class Blog(TranslatableModel):
    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")
    
    category = models.ForeignKey(BlogCategory, on_delete=models.SET_NULL, null=True, related_name="posts", verbose_name=_("Category"))

    translations = TranslatedFields(
        title = models.CharField(max_length=50, verbose_name=_("Title")),
        content = models.TextField(verbose_name=_("Content")),
    )

    date = models.DateTimeField(auto_now_add=True, verbose_name=_("Date and time"))

    author = models.CharField(max_length = 100, verbose_name=_("Author"))

    slug = models.SlugField(verbose_name=_("Short url"))
    
    image_content = ResizedImageField(size=[1920, 1280],  quality=100, crop=["middle", "center"], upload_to="images/", verbose_name=_("Main image"))

    image_description = ResizedImageField(size=[550, 600],  quality=100, crop=["middle", "center"], upload_to="images/", verbose_name=_("Thumbnail image"))

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
    class Meta:
        verbose_name = _("Feedback")
        verbose_name_plural = _("Feedbacks")
    
    name = models.CharField(max_length=255, verbose_name=_("Fullname"))
    email = models.EmailField(verbose_name=_("Email"))
    subject = models.CharField(max_length=255, verbose_name=_("Subject"))
    message = models.TextField(verbose_name=_("Message"))
    
    def __str__(self):
        return self.name or "-"


class Partner(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    url = models.TextField(verbose_name=_("Url"))
    image = models.ImageField(verbose_name=_("Image"))

    def __str__(self):
        return self.title
    

    @property
    def get_image(self):
        if self.image:
            return self.image.url
        return ""
    

    @property
    def get_alt(self):
        if self.title:
            return self.title
        return ""


class StaticPage(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(max_length=50, verbose_name=_("Title")),
        content = models.TextField(verbose_name=_("Content")),
    )

    slug = models.SlugField()

    show_at_navbar = models.BooleanField(default=False)
    show_at_footer = models.BooleanField(default=False)

    def __str__(self):
        return self.safe_translation_getter("title", any_language=True) or "-"
    
    @property
    def get_link(self):
        return reverse("static-page", kwargs={"slug": self.slug})