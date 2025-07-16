from django.db import models

# Create your models here.
class AcessRequirement(models.TextChoices):
    ANYONE="anyone","Anyone"
    EMAIL_REQUIRED="email_required","Email_Required"
   

class PublishedStatus(models.TextChoices):
    PUBLISHED="published","PUBLISHED"
    COMING_SOON="soon","Coming Soon"
    DRAFT="draft","DRAFT"
def handle_upload(instance,filename):
    return f"{filename}"
class Courses(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(blank=True,default="")
    image=models.ImageField(upload_to=handle_upload)
    access=models.CharField( max_length=100,
                                   choices=AcessRequirement.choices,
                                   default=AcessRequirement.EMAIL_REQUIRED)
    status=models.CharField( max_length=20,
                                   choices=PublishedStatus.choices,
                                   default=PublishedStatus.DRAFT)
@property
def is_published(self):
    return self.status == PublishedStatus.PUBLISHED




