from django.db import models
from common.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import F
# Create your models here.

class Region(models.Model):
    region = models.CharField(max_length=128)

    def __str__(self):
        return self.region

class ProfessionalField(models.Model):
    field = models.CharField(max_length=128)
    slug = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.field

class OfficialPosition(models.Model):
    field = models.ManyToManyField(ProfessionalField, related_name='field_name')
    position = models.CharField(max_length=128)
    slug = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.position

class Status(models.Model):
    title = models.CharField(max_length=128)
    slug = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.title

class Category(models.Model):  # Subject
    title = models.CharField(max_length=128)
    slug = models.CharField(max_length=128)
    icon = models.FileField(upload_to="category/")

    def __str__(self):
        return str(self.title)

class WorkerPost(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    worker_count = models.PositiveIntegerField(default=0)
    icon = models.FileField(upload_to='workerpost/')

    # def update_score(self):
    #     user = User.objects.filter(job_field=self.category)


class Company(models.Model):
    title = models.CharField(max_length=256)

# For Vacancy
class Post(models.Model):
    job_field = models.ForeignKey(ProfessionalField, on_delete=models.CASCADE, related_name='field_fromPost')
    job_position = models.ForeignKey(OfficialPosition, on_delete=models.CASCADE, related_name='position_name')
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    min_price = models.PositiveIntegerField(blank=True)
    max_price = models.PositiveIntegerField()
    posted_date = models.DateField(auto_now=False)
    location = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='job_location')

    job_status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='job_status')

    times_seen = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.job_position)

class Statistic(models.Model):
    company_count = models.PositiveIntegerField(default=0)
    user_count = models.PositiveIntegerField(default=0)
    vacancy_count = models.PositiveIntegerField(default=0)

@receiver(post_save, sender=User)
def update_user_count(sender, instance, created, **kwargs):
    if created:
        Statistic.objects.update(user_count=F('user_count') + 1)

@receiver(post_save, sender=Company)
def update_company_count(sender, instance, created, **kwargs):
    if created:
        Statistic.objects.update(company_count=F('company_count') + 1)

@receiver(post_save, sender=Post)
def update_vacancy_count(sender, instance, created, **kwargs):
    if created:
        Statistic.objects.update(vacancy_count=F('vacancy_count') + 1)