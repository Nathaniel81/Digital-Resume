from typing import Any
from django.shortcuts import render
from django.contrib import messages
from .models import (
		Profile,
		Blog,
		Portfolio,
		Testimonial,
		Certificate
	)

from django.views import generic

class Index(generic.TemplateView):
    template_name = 'core/index.html'
    def get_context_data(self, **kwargs):    
        context = super().get_context_data(**kwargs)

        testimonials = Testimonial.objects.filter(is_active=True)
        certificates = Certificate.objects.filter(is_active=True)
        blogs = Blog.objects.filter(is_active=True)
        portfolio = Portfolio.objects.filter(is_active=True)

        context["testimonials"] = testimonials
        context["certificates"] = certificates
        context["blogs"] = blogs
        context["portfolio"] = portfolio
        print(context)
        return context