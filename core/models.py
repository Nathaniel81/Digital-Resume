from django.db import models
from django.contrib.auth.models import User


class Skill(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    image = models.FileField(blank=True, null=True, upload_to='skills')
    score = models.IntegerField(default=80, blank=True, null=True)
    key_skill = models.BooleanField(default=False)
    class Meta:
         verbose_name_plural = 'Skills'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, null=True, upload_to="avatar")
    title = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    skills = models.ManyToManyField(Skill, blank=True)
    cv = models.FileField(blank=True, null=True, upload_to="cv")

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

class ContactProfile(models.Model):
    name = models.CharField(verbose_name="Name", max_length=100)
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Message")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Contact Profiles'
        verbose_name = 'Contact Profile'
        ordering = ["created_at"]

    def __str__(self):
        return f'{self.name}'

class Testimonial(models.Model):
    thumbnail = models.ImageField(blank=True, null=True, upload_to="testimonials")
    name = models.CharField(max_length=200, blank=True, null=True)
    role = models.CharField(max_length=200, blank=True, null=True)
    quote = models.CharField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name_plural = 'Testimonials'
        ordering = ["name"]

    def __str__(self):
        return self.name

class Certificate(models.Model):
    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name_plural = 'Certificates'
        verbose_name = 'Certificate'

    def __str__(self):
        return self.name
