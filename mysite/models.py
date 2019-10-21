from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
from django.http import Http404


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
    def get_project_by_id(cls, id):
        try:
            proj = Projects.objects.get(pk=id)
        except ObjectDoesNotExist:
            raise Http404()
        return proj

    @classmethod
    def get_projects(cls):
        project = cls.objects.all()
        return project

    @classmethod
    def search_by_title(cls, search_term):
        projects = cls.objects.filter(title__icontains=search_term)
        return projects

#
# class Comment(models.Model):
#     number = models.IntegerField(default=0)
#     comment = models.CharField(max_length=200)
#     date = models.DateTimeField(auto_now_add=True)
#     author = models.ForeignKey(User, on_delete=models.CASCADE, default='1')
#     project = models.ForeignKey(Projects, on_delete=models.CASCADE, default='project_folder/responsive.jpg')
#
#     def __str__(self):
#         return f'{self.username}'
#
#     class Meta:
#         ordering = ['-date']
#
#     @classmethod
#     def get_all_comments(cls):
#         comments = Comment.objects.all()
#         return comments
