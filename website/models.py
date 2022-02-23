from django.db import models


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