from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pic = models.ImageField(upload_to='profile_photo/', blank=True, default='profile_photo/defaultprofile_Wk2PTL2.jpg')
    bio = models.CharField(max_length=265, blank=True)
    contact_info = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'


class Projects(models.Model):
    image = models.ImageField(upload_to='project_folder')
    title = models.CharField(max_length=255)
    description = models.TextField()
    link = models.CharField(max_length=200)
    post_date = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default='1')
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='1')

    def __str__(self):
        return f'{self.profile.user.username}'

    class Meta:
        ordering = ['-post_date']

    @classmethod
    def get_projects(cls):
        project = cls.objects.all()
        return project

    @classmethod
    def search_by_title(cls, search_term):
        projects = cls.objects.filter(title__icontains=search_term)
        return projects

