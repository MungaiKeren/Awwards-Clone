# Generated by Django 2.2.6 on 2019-10-22 05:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mysite', '0002_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('design', models.PositiveSmallIntegerField(default=0)),
                ('usability', models.PositiveSmallIntegerField(default=0)),
                ('content', models.PositiveSmallIntegerField(default=0)),
                ('author', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(default='project_folder/responsive.jpg', on_delete=django.db.models.deletion.CASCADE, to='mysite.Projects')),
            ],
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
