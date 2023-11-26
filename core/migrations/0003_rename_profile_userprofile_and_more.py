# Generated by Django 4.2.7 on 2023-11-26 07:10

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_media'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profile',
            new_name='UserProfile',
        ),
        migrations.AlterModelOptions(
            name='contactprofile',
            options={'ordering': ['timestamp'], 'verbose_name': 'Contact Profile', 'verbose_name_plural': 'Contact Profiles'},
        ),
        migrations.AlterModelOptions(
            name='skill',
            options={'verbose_name': 'Skill', 'verbose_name_plural': 'Skills'},
        ),
        migrations.AlterModelOptions(
            name='testimonial',
            options={'ordering': ['name'], 'verbose_name': 'Testimonial', 'verbose_name_plural': 'Testimonials'},
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': 'User Profile', 'verbose_name_plural': 'User Profiles'},
        ),
        migrations.RenameField(
            model_name='contactprofile',
            old_name='created_at',
            new_name='timestamp',
        ),
        migrations.RenameField(
            model_name='skill',
            old_name='key_skill',
            new_name='is_key_skill',
        ),
    ]
