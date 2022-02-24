from django.db import models
from parler.models import TranslatableModel, TranslatedFields


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