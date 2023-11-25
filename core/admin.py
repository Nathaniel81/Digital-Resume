from django.contrib import admin
from . models import (
    Profile,
    ContactProfile,
    Testimonial,
    Media,
    Portfolio,
    Blog,
    Certificate,
    Skill
    )

admin.site.register(Profile)
admin.site.register(ContactProfile)
admin.site.register(Media)
admin.site.register(Testimonial)
admin.site.register(Blog)
admin.site.register(Portfolio)
admin.site.register(Certificate)
admin.site.register(Skill)
