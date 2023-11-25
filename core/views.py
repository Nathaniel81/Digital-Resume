from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse
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

from .forms import ContactForm

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

        return context

class Contact(generic.FormView):
    template_name = 'core/contact.html'
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Thank you. We will be in touch soon.')
        return super().form_valid(form)

class Portfolio(generic.ListView):
    model = Portfolio
    template_name = 'core/porfolio.html'
    paginate_by = 10
    
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

class Blog(generic.ListView):
    model = Blog
    template_name = 'core/blog.html'
    paginate_by = 10
    
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

