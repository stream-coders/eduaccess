# Generated by Django 5.1 on 2024-09-12 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0003_course_prev_img'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['created_at']},
        ),
        migrations.AlterModelOptions(
            name='enrollment',
            options={'ordering': ['created_at']},
        ),
        migrations.AlterModelOptions(
            name='lesson',
            options={'ordering': ['created_at']},
        ),
        migrations.AlterModelOptions(
            name='module',
            options={'ordering': ['created_at']},
        ),
        migrations.AlterModelOptions(
            name='option',
            options={'ordering': ['created_at']},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['created_at']},
        ),
        migrations.AlterModelOptions(
            name='quiz',
            options={'ordering': ['created_at']},
        ),
        migrations.AlterModelOptions(
            name='resource',
            options={'ordering': ['created_at']},
        ),
        migrations.AlterModelOptions(
            name='score',
            options={'ordering': ['created_at']},
        ),
        migrations.AddField(
            model_name='user',
            name='profile_image',
            field=models.URLField(default='https://www.gravatar.com/avatar/00000000000000000000000000000000?d=mp&f=y'),
        ),
    ]
