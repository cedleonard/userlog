from django.db import models
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):
    #create relationship
    user = models.OneToOneField(User)
    #Add any additional attributes
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to="profile_pictures", blank=True)
    # import pillow for importing profile_pictures
    def __str__(self):
        return self.user.username

# Create your models here.
