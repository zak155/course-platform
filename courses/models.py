from django.db import models

# Create your models here.
class AcessRequirement(models.TextChoices):
    ANYONE="anyone","Anyone"
    EMAIL_REQUIRED="email_required","Email_Required"
    DRAFT="draft","DRAFT"

class PublishedStatus(models.TextChoices):
    PUBLISHED="published","PUBLISHED"
    COMING_SOON="soon","Coming Soon"
    DRAFT="draft","DRAFT"

class courses(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(blank=True,default="")
    #image
    access=models.CharField( max_length=20,
                                   choices=AcessRequirement.choices,
                                   defualt=AcessRequirement.DRAFT)
    status=models.CharField( max_length=20,
                                   choices=PublishedStatus.PUBLISHED,
                                   defualt=PublishedStatus.DRAFT)
@property
def is_published(self):
    return self.status == PublishedStatus.PUBLISHED




