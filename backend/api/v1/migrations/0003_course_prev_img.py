# Generated by Django 5.1 on 2024-09-12 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0002_user_groups_user_is_superuser_user_user_permissions'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='prev_img',
            field=models.URLField(default='https://picsum.photos/id/2/5000/3333'),
        ),
    ]
